import pandas as pd

# 读取数据
r1 = pd.read_csv("url_hash_msg.csv")  # 文件1
r2 = pd.read_csv("commit_msg_labels.csv")  # 文件2

# 数据合并
all_data_st = pd.merge(r2, r1, how='inner')

# 空值填充为0
#all_data_st['r1_cnt'].fillna(0, inplace=True)
#all_data_st['r2_cnt'].fillna(0, inplace=True)

# 导出结果数据
all_data_st.to_csv("labels_repo_hash_msg.csv")