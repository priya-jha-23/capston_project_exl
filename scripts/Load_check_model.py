import pandas as pd
import pickle
import matplotlib.pyplot as plt
from sklearn.metrics import (
    classification_report, 
    accuracy_score, 
    confusion_matrix, 
    ConfusionMatrixDisplay
)
from sklearn.preprocessing import MinMaxScaler
from featureengineering import feature_engineering

# Step 1: Load the test data (10 samples)
test_data = pd.read_csv('test_data.csv')

print("Test data loaded successfully. Number of samples:", len(test_data))

# Step 2: Separate true labels before transformation
y_true = test_data['Churn'].map({'No': 0, 'Yes': 1})  # Ensure numeric
X_test = test_data.drop(columns=['CustomerID', 'Churn'])

# Step 3: Apply feature engineering
X_test_transformed = feature_engineering(X_test)

# Step 3.1: One-hot encode if required (based on training process)
X_test_transformed = pd.get_dummies(X_test_transformed)

# Step 3.2: Align test columns with training features
with open("random_forest_model_hyp.pkl", "rb") as f:
    model = pickle.load(f)

# Ensure test features match training features
expected_features = model.feature_names_in_
for col in expected_features:
    if col not in X_test_transformed.columns:
        X_test_transformed[col] = 0  # add missing column with default 0

X_test_transformed = X_test_transformed[expected_features]  # reorder columns

# Step 3.3: Scale using MinMaxScaler (same method used in training)
scaler = MinMaxScaler()
X_test_scaled = pd.DataFrame(scaler.fit_transform(X_test_transformed), columns=X_test_transformed.columns)

# Step 4: Predict using the model
y_pred = model.predict(X_test_scaled)

# Step 5: If predictions are in 'Yes'/'No', convert to 0/1
if y_pred.dtype == object:
    y_pred = pd.Series(y_pred).map({'No': 0, 'Yes': 1})

# Step 6: Evaluate
print("Accuracy:", accuracy_score(y_true, y_pred))
print("Classification Report:\n", classification_report(y_true, y_pred))

# Step 7: Confusion matrix
cm = confusion_matrix(y_true, y_pred)
print("Confusion Matrix:\n", cm)

# Step 8: Plot confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['No', 'Yes'])
fig, ax = plt.subplots(figsize=(6, 6))
disp.plot(ax=ax, cmap='Blues', values_format='d')
plt.title("Confusion Matrix")
plt.grid(False)
plt.show()
