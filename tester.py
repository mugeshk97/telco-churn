import requests
import json

payload = {'MonthlyCharges':19.45,
'Net_Fiber optic': 0.00,
'Electronic check': 0.00,
'Month-to-month': 0.00,
'DeviceProtection_No': 0.00,
'OnlineBackup_No': 0.00,
'OnlineSecurity_No': 0.00,
'TechSupport_No': 0.00,
'ten1-18': 0.00,
}
    
data = requests.post('https://murmuring-stream-94529.herokuapp.com/', json= payload)
print(data.json())


