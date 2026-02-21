import pandas as pd

## crear funciones
def prepare_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # ejemplo de data preparation steps:
    # handle missing values
    df.fillna(df.mean(), inplace=True)
    
    # Encode categorical variables if necessary
    df = pd.get_dummies(df, drop_first=True)
    
    return df

if __name__ == "__main__":
    # example usage
    training_data_set = prepare_data('data/raw/hiring.csv')
    training_data_set.to_csv('data/training/hiring_training.csv', index=False)
    