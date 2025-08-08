import pandas as pd

def detect_churn_from_file(input_csv="cleaned_data.csv", output_csv="cleaned_data_with_churn.csv"):
    """
    Reads customer data from input_csv, applies churn detection logic,
    adds a 'Churn' column, saves the result to output_csv, and returns the DataFrame.
    """
    # Load the customer data
    df = pd.read_csv(input_csv)

    # Define churn condition
    def detect_churn(row):
        if row["Tenure"] == 0:
            return 'No'
        avg_monthly_spend = row["Balance"] / row["Tenure"]
        last_known_avg = row["EstimatedSalary"]
        if row["Tenure"] <= 3 and avg_monthly_spend < 0.5 * last_known_avg:
            return 'Yes'
        return 'No'

    # Apply churn detection
    df["Churn"] = df.apply(detect_churn, axis=1)

    # Save to new file
    df.to_csv(output_csv, index=False)
    print(f"Churn column added and saved to {output_csv}")

    # Return the modified DataFrame
    return df
