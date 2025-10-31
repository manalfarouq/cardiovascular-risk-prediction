
from sklearn.model_selection import train_test_split



def encoder_cible(data, cible):
    data[cible] = data[cible].map(lambda x: 0 if x == "negative" else 1)
    return data


def split_data(data, cible):
    X = data.drop(columns=[cible]) 
    y = data[cible]
   
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) 

    return X_train, X_test, y_train, y_test
