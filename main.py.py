import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    confusion_matrix, 
    accuracy_score, 
    precision_score, 
    recall_score, 
    classification_report
)
from sklearn.preprocessing import MinMaxScaler
import pickle

from featureengineering import feature_engineering  # Your feature engineering file

# Step 1: Load the dataset
df = pd.read_csv("cleaned_customer_data_with_churn.csv")

# Step 2: Separate target variable
y = df['Churn']

# Step 3: Drop target column before feature engineering
df_features = df.drop('Churn', axis=1)

# Step 4: Apply feature engineering
X = feature_engineering(df_features)

# Step 4.1: Drop CustomerID if present
if 'CustomerID' in X.columns:
    X.drop('CustomerID', axis=1, inplace=True)

# Step 4.2: One-hot encode categorical variables
X = pd.get_dummies(X)

# Step 4.3: Scale numeric features
scaler = MinMaxScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

# Step 5: Stratified split to preserve class ratio
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)

# Step 6: Train Random Forest with class_weight='balanced'
model = RandomForestClassifier(random_state=42, class_weight='balanced')
model.fit(X_train, y_train)

# Step 7: Predict
y_pred = model.predict(X_test)

# Step 8: Evaluate
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, pos_label='Yes', zero_division=0))
print("Recall:", recall_score(y_test, y_pred, pos_label='Yes', zero_division=0))

# Step 8.1: Detailed report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Step 9: Feature importance
importances = model.feature_importances_
feature_names = X.columns
importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importances
}).sort_values(by='Importance', ascending=False)

top_3 = importance_df.head(3)
print("\nTop 3 Important Features:")
print(top_3)

# Step 10: Save model
with open("random_forest_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("\nModel saved as 'random_forest_model.pkl'")
