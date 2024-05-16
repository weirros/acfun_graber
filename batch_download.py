# -*- coding: utf-8 -*-
"""
Created on Thu May 16 13:50:10 2024
pip install you-get
#需自行下载配置ffmpeg
@author: David
"""

file = './grabed.csv'
from subprocess import run
import pandas as pd

df = pd.read_csv(file)

# print(df)
for row in df:
    
    url = row['urls']

    cmd = f'''you-get {url} '''
    print(cmd)
    run(cmd,shell=True)