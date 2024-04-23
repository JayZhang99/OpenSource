import os
import sys
import pandas as pd
dataset_path = r'/Users/jayzhang/PycharmProjects/commitclassifier/'
Project_list = ['gimp','airflow','dubbo','flink','kafka','tvm']
for proname in Project_list:
    resul = proname + '_end.csv'
    result = os.path.join(dataset_path, resul)
    df = pd.read_csv(result)
    df = df[~df['labels'].isin([6])]
    df = df[~df['labels'].isin([7])]
    tar = proname + '_del.csv'
    df.to_csv(tar,index=False)