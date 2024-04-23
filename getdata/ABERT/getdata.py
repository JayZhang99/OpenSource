from pydriller import Repository
import os
import pandas as pd
project_path = r'/Users/jayzhang/kafka'
dataset_path = r'/Users/jayzhang/PycharmProjects/commitclassifier/airflow.csv'
repourl = 'https://github.com/apache/tvm/commit/'
project_name = os.path.split(project_path)[1]
T = Repository(project_path).traverse_commits()
T = list(T)
class commit(object):
    def getchange(self):
        commit_msg_list = []
        commit_labels_list = []
        for i in T:
            commit_msg_list.append(i.msg.replace('\n', '').replace('\r', '').replace('\t', ''))
            if i.modified_files:
                for file in i.modified_files:
                    commit_labels_list.append(file.change_type)
                    break
            else:
                commit_labels_list.append('None')
        df = pd.DataFrame({'commit_msg': commit_msg_list, 'labels': commit_labels_list})
        df.to_csv("data/kafka_msg_labels.csv", index=False)
    def getrepo(self):
        commit_msg_list = []
        commit_repo_list =[]
        for i in T:
            commit_msg_list.append(i.msg.replace('\n', '').replace('\r', '').replace('\t', ''))
            commit_repo_list.append('kafka')
        df = pd.DataFrame({'commit_msg': commit_msg_list, 'commit_repo': commit_repo_list})
        df.to_csv("kafka_repo.csv", index=False)
    def gethash(self):
        commit_msg_list = []
        commit_hash_list = []
        commit_url = []
        for i in T:
            commit_msg_list.append(i.msg.replace('\n', '').replace('\r', '').replace('\t', ''))
            commit_hash_list.append(i.hash)
            commit_url.append(repourl+i.hash)
        df = pd.DataFrame({'commit_url':commit_url,'commit_hash':commit_hash_list,'commit_msg': commit_msg_list})
        df.to_csv("tvm_hash&msg&url.csv", index=False)
    def getmsg(self):
        commit_msg_list = []
        for i in T:
            commit_msg_list.append(i.msg.replace('\n', '').replace('\r', '').replace('\t', ''))
        df = pd.DataFrame({'commit_msg': commit_msg_list})
        df.to_csv("tvm.csv",index=False)
        '''df1 = pd.read_csv('commit_msg.csv')
        frames = [df1, df]
        all_csv = pd.concat(frames)
        all_csv.to_csv("commit_msg.csv", index=False)'''
    def newhunk(self):
        commit_data_list = []
        for i in T:
            hunk = i.msg.replace('\n', '').replace('\r', '').replace('\t', '')
            for m in i.modified_files:
                hunk_list = m.diff.strip()
                hunk = hunk + hunk_list.replace('\n', '').replace('\r', '').replace('\t', '')
                if (len(hunk) > 512):
                    hunk = hunk[:512]
                    break
            commit_data_list.append(hunk)
        df = pd.DataFrame({'commit_data': commit_data_list})
        df.to_csv('commit_data_head.csv',index=False)
    def gethunk(self):
        commit_data_list = []
        for i in T:
            hunk = i.msg.replace('\n', '').replace('\r', '').replace('\t', '')
            for m in i.modified_files:
                hunk_list = m.diff.strip()
                hunk = hunk + hunk_list.replace('\n', '').replace('\r', '').replace('\t', '')
            commit_hunk_list.append(hunk)
        df = pd.DataFrame({'commit_data': commit_hunk_list})
        df1 = pd.read_csv('commit_data.csv')
        frames = [df1, df]
        all_csv = pd.concat(frames)
        all_csv.to_csv("commit_data.csv", index=False)
    def newdata(self):
        commit_msg_list = []
        commit_hunk_list = []
        for i in T:
            hunk = ""
            #for m in i.modified_files:
               # hunk_list = m.diff
              #  hunk = hunk + hunk_list.replace('\n', '').replace('\r', '')
            commit_msg_list.append(i.msg.replace('\n', '').replace('\r', '').replace('\t', ''))
           # commit_hunk_list.append(hunk)
        df = pd.DataFrame({'commit_msg': commit_msg_list})
        df.to_csv("commit_msg.csv", index=False)
        #df = pd.DataFrame({'commit_msg': commit_msg_list, 'commit_data': commit_hunk_list})
        #df.to_csv("tvm_commit_data.csv", index=False)

    def csv2txt(self):
        data = pd.read_csv(dataset_path)
        with open('test.txt', 'a+') as f:  # 现在jupyter新建一个txt空文档
            for line in data.values:
                f.write((str(line[0]) + '\t' + str(line[1]) + '\n'))

    def delblankline(self, infile, outfile):
        """ Delete blanklines of infile """
        infp = open(infile, "r")
        outfp = open(outfile, "w")
        lines = infp.readlines()
        for li in lines:
            if li.split():
                outfp.writelines(li)
        infp.close()
        outfp.close()

def start():
    com=commit()
    com.getchange()
start()
