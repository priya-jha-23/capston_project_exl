import pandas as pd

# Load the customer data
df1 = pd.read_csv("cleaned_data.csv")

# Apply churn conditions
def detect_churn(row):
    # Avoid division by zero
    if row["Tenure"] == 0:
        return 'No'
    avg_monthly_spend = row["Balance"] / row["Tenure"]
    last_known_avg = row["EstimatedSalary"] 
    if row["Tenure"] <= 3 and avg_monthly_spend < 0.5 * last_known_avg:
        return 'Yes'
    return 'No'


df1["Churn"] = df1.apply(detect_churn, axis=1)

# Save new CSV with churn
df1.to_csv("cleaned_data_with_churn.csv", index=False)




