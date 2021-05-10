import mysql.connector
import pandas as pd
import sys

dataset = sys.argv[1]

db = mysql.connector.connect(host="192.168.1.2",                
                            user="mugesh", 
                            database = "telcom", 
                            passwd="Mugesh97.",
                            auth_plugin = 'mysql_native_password')


cursor = db.cursor()


q2 = f"SHOW COLUMNS FROM {dataset}"

cursor.execute(q2)
column_names = []
for x in cursor:
    column_names.append(x[0])


q3 = f"SELECT * FROM {dataset}"

cursor.execute(q3)
data = []
for x in cursor:
    data.append(x)

df = pd.DataFrame.from_records(
    data, columns=column_names)

df.to_csv(f'/home/mugesh/Projects/telco-churn/data/raw/{dataset}.csv', index = False)