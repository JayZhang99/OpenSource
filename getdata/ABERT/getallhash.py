import pandas as pd
import os
#遍历获得文件
def FilesPath(path):
    '''
    path: 目录文件夹地址
    返回值:列表,pdf文件全路径
    '''
    filePaths = [] # 存储目录下的所有文件名，含路径
    for root,dirs,files in os.walk(path):
        for file in files:
            filePaths.append(os.path.join(root,file))
    return filePaths
#获得所以文件路径
Total_file = FilesPath('hash')
data = pd.DataFrame()
for file_path in (Total_file[1:10]):
    df = pd.read_csv(file_path, encoding='utf8')
    data = pd.concat([data, df])
Total_data_save_path='url_hash_msg.csv'
# 重新设置索引 从0开始
data.reset_index(drop=True, inplace=True)
# 将合并的data存储
data.to_csv(Total_data_save_path, index=False, encoding='utf8')