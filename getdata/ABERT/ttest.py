from pydriller import Repository
import os
import pandas as pd
project_path = r'/Users/jayzhang/'
dataset_path = r'/Users/jayzhang/PycharmProjects/commitclassifier/'
Project_list = ['gimp','airflow','dubbo','flink','kafka','tvm']
# project_name = os.path.split(project_path)[1]
# T = Repository(project_path).traverse_commits()
# T = list(T)
class commit(object):
    def getsinglemsg(self):
        for proname in Project_list:
            propath = os.path.join(project_path,proname)
            Rep = Repository(propath).traverse_commits()
            Rep = list(Rep)
            tar = proname + '.csv'
            target = os.path.join(dataset_path,tar)
            commit_msg_list = []
            for i in Rep:
                commit_msg_list.append(i.msg.replace('\n', '').replace('\r', '').replace('\t', ''))
            df = pd.DataFrame({'commit_msg': commit_msg_list})
            df.to_csv(target,index=False)
    def getmsg(self):
        commit_msg_list = []
        for i in T:
            commit_msg_list.append(i.msg.replace('\n', '').replace('\r', '').replace('\t', ''))
        df = pd.DataFrame({'commit_msg': commit_msg_list})
        df1 = pd.read_csv('commit_msg.csv')
        frames = [df1, df]
        all_csv = pd.concat(frames)
        all_csv.to_csv("commit_msg.csv", index=False)
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
    com.getsinglemsg()
start()
