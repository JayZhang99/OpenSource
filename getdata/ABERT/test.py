from pydriller import Repository
import os
import pandas as pd
project_path = r'/Users/jayzhang/tvm'
dataset_path = r'/Users/jayzhang/PycharmProjects/commitclassifier/train.csv'
project_name = os.path.split(project_path)[1]
T = Repository(project_path).traverse_commits()
T = list(T)
A = [1, 2, 3, 4]
df = pd.DataFrame({'A': A})
df.to_csv('A.csv',mode='a',index=False)
#df1 = pd.read_csv('A.csv')
#with open('A.csv','ab') as f:
   # f.write(open('B.csv','rb').read())
#frames = [df1,df]
#all_csv = pd.concat(frames)
#all_csv.to_csv("A.csv",index=False)
print(type(T[0].msg))