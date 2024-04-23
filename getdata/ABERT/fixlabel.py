import os
import sys
import pandas as pd
dataset_path = r'/Users/jayzhang/PycharmProjects/commitclassifier/'
Project_list = ['gimp','airflow','dubbo','flink','kafka','tvm']

class2label = {
    'Fix': 0,
    'Feature Addition': 1,
    'Docs': 2,
    'Test': 3,
    'Refactoring': 4,
    'Environment': 5,
}

fix = pd.read_csv('fix.csv')
fix = list(fix)
add = pd.read_csv('feature_addition.csv')
add = list(add)
doc = pd.read_csv('doc.csv')
doc = list(doc)
ref = pd.read_csv('refactoring.csv')
ref = list(ref)
testt = pd.read_csv('test.csv')
testt = list(testt)
env = pd.read_csv('environment.csv')
env = list(env)

for proname in Project_list:
    tar = proname + '_labels.csv'
    target = os.path.join(dataset_path, tar)
    resul = proname + '_end.csv'
    result = os.path.join(dataset_path,resul)
    df = pd.read_csv(target)
    msg = list(df['commit_msg'])
    label = list(df['labels'])
    num = len(label)
    for i in range(num):
        commit_msg = msg[i].lower().split(" ")  # to array
        for word in commit_msg:
            for assoc_word in add:
                if assoc_word in word:
                    label[i] = 1
            for assoc_word in fix:
                if assoc_word in word:
                    label[i] = 0
            for assoc_word in doc:
                if assoc_word in word:
                    label[i] = 2
            for assoc_word in ref:
                if assoc_word in word:
                    label[i] = 4
            for assoc_word in testt:
                if assoc_word in word:
                    label[i] = 3
            for assoc_word in env:
                if assoc_word in word:
                    label[i] = 5
            if "merge" in word:
                label[i] = 7
    df = pd.DataFrame({'commit_msg': msg, 'labels': label})
    df.to_csv(result, index=False)
