import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression

# Load Dataset
dataset = pd.read_csv(r'ml_model\train.csv', encoding='latin-1')
dataset = dataset.rename(columns=lambda x: x.strip().lower())

# Preprocess
dataset = dataset[['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked', 'survived']]
dataset['sex'] = dataset['sex'].map({'male': 0, 'female': 1})
dataset['age'] = dataset['age'].fillna(np.mean(dataset['age']))

# One-hot encoding for embarked
embarked_dummies = pd.get_dummies(dataset['embarked'])
dataset = pd.concat([dataset, embarked_dummies], axis=1).drop(['embarked'], axis=1)

# Features and target
X = dataset.drop(['survived'], axis=1)
y = dataset['survived']

# Scale data
sc = MinMaxScaler()
X_scaled = sc.fit_transform(X)

# Train model
log_model = LogisticRegression()
log_model.fit(X_scaled, y)

# Save model and scaler
pickle.dump(log_model, open("ml_model/ml_model.sav", "wb"))
pickle.dump(sc, open("ml_model/scaler.sav", "wb"))

print("Model trained and saved successfully!")
