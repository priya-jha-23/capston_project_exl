import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def feature_engineering(df):
    df = df.copy()

    # 1. Drop ID column if it exists
    if 'CustomerID' in df.columns:
        df = df.drop('CustomerID', axis=1)

    # 2. Identify categorical and numerical columns
    categorical_cols = df.select_dtypes(include=['object', 'category', 'bool']).columns
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    # 3. Apply MinMaxScaler only to numeric columns
    scaler = MinMaxScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    # 4. One-Hot Encode categorical columns
    df = pd.get_dummies(df, columns=categorical_cols)

    return df

