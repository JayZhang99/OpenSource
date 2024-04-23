import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

#Project_list = ['gimp','airflow','dubbo','flink','kafka','tvm']
Lang_list = ['Java','Python']
for proname in Lang_list:
    resul = proname + '_data.csv'
    df = pd.read_csv(resul)
    data = list(df['commit_msg'])
    label3 = list(df['labels'])
    val_csv = proname +'_val.csv'
    train_csv = proname+'_train.csv'
    test_csv = proname +'_test.csv'
    val_txt = proname +'_val.txt'
    train_txt = proname +'_train.txt'
    test_txt = proname +'_test.txt'
    X_train, X_test, Y_train, Y_test = train_test_split(data, label3, test_size=0.2)
    X_test, X_val, Y_test, Y_val = train_test_split(X_test, Y_test, test_size = 0.5)
    df = pd.DataFrame({'commit_msg':X_val,'labels': Y_val})
    df.to_csv(val_csv,index=False,)
    df = pd.DataFrame({'commit_msg':X_train,'labels': Y_train})
    df.to_csv(train_csv,index=False)
    df = pd.DataFrame({'commit_msg':X_test,'labels': Y_test})
    df.to_csv(test_csv,index=False)
    csv_list = [train_csv,test_csv,val_csv]
    txt_list = [train_txt,test_txt,val_txt]
    for i in range(3):
        csvPath = csv_list[i]
        txtPath = txt_list[i]
        data = pd.read_csv(csvPath)
        msg = data['commit_msg']
        label = list(data['labels'].fillna('None'))
        with open(txtPath, 'a+', encoding='utf-8') as f:
            for line in data.values:
                f.write((str(line[0]).replace('\n', '').replace('\r', '').replace('\t', '') + '\t'+ str(line[1]).replace('\n', '').replace('\r', '').replace('\t', '') + '\n'))
