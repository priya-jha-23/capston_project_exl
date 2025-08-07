import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from featureengineering import feature_engineering 

# Load the cleaned data
df = pd.read_csv('cleaned_data_with_churn.csv')


# # Set global style and color palette
# sns.set(style='whitegrid')
# main_palette = ['#2C3E50', '#3498DB', '#A3C9F5']  # Blue tones

# # 1. Gender Distribution
# plt.figure(figsize=(6, 4))
# sns.countplot(x='Gender', data=df, palette=main_palette)
# plt.title('Gender Distribution', fontsize=14)
# plt.xlabel('Gender', fontsize=12)
# plt.ylabel('Customer Count', fontsize=12)
# plt.tight_layout()
# plt.show()

# # 2. Age Distribution
# plt.figure(figsize=(6, 4))
# sns.histplot(df['Age'], kde=True, bins=20, color='#3498DB')
# plt.title('Age Distribution', fontsize=14)
# plt.xlabel('Age', fontsize=12)
# plt.ylabel('Frequency', fontsize=12)
# plt.tight_layout()
# plt.show()

# # 3. Tenure Distribution
# plt.figure(figsize=(6, 4))
# sns.countplot(x='Tenure', data=df, palette=sns.color_palette("Blues", as_cmap=False))
# plt.title('Tenure Distribution', fontsize=14)
# plt.xlabel('Tenure (Years)', fontsize=12)
# plt.ylabel('Customer Count', fontsize=12)
# plt.tight_layout()
# plt.show()

# # 4. Balance Distribution
# plt.figure(figsize=(6, 4))
# sns.histplot(df['Balance'], kde=True, bins=20, color='#1F618D')
# plt.title('Balance Distribution', fontsize=14)
# plt.xlabel('Balance', fontsize=12)
# plt.ylabel('Frequency', fontsize=12)
# plt.tight_layout()
# plt.show()

# # 5. NumOfProducts Distribution
# plt.figure(figsize=(6, 4))
# sns.countplot(x='NumOfProducts', data=df, palette=main_palette)
# plt.title('Number of Products Distribution', fontsize=14)
# plt.xlabel('NumOfProducts', fontsize=12)
# plt.ylabel('Customer Count', fontsize=12)
# plt.tight_layout()
# plt.show()

# # 6. HasCrCard Distribution
# plt.figure(figsize=(6, 4))
# sns.countplot(x='HasCrCard', data=df, palette=main_palette)
# plt.title('Credit Card Ownership', fontsize=14)
# plt.xlabel('Has Credit Card (0 = No, 1 = Yes)', fontsize=12)
# plt.ylabel('Customer Count', fontsize=12)
# plt.tight_layout()
# plt.show()

# # 7. IsActiveMember Distribution
# plt.figure(figsize=(6, 4))
# sns.countplot(x='IsActiveMember', data=df, palette=main_palette)
# plt.title('Active Membership Distribution', fontsize=14)
# plt.xlabel('Is Active Member (0 = No, 1 = Yes)', fontsize=12)
# plt.ylabel('Customer Count', fontsize=12)
# plt.tight_layout()
# plt.show()

# # 8. Estimated Salary Distribution
# plt.figure(figsize=(6, 4))
# sns.histplot(df['EstimatedSalary'], kde=True, bins=20, color='#117A65')
# plt.title('Estimated Salary Distribution', fontsize=14)
# plt.xlabel('Estimated Salary', fontsize=12)
# plt.ylabel('Frequency', fontsize=12)
# plt.tight_layout()
# plt.show()

# # 9. Churn Distribution
# plt.figure(figsize=(6, 4))
# sns.countplot(x='Churn', data=df, palette=main_palette)
# plt.title('Churn Distribution', fontsize=14)
# plt.xlabel('Churn (0 = No, 1 = Yes)', fontsize=12)
# plt.ylabel('Customer Count', fontsize=12)
# plt.tight_layout()
# plt.show()


# # # Visualizing relationships between features and churn


sns.set(style="whitegrid")  # Clean background

# Define a professional color palette
palette_main = ['#2C3E50', '#3498DB']  # Dark Blue, Sky Blue (for Churn: No, Yes)
box_palette = ['#A3C9F5', '#1F4788']   # For boxplots

# # 1. Gender vs Churn
# plt.figure(figsize=(6, 4))
# sns.countplot(x='Gender', hue='Churn', data=df, palette=palette_main)
# plt.title('Gender vs Churn', fontsize=14)
# plt.xlabel('Gender', fontsize=12)
# plt.ylabel('Customer Count', fontsize=12)
# plt.legend(title='Churn')
# plt.tight_layout()
# plt.show()

# # 2. Age vs Churn (Box plot)
# plt.figure(figsize=(6, 4))
# sns.boxplot(x='Churn', y='Age', data=df, palette=box_palette)
# plt.title('Age Distribution by Churn', fontsize=14)
# plt.xlabel('Churn', fontsize=12)
# plt.ylabel('Age', fontsize=12)
# plt.tight_layout()
# plt.show()

# 3. Tenure vs Churn
plt.figure(figsize=(6, 4))
sns.boxplot(x='Churn', y='Tenure', data=df, palette=box_palette)
plt.title('Tenure Distribution by Churn', fontsize=14)
plt.xlabel('Churn', fontsize=12)
plt.ylabel('Tenure (Months)', fontsize=12)
plt.tight_layout()
plt.show()

