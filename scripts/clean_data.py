import pandas as pd

def clean_customer_data(input_file='Consistent_data.csv', output_file='cleaned_data.csv'):
    # Step 1: Load the data
    df = pd.read_csv(input_file)

    print("Null values BEFORE cleaning:\n")
    print(df.isnull().sum())
    print("\nTotal null values before cleaning:", df.isnull().sum().sum())
    print("-" * 50)

    # Step 2: Drop rows where 'CustomerID' is missing
    df = df.dropna(subset=['CustomerID'])

    # Step 3: Handle missing 'Tenure'
    if 'Tenure' in df.columns:
        missing_tenure_ratio = df['Tenure'].isnull().mean()

        if missing_tenure_ratio <= 0.02:
            df = df.dropna(subset=['Tenure'])
        else:
            tenure_median = df['Tenure'].median()
            df['Tenure'] = df['Tenure'].fillna(tenure_median)

    # Step 4: Fill other numeric missing values with median
    numeric_columns = df.select_dtypes(include='number').columns

    for col in numeric_columns:
        if col != 'Tenure':
            median_value = df[col].median()
            df[col] = df[col].fillna(median_value)

    # Step 5: Fill missing 'Gender' with mode (most common value)
    if 'Gender' in df.columns:
        gender_mode = df['Gender'].mode()[0]
        df['Gender'] = df['Gender'].fillna(gender_mode)

    # Step 6: Handle outliers using IQR method
    for col in numeric_columns:
        print(f"\nHandling outliers in '{col}'")
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        df[col] = df[col].apply(lambda x: lower if x < lower else upper if x > upper else x)
        print("Outliers removed.")

    # Step 7: Save cleaned data
    print("\n" + "-" * 50)
    print("Null values AFTER cleaning:\n")
    print(df.isnull().sum())
    print("\nTotal null values after cleaning:", df.isnull().sum().sum())

    df.to_csv(output_file, index=False)
    print("\nAfter cleaning, number of samples:", len(df))
    print(f"Cleaned data saved to '{output_file}'")

    return df
