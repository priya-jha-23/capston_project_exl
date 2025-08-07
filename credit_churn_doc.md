# EXL Capstone Project Documentation

## Project Title: Credit Card Churn Prediction

**Organization:** EXL\
**Track:** Python + AI/ML + AWS Cloud Integration\
**Team:** Individual\
**Submission Mode:** GitHub + AWS + PPT Presentation

---

## 1. Business Scenario

EXL's Credit Card Analytics Division has noted a reduction in customer retention within specific user segments. The internal data science team seeks a proof-of-concept (PoC) to:

- Predict which customers are likely to churn based on behavioral and demographic data.
- Identify early warning signals using data science and visual analytics.
- Simulate a production-like environment by deploying the full pipeline using AWS Aurora MySQL and EC2.

---

## 2. Key Business Definitions

**Churn Definition:** A customer is considered churned if:

- They have not transacted for over 3 months,
- Their average monthly spend has dropped below 50% of their previous average,
- They are marked as "Churn = Yes" in the dataset.

This aligns with industry-standard KPIs used by banks and financial institutions.

---

## 3. Dataset and Encoding Guidelines

- **Dataset File:** `exl_credit_card_customers.csv`
- **Data Type:** Structured CSV data
- **Synthetic Expansion:** Allowed while maintaining column consistency
- **Encoding:**
  - Categorical columns must be encoded using **One-Hot Encoding**
  - **Label encoding/manual mapping is prohibited** to maintain uniform feature space

---

## 4. Git & Branching Strategy

Participants are required to maintain GitHub repositories with the following branches:

- `main` - Final working code
- `dev` - Development branch
- `feature/eda` - Exploratory Data Analysis
- `feature/ml` - Model training and evaluation
- `feature/aws` - AWS deployment scripts
- `presentation` - Final presentation assets

---

## 5. Cloud Infrastructure Requirements

### Step-by-Step AWS Setup

**Step 1: RDS Setup (Aurora MySQL)**

- Create DB: `exl_churn_db`
- Create table: `customers`
- Load CSV data into the table

**Step 2: EC2 Setup**

- Launch EC2 Ubuntu instance
- Install Python 3.9+, and required libraries
- Clone GitHub repo

**Step 3: Execute ML Pipeline**

- Read data from Aurora
- Run preprocessing and train Logistic Regression model
- Save predictions back to Aurora in a table `churn_predictions`

---

## 6. Task Breakdown

### Day 1: Data Acquisition & Exploration

- Load dataset using Pandas
- Upload to Aurora DB and validate via SQL queries
- EDA: Age distribution, churn ratio, tenure, card type analysis, and correlation matrix
- Visualizations stored under `feature/eda`

### Day 2: Feature Engineering & Modeling

- One-Hot Encoding for all categorical variables
- Normalize numerical columns using MinMaxScaler
- Train Logistic Regression model
- Evaluate using Confusion Matrix, Accuracy, Precision, Recall
- Store insights and model in `feature/ml`

### Day 3: AWS Execution & Final Reporting

- Connect EC2 instance with Aurora DB
- Predict on test data and store in `churn_predictions`
- Prepare 5-slide PPT:
  - Problem Statement
  - EDA Summary
  - Model Performance
  - AWS Architecture
  - Final Recommendations
- Final code and PPT pushed to respective branches


---

## 7. Project Directory Structure

```plaintext
exl-credit-churn-analysis/
├── data/
│   ├── raw/
│   │   └── exl_credit_card_churn_data.csv
│   └── processed/
│       └── churn_cleaned.csv
├── scripts/
│   ├── data_loader.py
│   ├── data_cleaner.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   ├── model_predict.py
│   └── model_serializer.py
├── model/
│   ├── churn_model.pkl
│   └── model_metrics.txt
├── aws/
│   ├── rds_setup.md
│   └── ec2_connection.md
├── git/
│   └── git_flow.md
├── presentation/
│   └── churn_project_ppt.pptx
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 8. Technology Stack

- **Programming Language:** Python 3.9+
- **Libraries:** pandas, numpy, scikit-learn, seaborn, matplotlib, mysql-connector-python
- **Model:** Logistic Regression
- **Cloud Services:** AWS EC2 (Ubuntu), AWS Aurora MySQL (RDS)
- **Version Control:** Git & GitHub

---

## 9. Key Insights

- Age, tenure, and activity levels showed high correlation with churn.
- Logistic Regression performed well in identifying churned customers.
- Normalized and one-hot encoded features improved model performance.

---

## 10. Future Scope

- Upgrade model to Random Forest or XGBoost for better performance
- Automate retraining pipeline using AWS Lambda or S3 Triggers
- Integrate real-time dashboards using AWS QuickSight or Streamlit

---

## 11. Author

**Name:** [Priya Jha]\
**Email:** [[priyajha28111999@gmail.com](mailto\:priyajha28111999@gmail.com)]\
**GitHub Repo:** [[github.com/your\_username/exl-credit-churn-analysis](https://github.com/priya-jha-23/capston_project_exl)]