# # 4. Balance vs Churn
# plt.figure(figsize=(6, 4))
# sns.boxplot(x='Churn', y='Balance', data=df, palette=box_palette)
# plt.title('Balance vs Churn', fontsize=14)
# plt.xlabel('Churn', fontsize=12)
# plt.ylabel('Account Balance', fontsize=12)
# plt.tight_layout()
# plt.show()

# # 5. NumOfProducts vs Churn
# plt.figure(figsize=(6, 4))
# sns.countplot(x='NumOfProducts', hue='Churn', data=df, palette=palette_main)
# plt.title('Number of Products vs Churn', fontsize=14)
# plt.xlabel('Number of Products', fontsize=12)
# plt.ylabel('Customer Count', fontsize=12)
# plt.legend(title='Churn')
# plt.tight_layout()
# plt.show()

# # 6. HasCrCard vs Churn
# plt.figure(figsize=(6, 4))
# sns.countplot(x='HasCrCard', hue='Churn', data=df, palette=palette_main)
# plt.title('Credit Card Ownership vs Churn', fontsize=14)
# plt.xlabel('Has Credit Card (0 = No, 1 = Yes)', fontsize=12)
# plt.ylabel('Customer Count', fontsize=12)
# plt.legend(title='Churn')
# plt.tight_layout()
# plt.show()

# # 7. IsActiveMember vs Churn
# plt.figure(figsize=(6, 4))
# sns.countplot(x='IsActiveMember', hue='Churn', data=df, palette=palette_main)
# plt.title('Active Membership vs Churn', fontsize=14)
# plt.xlabel('Is Active Member (0 = No, 1 = Yes)', fontsize=12)
# plt.ylabel('Customer Count', fontsize=12)
# plt.legend(title='Churn')
# plt.tight_layout()
# plt.show()

# # 8. EstimatedSalary vs Churn
# plt.figure(figsize=(6, 4))
# sns.boxplot(x='Churn', y='EstimatedSalary', data=df, palette=box_palette)
# plt.title('Estimated Salary vs Churn', fontsize=14)
# plt.xlabel('Churn', fontsize=12)
# plt.ylabel('Estimated Salary', fontsize=12)
# plt.tight_layout()
# plt.show()


# # Gender distribution
# gender_counts = df['Gender'].value_counts()

# # Map specific colors by label
# color_map = {'Male': '#87CEEB', 'Female': '#FFC0CB'}  # Blue for Male, Pink for Female
# colors = [color_map[label] for label in gender_counts.index]

# # Create pie chart
# plt.figure(figsize=(6, 6))
# wedges, texts, autotexts = plt.pie(
#     gender_counts.values,
#     labels=None,
#     autopct='%1.1f%%',
#     startangle=140,
#     colors=colors,
#     wedgeprops=dict(edgecolor='white'),
#     textprops=dict(color="black", fontsize=12)
# )

# # Add title
# plt.title('Gender Distribution')

# # Add legend with correct labels
# plt.legend(wedges, gender_counts.index, title="Gender", loc="center left", bbox_to_anchor=(1, 0.5))

# plt.axis('equal')
# plt.tight_layout()
# plt.show()




# # Count active/inactive members
# active_counts = df['IsActiveMember'].value_counts()
# active_labels = ['Active' if i == 1 else 'Inactive' for i in active_counts.index]

# # Define color mapping explicitly
# color_map = {
#     'Active': '#2C3E50',    # Charcoal Blue (modern, strong)
#     'Inactive': '#BDC3C7'   # Light Silver Gray (clean, neutral)
# }
# colors = [color_map[label] for label in active_labels]

# # Plot pie chart
# plt.figure(figsize=(6, 6))
# wedges, texts, autotexts = plt.pie(
#     active_counts.values,
#     labels=None,  # We'll use legend instead
#     autopct='%1.1f%%',
#     startangle=140,
#     colors=colors,
#     wedgeprops=dict(edgecolor='white'),
#     textprops=dict(color="white", fontsize=12)
# )

# # Title
# plt.title('Is Active Member Distribution', color='black')

# # Add legend to label the colors properly
# plt.legend(wedges, active_labels, title="Membership", loc="center left", bbox_to_anchor=(1, 0.5))

# plt.axis('equal')
# plt.tight_layout()
# plt.show()



# # Churn distribution
# churn_counts = df['Churn'].value_counts()
# churn_labels = churn_counts.index  # Typically: ['No', 'Yes']

# # Use two different shades of blue
# color_map = {'No': '#6baed6', 'Yes': '#2171b5'}  # Light & Dark blue
# colors = [color_map[label] for label in churn_labels]

# # Create pie chart
# plt.figure(figsize=(6, 6))
# wedges, texts, autotexts = plt.pie(
#     churn_counts.values,
#     labels=None,  # We'll use legend for labels
#     autopct='%1.1f%%',
#     startangle=140,
#     colors=colors,
#     wedgeprops=dict(edgecolor='white'),
#     textprops=dict(color="black", fontsize=12)
# )

# # Add title
# plt.title('Churn Distribution')

# # Add legend at the side
# plt.legend(wedges, churn_labels, title="Churn", loc="center left", bbox_to_anchor=(1, 0.5))

# plt.axis('equal')
# plt.tight_layout()
# plt.show()



# # Drop 'CustomerID' if it exists
# if 'CustomerID' in df.columns:
#     df = df.drop('CustomerID', axis=1)

# # Select only numeric columns
# numeric_df = df.select_dtypes(include=['number'])

# # Compute correlation matrix
# corr_matrix = numeric_df.corr()



# # Plot the correlation heatmap
# plt.figure(figsize=(12, 8))
# sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar=True)
# plt.title("Correlation Matrix")
# plt.show()
