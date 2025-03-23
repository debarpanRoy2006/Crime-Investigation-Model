import wandb
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Initialize W&B
wandb.init(project="my_ml_project", name="chicken_model_training")

# Load dataset
data = pd.read_csv("train.csv")
X = data.drop(columns=["target"])  # Replace "target" with the actual column name
y = data["target"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Save scaler
pickle.dump(scaler, open("scaler.sav", "wb"))

# Define model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Log hyperparameters
wandb.config = {
    "n_estimators": 100,
    "random_state": 42,
    "test_size": 0.2
}

# Train model
model.fit(X_train, y_train)

# Evaluate model
accuracy = model.score(X_test, y_test)
wandb.log({"accuracy": accuracy})

# Save model
pickle.dump(model, open("model.sav", "wb"))
wandb.save("model.sav")

print(f"Model training complete. Accuracy: {accuracy}")
