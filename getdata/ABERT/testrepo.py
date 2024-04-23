import pandas as pd

# 读取数据
r1 = pd.read_csv("repo_hash_msg_labels.csv")  # 文件1

print(r1.iloc[1: 10])

