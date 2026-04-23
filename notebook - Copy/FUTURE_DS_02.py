
import pandas as pd
import matplotlib.pyplot as plt
# Load data
df = pd.read_csv(r"E:\Project1\WA_Fn-UseC_-Telco-Customer-Churn.csv")
# Cleaning
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df = df.dropna()
# Convert churn to numeric
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# Analysis Area

# Churn rate
print("Churn Rate:", df['Churn'].mean()*100)
# Contract churn
contract = df.groupby('Contract')['Churn'].mean()
# Payment churn
payment = df.groupby('PaymentMethod')['Churn'].mean()
# Tenure churn
tenure = df.groupby('tenure')['Churn'].mean()
# Charges churn
charges = df.groupby('Churn')['MonthlyCharges'].mean()

# Dashboard (one sheet bar chart)

fig, axes = plt.subplots(2, 2, figsize=(12,10))
contract.plot(kind='bar', ax=axes[0,0], title="Churn by Contract")
payment.plot(kind='bar', ax=axes[0,1], title="Churn by Payment")
tenure.plot(ax=axes[1,0], title="Churn vs Tenure")
charges.plot(kind='bar', ax=axes[1,1], title="Charges vs Churn")
plt.tight_layout()
plt.show()
