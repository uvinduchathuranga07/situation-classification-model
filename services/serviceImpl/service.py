
import os

import joblib
import warnings
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder

warnings.filterwarnings("ignore")

MODEL_DIR = os.path.abspath("models")
original_labels = ["High", "Low", "Medium"]  # Replace with your actual class labels

# Initialize a new LabelEncoder
le = LabelEncoder()

# Fit the LabelEncoder to your original class labels
le.fit(original_labels)
loaded_model = joblib.load(os.path.join(MODEL_DIR, 'randomforest_model.pkl'))
# original_labels = ["High", "Low", "Medium"]
# le = LabelEncoder()
le.fit(original_labels)

def predict_coral(new_data):
    data_array = np.array([list(new_data.values())])
    predicted_label = loaded_model.predict(data_array)
    predicted_situation = le.inverse_transform(predicted_label)
    print(f'Predicted Situation: {predicted_situation[0]}')

    return predicted_situation[0]

