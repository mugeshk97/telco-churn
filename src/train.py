import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score ,confusion_matrix
from utils import load_config, save_model, write_json
from sklearn.model_selection import train_test_split



cols =['Net_Fiber optic',
    'Electronic check',
    'Month-to-month',
    'DeviceProtection_No',
    'OnlineBackup_No',
    'OnlineSecurity_No',
    'TechSupport_No',
    'ten1-18',
    'MonthlyCharges',
    'Churn']

train = pd.read_csv('/home/mugesh/Projects/telco-churn/data/feature/train_feature.csv', usecols= cols)

X = train.drop('Churn', axis= 1)
y = train.Churn

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)

scaler = StandardScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

def get_label(pred, threshold):
    y_pred = []
    for i in pred:
        if i[0] < threshold:
            y_hat = 1
        else:
            y_hat = 0
        y_pred.append(y_hat)
    return y_pred


config = load_config()
train_config = config['hyp']

model = LogisticRegression(max_iter= train_config['max_iter'], class_weight= train_config['class_weight'])
model.fit(x_train, y_train)

pred = model.predict_proba(x_test)
y_pred = get_label(pred, threshold= train_config['threshold'])

accuracy = accuracy_score(y_test, y_pred)
report = {'val_acc': accuracy}

write_json('/home/mugesh/Projects/telco-churn/report/report.json', report)
save_model('/home/mugesh/Projects/telco-churn/model/model.pkl', model)
