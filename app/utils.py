from django.conf import settings
import pickle as pk
import sklearn
import pandas as pd


with open(f'{settings.BASE_DIR}/trained_model.sav', 'rb') as f:
    model = pk.load(f)

def get_class(data):

    data = dict([[i, [data[i]]] for i in data])

    df = pd.DataFrame(data)
    df.drop(columns='i', inplace=True)

    return model.predict(pd.DataFrame(df))[0]