import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

def audit_model(protected_attribute):
    """
    Trains a model and calculates accuracy and disparate impact.
    
    Args:
        protected_attribute (str): The column to audit for bias (e.g., 'gender', 'race').

    Returns:
        dict: A dictionary containing the audit results.
    """
    df = pd.read_csv('data/adult.csv')
    
    # Define target and features
    target = 'income'
    features = df.drop(columns=[target]).columns
    
    # One-hot encode categorical features
    X = pd.get_dummies(df[features], drop_first=True)
    y = df[target]
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # Scale numerical features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train a simple model
    model = LogisticRegression(random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # --- CALCULATE ACCURACY ---
    y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    
    # --- CALCULATE DISPARATE IMPACT ---
    # Get predictions for the entire dataset to audit fairness
    full_dataset_scaled = scaler.transform(X)
    df['prediction'] = model.predict(full_dataset_scaled)
    
    # Identify privileged vs unprivileged groups
    groups = df[protected_attribute].unique()
    privileged_group_name = groups[0]
    unprivileged_group_name = groups[1]

    privileged_group = df[df[protected_attribute] == privileged_group_name]
    unprivileged_group = df[df[protected_attribute] == unprivileged_group_name]

    # Calculate rate of positive outcomes (prediction == 1)
    privileged_positive_rate = privileged_group['prediction'].mean()
    unprivileged_positive_rate = unprivileged_group['prediction'].mean()

    # Calculate disparate impact, handling division by zero
    disparate_impact = 0.0
    if privileged_positive_rate > 0:
        disparate_impact = unprivileged_positive_rate / privileged_positive_rate

    return {
        "accuracy": f"{accuracy:.2%}",
        "protected_attribute": protected_attribute.replace('-', ' ').title(),
        "privileged_group": privileged_group_name,
        "unprivileged_group": unprivileged_group_name,
        "privileged_rate": f"{privileged_positive_rate:.2%}",
        "unprivileged_rate": f"{unprivileged_positive_rate:.2%}",
        "disparate_impact": f"{disparate_impact:.2f}",
        "is_fair": disparate_impact >= 0.8
    }