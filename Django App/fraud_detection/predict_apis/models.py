import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the dummy dataset
data = pd.read_csv('fraud_data.csv')

# Encode categorical features
label_encoder = LabelEncoder()
data['Customer Email Domain'] = label_encoder.fit_transform(data['Customer Email Domain'])

# Features and target
X = data[['Order Amount', 'Customer Email Domain', 'Past Fraud History']]
y = data['Fraud Probability (%)']

# Train a RandomForestClassifier
model = RandomForestClassifier()
model.fit(X, y)

# Save the model and label encoder
joblib.dump(model, 'fraud_model.pkl')
joblib.dump(label_encoder, 'label_encoder.pkl')