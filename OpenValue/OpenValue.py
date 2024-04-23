import pandas as pd

# 读取数值数据和权重数据
scores = pd.read_csv('scores.csv')
commitclass = 'Fix'
Wclass={'Fix':25,'Feature add':5,'Test':1,'Ref':1,'Docs':0.2,'Env':0.04}

Cscore =  scores.iloc[:,0].sum()
OpenValue = Wclass[commitclass]*Cscore

