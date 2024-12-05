# data_preparation.py
import pandas as pd
import numpy as np

def prepare_data():
    print("Preparing data...")
    # Example: Load dataset
    data = pd.read_csv('data.csv')
    # Example: Basic data cleaning
    data = data.dropna()
    print(f"Prepared {len(data)} rows of data.")
    data.to_csv('prepared_data.csv', index=False)

if __name__ == "__main__":
    prepare_data()
