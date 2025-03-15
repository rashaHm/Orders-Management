from django.urls import path
from .views import FraudDetectionView

urlpatterns = [
    path('detect-fraud/', FraudDetectionView.as_view(), name='detect-fraud'),
]