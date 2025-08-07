import pandas as pd

# Load the dataset
df = pd.read_csv('Customer-Churn-Records.csv')

# Step 1: Remove duplicates and check for null CustomerID
df.drop_duplicates(subset='CustomerID', inplace=True)
df = df[df['CustomerID'].notna()]

# Step 2: Enforce data consistency rules

# CreditScore: Keep between 300 and 850
df = df[(df['CreditScore'] >= 300) & (df['CreditScore'] <= 850)]

# Age: Keep between 18 and 100
df = df[(df['Age'] >= 5) & (df['Age'] <= 100)]

# Tenure: Non-negative, realistic max 10
df = df[(df['Tenure'] >= 0) & (df['Tenure'] <= 10)]

# Balance: No negative balances
df = df[df['Balance'] >= 0]

# NumOfProducts: At least 1(Then only customer can be considered)
df = df[(df['NumOfProducts'] >= 1)]

# Product: Should be a whole number, assume max 4
df['NumOfProducts'] = df['NumOfProducts'].apply(lambda x: int(x // 1))

# HasCrCard and IsActiveMember: Should be 0 or 1
df = df[df['HasCrCard'].isin([0, 1])]
df = df[df['IsActiveMember'].isin([0, 1])]

# EstimatedSalary: Should be non-negative
df = df[df['EstimatedSalary'] >= 0]

# Product: Should be a whole number, assume max 4
df['NumOfProducts'] = df['NumOfProducts'].apply(lambda x: int(x // 1))

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

print("\n After consistent mapping length of dataset:", len(df))
# Step 6: Save cleaned data
df.to_csv("Consistent_data.csv", index=False)
print("\nCleaned data saved as 'modified_customer_data.csv'")
