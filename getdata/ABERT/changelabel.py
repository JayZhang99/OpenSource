import pandas as pd

# 读取数据
data = pd.read_csv("labels_repo_hash_msg.csv")  # 文件1

num2class = {
    0:"Fix",
    1:"Feature Addition",
    2:"Non Functional",
    3:"Test",
    4:"Refactoring",
    5:"Deprecate",
    6:"None"
}
msg = data['commit_msg']
labels = list(data['labels'])
url = data['commit_url']
hsh = data['commit_hash']
for i in range(len(labels)):
    labels[i]=num2class[labels[i]]
data = pd.DataFrame({'commit_msg': msg, 'labels': labels,'commit_url':url,'commit_hash':hsh})
data.to_csv("msg_labels_url_hash.csv")