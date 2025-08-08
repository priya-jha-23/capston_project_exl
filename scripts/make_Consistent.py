import pandas as pd

def make_consistence(input_csv='Customer-Churn-Records.csv', output_csv='Consistent_data.csv'):
    # Load the dataset
    df = pd.read_csv(input_csv)

    # Step 1: Remove duplicates and check for null CustomerID
    df.drop_duplicates(subset='CustomerID', inplace=True)
    df = df[df['CustomerID'].notna()]

    # Step 2: Enforce data consistency rules
    df = df[(df['CreditScore'] >= 300) & (df['CreditScore'] <= 850)]        # CreditScore
    df = df[(df['Age'] >= 5) & (df['Age'] <= 100)]                           # Age
    df = df[(df['Tenure'] >= 0) & (df['Tenure'] <= 10)]                      # Tenure
    df = df[df['Balance'] >= 0]                                             # Balance
    df = df[df['NumOfProducts'] >= 1]                                       # NumOfProducts
    df['NumOfProducts'] = df['NumOfProducts'].apply(lambda x: int(x // 1))  # Round down
    df = df[df['HasCrCard'].isin([0, 1])]                                   # HasCrCard
    df = df[df['IsActiveMember'].isin([0, 1])]                              # IsActiveMember
    df = df[df['EstimatedSalary'] >= 0]                                     # EstimatedSalary

    # Step 3: View unique gender values
    unique_genders = df['Gender'].dropna().unique()
    print("Unique Gender values:\n", unique_genders)

    # Step 4: Ask user to map each unique value
    gender_map = {}
    for g in unique_genders:
        print(f"\nHow should '{g}' be categorized?")
        choice = input("Enter [M]ale, [F]emale, or [U]nknown: ").strip().upper()

        if choice == 'M':
            gender_map[g] = 'Male'
        elif choice == 'F':
            gender_map[g] = 'Female'
        else:
            gender_map[g] = ''

    # Step 5: Apply the mapping
    df['Gender'] = df['Gender'].map(gender_map)

    print("\nAfter consistent mapping, length of dataset:", len(df))

    # Step 6: Save cleaned data
    df.to_csv(output_csv, index=False)
    print(f"\nCleaned data saved as '{output_csv}'")

    return df
