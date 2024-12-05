# train_model.py
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import joblib

def train_model():
    print("Training model...")
    data = pd.read_csv('prepared_data.csv')
    X = data.drop('target', axis=1)  # Example: Features
    y = data['target']               # Example: Target
    model = RandomForestClassifier()
    model.fit(X, y)
    joblib.dump(model, 'model.pkl')
    print("Model trained and saved as model.pkl")

if __name__ == "__main__":
    train_model()
