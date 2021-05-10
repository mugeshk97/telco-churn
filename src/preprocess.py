import pandas as pd
from sklearn.preprocessing import LabelEncoder
import sys

dataset = sys.argv[1]


def clean_data(data):
    idx = data[data.TotalCharges == ' '].index
    data = data.drop(idx)
    return data
def change_data(data):
    data.TotalCharges = pd.to_numeric(data.TotalCharges)
    data.MonthlyCharges = pd.to_numeric(data.MonthlyCharges)
    return data

def dummies(data):
    internet = pd.get_dummies(data.InternetService, prefix= 'Net', prefix_sep='_')
    payment = pd.get_dummies(data.PaymentMethod)
    contract = pd.get_dummies(data.Contract)

    data = data.drop(['InternetService','PaymentMethod', 'Contract'], axis=1)
    data = pd.concat([data, internet, payment, contract], axis=1)

    a = pd.get_dummies(data.DeviceProtection, prefix= 'DeviceProtection', prefix_sep='_')
    b = pd.get_dummies(data.OnlineBackup, prefix= 'OnlineBackup', prefix_sep='_')
    c = pd.get_dummies(data.OnlineSecurity, prefix= 'OnlineSecurity', prefix_sep='_')
    d  =pd.get_dummies(data.TechSupport, prefix= 'TechSupport', prefix_sep='_')

    data = data.drop(['DeviceProtection', 'OnlineBackup', 'OnlineSecurity', 'TechSupport'], axis=1)
    data = pd.concat([data, a, b ,c, d], axis=1)
    return data

encoder = LabelEncoder()

def encoding(data):
    for col in data:
        if data[col].dtype == object:
            data[col] = encoder.fit_transform(data[col])
    return data

def bining(data):
    tensure_cat= pd.cut(data['tenure'], bins=4, labels=["ten1-18", "ten19-36", "ten37-54", "ten55-72"])
    tensure_cat.value_counts()

    tensure_cat = pd.get_dummies(tensure_cat)

    data = pd.concat([data, tensure_cat], axis =1)

    data = data.drop('tenure', axis= 1)
    return data

data = pd.read_csv(f'/home/mugesh/Projects/telco-churn/data/raw/{dataset}.csv')
data = data.drop('id', axis =1)
data = clean_data(data)
data = change_data(data)
data = dummies(data)
data = encoding(data)
data = bining(data)
print(data.shape)

data.to_csv(f'/home/mugesh/Projects/telco-churn/data/feature/{dataset}_feature.csv', index= False)


