import pandas as pd
import numpy as np

# Create a dummy dataset
data = {
    'order_amount': np.random.randint(10, 1000, size=1000),
    'email_domain': np.random.choice(['gmail.com', 'yahoo.com', 'hotmail.com', 'company.com'], size=1000),
    'past_fraud_history': np.random.choice([0, 1], size=1000),  # 0: No fraud, 1: Fraud in past
    'is_fraudulent': np.random.choice([0, 1], size=1000)  # 0: Legitimate, 1: Fraudulent
}

df = pd.DataFrame(data)

# Save the dataset to a CSV file
df.to_csv('dummy_orders.csv', index=False)
