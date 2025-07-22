import pandas as pd
import numpy as np
import requests
import io
import os

def setup_data():
    """
    Downloads, cleans, and saves the UCI Adult Census dataset.
    """
    # Create a data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    print("Downloading dataset...")
    # URL for the dataset
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
    
    # Download the content
    try:
        res = requests.get(url, timeout=30).content
    except requests.RequestException as e:
        print(f"Error downloading data: {e}")
        return

    # Define column names
    column_names = [
        'age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
        'occupation', 'relationship', 'race', 'gender', 'capital-gain', 'capital-loss',
        'hours-per-week', 'native-country', 'income'
    ]
    
    # Read the data, replacing '?' with NaN
    df = pd.read_csv(io.StringIO(res.decode('utf-8')), header=None, names=column_names, sep=',\s*', engine='python', na_values='?')
    
    # Drop rows with any missing values
    df.dropna(inplace=True)
    
    # Make the target variable binary
    df['income'] = df['income'].apply(lambda x: 1 if x == '>50K' else 0)

    # Save the cleaned data
    df.to_csv('data/adult.csv', index=False)
    print("✅ Cleaned data saved successfully to data/adult.csv")

if __name__ == '__main__':
    setup_data()