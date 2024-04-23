from pydriller import Repository
import os
import pandas as pd
import random
project_path = r'/Users/jayzhang/opensource/data/dubbo'
dataset_path = r'/Users/jayzhang/opensource/data/OpenValue/dubbo.csv'
repourl = 'https://github.com/apache/tvm/commit/'
project_name = os.path.split(project_path)[1]
T = Repository(project_path).traverse_commits()
T = list(T)
class commit(object):
    def getsha(self):
        commit_hash_list = []
        commit_score=[]
        repo_size = len(T)
        random_numbers=[random.randint(0,repo_size) for _ in range(100)]
        for i in random_numbers:
            commit_hash_list.append(T[i].hash)
            commit_score.append(random.randint(1,5))
        df = pd.DataFrame({'commit_hash': commit_hash_list, 'score': commit_score})
        df.to_csv(dataset_path,index=False)
def start():
    com=commit()
    com.getsha()
start()
