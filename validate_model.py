# validate_model.py
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

def validate_model():
    print("Validating model...")
    data = pd.read_csv('prepared_data.csv')
    X = data.drop('target', axis=1)  # Example: Features
    y = data['target']               # Example: Target
    model = joblib.load('model.pkl')
    predictions = model.predict(X)
    accuracy = accuracy_score(y, predictions)
    print(f"Validation Accuracy: {accuracy:.2f}")

if __name__ == "__main__":
    validate_model()
