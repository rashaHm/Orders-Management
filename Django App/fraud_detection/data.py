import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)

# Define parameters
num_rows = 1000
order_amounts = np.random.uniform(10, 1000, num_rows)  # Random order amounts between $10 and $1000

# Sample email domains
email_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'company.com', 'edu.com']
customer_email_domains = [random.choice(email_domains) for _ in range(num_rows)]

# Generate past fraud history (0 = no fraud, 1 = past fraud)
past_fraud_history = np.random.choice([0, 1], size=num_rows, p=[0.85, 0.15])  # 85% legitimate, 15% fraudulent

# Create a DataFrame
data = {
    'Order Amount': order_amounts,
    'Customer Email Domain': customer_email_domains,
    'Past Fraud History': past_fraud_history,
}

df = pd.DataFrame(data)

# Simulate fraud probability score (0-100%)
def calculate_fraud_probability(row):
    base_probability = 5  # Base probability
    if row['Order Amount'] > 700:
        base_probability += 40  # Higher amounts increase fraud risk
    elif row['Order Amount'] > 300:
        base_probability += 20  # Moderate amounts also increase risk
        
    if row['Customer Email Domain'] == 'company.com':
        base_probability -= 15  # Company emails are less likely to be fraudulent
    elif row['Customer Email Domain'] == 'edu.com':
        base_probability -= 10  # Educational emails are also less risky

    if row['Past Fraud History'] == 1:
        base_probability += 50  # Past fraud history significantly increases risk
    
    # Cap the probability at 100%
    return min(base_probability, 100)

# Apply the function to calculate fraud probabilities
df['Fraud Probability (%)'] = df.apply(calculate_fraud_probability, axis=1)

# Save the DataFrame to a CSV file
df.to_csv('fraud_data.csv', index=False)

print("Dummy dataset created and saved as 'fraud_data.csv'")