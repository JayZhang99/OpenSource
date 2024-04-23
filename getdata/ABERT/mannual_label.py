import os
import sys
import pandas as pd

data_path = 'airflow_data_labels.csv'

def mannual_label():
    df = pd.read_csv(data_path)
    msg = list(df['commit_data'])
    label = list(df['labels'])
    num = len(label)
    class2label = {
        'Fix': 0,
        'Feature Addition': 1,
        'Non Functional': 2,
        'Test': 3,
        'Refactoring': 4,
        'Deprecate': 5,
        'None': 6
    }
    for i in range(num):
        if label[i] == 6:
            print(msg[i])
            print(class2label)
            print(i)
            print(num)
            l = int(input())
            if(l == -1):
                break
            label[i] = l
    df = pd.DataFrame({'commit_data': msg, 'labels': label})
    df.to_csv('airflow_data_labels.csv', index=False)
mannual_label()
