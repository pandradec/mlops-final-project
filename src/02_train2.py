# Importing the libraries, usando MLFLOW
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import mlflow


mlflow.set_tracking_uri("http://localhost:5000")

dataset = pd.read_csv('data/training/hiring_training.csv')

x = dataset.iloc[:, :3]
y = dataset.iloc[:, -1]

from sklearn.linear_model import LinearRegression

def train_model(data_file_path, model_file_path):
    regressor = LinearRegression()
    #Fitting model with trainig data
    regressor.fit(x, y)

    # Saving model to disk
    #pickle.dump(regressor, open(model_file_path,'wb'))
    #return regressor


if __name__ == "__main__":
    print("Model trained and saved successfully")
    mlflow.set_experiment("hiring_model_experiment")
    mlflow.sklearn.autolog()
    train_model('data/training/hiring_training.csv', 'models/model.pkl')