import os
import sys
import pandas as pd

data_path = 'msg_labels.csv'

df = pd.read_csv(data_path)

msg = df['commit_msg']

msg = pd.DataFrame({'commit msg':msg})

msg.to_csv('onlymsg.csv',index = False )
