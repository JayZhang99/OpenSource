import pandas as pd

data = pd.read_csv('msg_labels_end.csv')

msg = data['commit_data']

labels = data['labels']

num = len(labels)
cnt = [0,0,0,0,0,0,0]
for i in range(num):
    cnt[labels[i]] = 1+cnt[labels[i]]
for i in range(7):
    print(i,cnt[i])