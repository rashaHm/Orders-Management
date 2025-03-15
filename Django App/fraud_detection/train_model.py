import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the dataset
df = pd.read_csv('dummy_orders.csv')

# Encode categorical variables
le = LabelEncoder()
df['email_domain'] = le.fit_transform(df['email_domain'])

# Split the data into features and target
X = df[['order_amount', 'email_domain', 'past_fraud_history']]
y = df['is_fraudulent']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'fraud_model.pkl')
