from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import joblib

# Load the trained model and label encoder
model = joblib.load('fraud_model.pkl')
label_encoder = joblib.load('label_encoder.pkl')

class FraudDetectionView(APIView):
    def post(self, request):
        # Extract input data
        order_amount = request.data.get('order_amount')
        email_domain = request.data.get('email_domain')
        past_fraud_history = request.data.get('past_fraud_history')

        # Encode email domain
        email_domain_encoded = label_encoder.transform([email_domain])[0]

        # Prepare input for prediction
        input_data = [[order_amount, email_domain_encoded, past_fraud_history]]
   

        # Predict fraud probability
        fraud_probability = model.predict_proba(input_data)[0][1]  # Probability of fraud
        fraud_score = int(max(model.predict_proba(input_data)[0]) * 100)  # Convert to percentage

        return Response({'fraud_score': model.predict(input_data)}, status=status.HTTP_200_OK)