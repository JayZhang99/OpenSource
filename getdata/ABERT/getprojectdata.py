import pandas as pd

# 读取数据
Java_list = ['dubbo','flink','kafka']
C_list = ['gimp']
python_list = ['tvm','airflow']


r1 = pd.read_csv("dubbo_del.csv")  # 文件1
r2 = pd.read_csv("flink_del.csv")  # 文件2
r3 = pd.read_csv('kafka_del.csv') # 文件3
frames = [r1, r2, r3]
all_csv = pd.concat(frames)
all_csv.to_csv("Java_data.csv", index=False)
r1 = pd.read_csv("tvm_del.csv")  # 文件1
r2 = pd.read_csv("airflow_del.csv")  # 文件2
frames = [r1, r2]
all_csv = pd.concat(frames)
all_csv.to_csv("Python_data.csv", index=False)
# 数据合并
# all_data_st = pd.merge(r2, r1, how='inner')
# all_data = pd.merge(r3,all_data_st,how = 'inner')
# 空值填充为0
#all_data_st['r1_cnt'].fillna(0, inplace=True)
#all_data_st['r2_cnt'].fillna(0, inplace=True)

# 导出结果数据
#all_data_st.to_csv("labels_repo_hash_msg.csv")