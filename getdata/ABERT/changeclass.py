import om
import sys
import pandas as pd

data_path = 'airflow_data_labels.csv'
df = pd.read_csv(data_path)
msg = list(df['commit_data'])
label = list(df['labels'])
num = len(label)
for i in range(num):
    if label[i] == 7:
        label[i] = 6
df = pd.DataFrame({'commit_data': msg, 'labels': label})
df.to_csv('airflow_data_labels.csv', index=False)