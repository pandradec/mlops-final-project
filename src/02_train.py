# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle



#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import LinearRegression

def train_model(data_file_path, model_file_path):
    dataset = pd.read_csv(data_file_path)
    x = dataset.iloc[:, :3]
    y = dataset.iloc[:, -1]
    regressor = LinearRegression()
    #Fitting model with trainig data
    regressor.fit(x, y)

    # Saving model to disk
    pickle.dump(regressor, open(model_file_path,'wb'))
    return regressor

'''
# Loading model to compare the results
model = pickle.load(open('models/model.pkl','rb'))
print(model.predict([[2, 9, 6]]))
'''

if __name__ == "__main__":
    print("Model trained and saved successfully")
    train_model('data/training/hiring_training.csv', 'models/model.pkl')