# Credit Card Churn Prediction Using Machine Learning

## Objective
Develop a predictive model that identifies customers likely to churn (discontinue using a credit card), enabling proactive customer retention strategies.

---

## Problem Statement
Customer attrition is a major concern in the banking sector. By predicting potential churners in advance, banks can take timely actions such as offering incentives or improved services to retain them.

---

## Dataset
- **Source:** [Kaggle](https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset)  
- **Records:** ~10,000 customer entries  
- **Features:**  
  - `CustomerId`, `Gender`, `Age`, `Tenure`, `Balance`, `NumOfProducts`, `HasCrCard`, `IsActiveMember`, `EstimatedSalary`, etc.
- **Target Variable:** `Exited` (1 = churned, 0 = not churned)

---

## Technology Stack
- **Programming Language:** Python  
- **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn  
- **Model:** Random Forest Classifier (Ensemble Learning)  
- **Tools:** VS Code  

---

## Data Preprocessing & Feature Engineering
- Handled missing values
- Encoded categorical variables (e.g., Gender)
- Normalized/scaled numerical features
- Split data into:
  - **Training set:** 9494 samples
  - **Test set:** 477 samples

---

## Exploratory Data Analysis (EDA)
- Visualized churn distribution
- Feature analysis using:
  - Correlation heatmaps
  - Bar plots for categorical variables
  - Box plots for numerical variables
- Key findings:
  - Inactive members and customers with fewer products were more likely to churn

---

## Model Building
- Tested multiple models, with **Random Forest** performing the best
- Hyperparameter tuning via GridSearchCV (no significant improvement, Random Forest remained most robust)

---

## Model Evaluation
- **Accuracy:** 99.21%  
- **Metrics:** Accuracy, Precision, Recall, F1 Score  
- **Visualization:** Confusion Matrix

---

## Deployment
- **GitHub Repo:** [Click Here](https://github.com/priya-jha-23/capston_project_exl)

---

## Results & Insights
- The model accurately identifies customers likely to churn
- **Top contributing features:**
  - Tenure
  - EstimatedSalary
  - Balance
- Enables proactive retention strategies

---

## Future Work
- Integrate real-time data from AWS RDS
- Test with larger and more diverse datasets
- Explore deep learning models and SHAP explainability
- Implement cost-sensitive learning for churn probability-based decision-making

---

## References
- [Kaggle Credit Card Dataset](https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset)  
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)

---

**Author:** Priya Jha  
Email: priyajha28111999@gmail.com  

