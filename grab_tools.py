# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:06:49 2024


acfun_爬虫_by_主播
@author: David
"""

#主播首页地址


url = 'https://www.acfun.cn/u/14539629'

#主播页数
pages = 13



from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options# 手机模式

import pandas as pd


options = Options()
options.add_argument('--headless')


driver = webdriver.Chrome(options=options)
driver.set_window_size(1280,960)
driver.get(url)
time.sleep(2)


def doSth(df):

    
    uxpath = '//*[@id="ac-space-video-list"]'

    
    subxpath = '//*[@id="ac-space-video-list"]/a[*]'

    
    lar = driver.find_element(By.XPATH,uxpath)


    sub = lar.find_elements(By.XPATH,subxpath)
    

    for i in sub:
        
        ts = i.text.split('\n')
        #print(i.text.split('\n'))
        hf = i.get_attribute('href')
        ts.append(hf)
        
        
        print(ts)
        
        #df = pd.concat([df,ts])
        df.loc[len(df)]=ts
    
    return df







def next_page():
    

    
    driver.find_element(By.XPATH,"//a[contains(text(),'下一页')]").click()

    
# next_page()


def main():
    
    df = pd.DataFrame(columns=['names','rates','dates','urls'],dtype=str)
    
    for row in range(pages):
        print('Now grabing pages:',row+1)    
        df = doSth(df)
        next_page()
        sleep(1.5)

    print(df)
    df.to_csv('grabed.csv',index=False, encoding="utf-8-sig")

main()