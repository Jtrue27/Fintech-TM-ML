#!/usr/bin/env python
# coding: utf-8

# #### Observe that we can get news of a day with the link format:
# https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/ccd=3PzzzV/search#result

# In[467]:


import sys
import pickle
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# In[575]:


def get_paper_link(paper,tr_len):
    paper_link=''
    for tr_index in range(1,tr_len):
        link_node=paper.select('#format0_disparea > tbody > tr:nth-of-type('+str(tr_index)+')') # 每列
        row=link_node[0].find_all("th", class_="std1")
        if '本論文永久網址1:' in row[0].string:
                row1=paper[0].select("#fe_text1")
                paper_link=row1[0].get('value')
                break
    #     link_node=paper.select_one('#fe_text1')
    #     paper_link=link_node.get('value')
    return paper_link

def get_chinese_title(paper):
    link_node=paper.select_one('#format0_disparea > tbody > tr:nth-of-type(4) > td')
    chinese_title=link_node.string
    return chinese_title

def get_english_title(paper):
    link_node=paper.select_one('#format0_disparea > tbody > tr:nth-of-type(5) > td')
    english_title=link_node.string
    return english_title

def get_paper_year(paper):
    link_node=paper.select_one('#format0_disparea > tbody > tr:nth-of-type(13) > td')
    paper_year=link_node.string
    return paper_year

def get_chinese_keyword(paper):
    link_node=paper.select('#format0_disparea > tbody > tr:nth-of-type(16) > td ')
    keywords=""
    for ele in link_node:
        keywords=keywords+ele.get_text()
    return keywords

def get_english_keyword(paper):
    link_node=paper.select('#format0_disparea > tbody > tr:nth-of-type(17) > td')
    keywords=""
    for ele in link_node:
        keywords=keywords+ele.get_text()
    return keywords

def get_paper_abstract(browser,paper):
    browser.find_element_by_xpath('//*[@id="gs32_levelrecord"]/ul/li[2]/a').click()
    link_node=paper.select_one('#format0_disparea > tbody > tr > td.stdncl2 > div')
    abstract=link_node.get_text()
    abstract=abstract.strip()
    abstract=abstract.replace('               ','').replace('\n','')
    return abstract

def get_paper_info(browser,paper): # link_node以解析過 與link不同
    chinese_title=get_chinese_title(paper)
    english_title=get_english_title(paper)
    chinese_keyword=get_chinese_keyword(paper)
    english_keyword=get_english_keyword(paper)
    paper_year=get_paper_year(paper)
    link=get_paper_link(paper)
    abstract=get_paper_abstract(browser,paper)
    
    info = {'chinese_title' : chinese_title,
            'english_title': english_title,
            'chinese_keyword':chinese_keyword,
            'english_keyword':english_keyword,
            'paper_year':paper_year,
            'link' : link,
            'abstract': abstract}
    return info


# In[590]:


browser = webdriver.Chrome('./chromedriver')
browser.get('https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/ccd=9P1K1H/webmge?mode=basic')
element=browser.find_element_by_id("ysearchinput0")
element.send_keys("機器學習", Keys.ARROW_DOWN)
browser.find_element_by_name("gs32search").click()
# 變化
paper_page=browser.find_element_by_class_name("slink")
paper_page.click()# 點1
data=list()
for i in range(0,20):
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    link_node=soup.select('#format0_disparea > tbody')
    tr_len=len(link_node[0])
    url=''
    chinese_title=''
    english_title=''
    year=''
    chinese_keyword=''
    english_keyword=''
    for tr_index in range(1,tr_len):
        link_node=soup.select('#format0_disparea > tbody > tr:nth-of-type('+str(tr_index)+')') # 每列
        row=link_node[0].find_all("th", class_="std1")
        if '本論文永久網址:' in row[0].string:
            row1=link_node[0].select("#fe_text1")
            link=row1[0].get('value')
            #print(url)
        elif row[0].string=='論文名稱:':
            back=link_node[0].select("td.std2")
            chinese_title=back[0].get_text()
            #print(chinese_title)
        elif row[0].string=='論文名稱(外文):':
            back=link_node[0].select("td.std2")
            english_title=back[0].get_text()
            #print(english_title)
        elif row[0].string=='論文出版年:':
            back=link_node[0].select("td.std2")
            year=back[0].get_text()
            #print(year)
        elif row[0].string=='中文關鍵詞:':
            back=link_node[0].select("td.std2")
            chinese_keyword=back[0].get_text()
            #print(chinese_keyword)
        elif row[0].string=='外文關鍵詞:':
            back=link_node[0].select("td.std2")
            english_keyword=back[0].get_text()
            #print(english_keyword)
    abstract=get_paper_abstract(browser,soup)
    info = {'chinese_title' : chinese_title,
            'english_title': english_title,
            'chinese_keyword':chinese_keyword,
            'english_keyword':english_keyword,
            'paper_year':year,
            'link' : link,
            'abstract':abstract
           }
    data.append(info)
    print("paper-"+str(i+1)+" finish!")
    next_paper=browser.find_element_by_css_selector('#bodyid > form:nth-child(16) > div > table > tbody > tr:nth-child(1) > td.etds_mainct > table > tbody > tr:nth-child(6) > td > div.cont_l2 > table > tbody > tr:nth-child(2) > td > div > table > tbody > tr > td:nth-child(1) > table > tbody > tr > td:nth-child(4) > input[type="image"]')
    next_paper.click()
browser.close()


# In[592]:


import pandas as pd
pd.DataFrame(data)[['chinese_title', 'english_title', 'chinese_keyword', 'english_keyword', 'paper_year','link','abstract']].head(19)


# In[571]:


# 主要爬蟲程式
def get_all_paper(from_paper_num=0,end_paper_num=10,keyword="機器學習",url="https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/ccd=9P1K1H/webmge?mode=basic"):
    browser = webdriver.Chrome('./chromedriver')
    browser.get(url)
    element=browser.find_element_by_id("ysearchinput0")
    element.send_keys(keyword, Keys.ARROW_DOWN)
    browser.find_element_by_id("gs32search").click()
    paper_page=browser.find_element_by_class_name("slink")# 選一篇進去
    paper_page.click()
    index=1
    data=list()
    for paper_number in range(from_paper_num,end_paper_num):# by each page crawler
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        data.append(get_paper_info(browser,soup))
        print("paper-"+str(paper_number+1)+" finish!")
        #browser.find_element_by_name("gonext").click()
        next_paper=browser.find_element_by_css_selector('#bodyid > form:nth-child(16) > div > table > tbody > tr:nth-child(1) > td.etds_mainct > table > tbody > tr:nth-child(6) > td > div.cont_l2 > table > tbody > tr:nth-child(2) > td > div > table > tbody > tr > td:nth-child(1) > table > tbody > tr > td:nth-child(4) > input[type="image"]')
        next_paper.click()
    browser.close()


# In[ ]:





# In[572]:


get_all_paper()


# In[ ]:


browser = webdriver.Chrome('./chromedriver')
browser.get('https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/ccd=9P1K1H/webmge?mode=basic')
element=browser.find_element_by_id("ysearchinput0")
element.send_keys("機器學習", Keys.ARROW_DOWN)
browser.find_element_by_name("gs32search").click()
# 變化
paper_page=browser.find_element_by_class_name("slink")
paper_page.click()# 點1
data=list()
for i in range(0,2):
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    link_node=soup.select('#format0_disparea > tbody')
    tr_len=len(link_node[0])
#     for tr_index in range(1,tr_len):
#         link_node=soup.select('#format0_disparea > tbody > tr:nth-of-type('+str(tr_index)+')') # 每列
        #row=link_node[0].find_all("th", class_="std1")
    print(get_paper_link(soup,tr_len))
        
        
#         if '本論文永久網址1:' in row[0].string:
#             row1=link_node[0].select("#fe_text1")
#             print(row1[0].get('value'))
#         else:
#             print('')
#         if row[0].string=='論文名稱:':
#             back=link_node[0].select("td.std2")
#             paper_chinese_title=back[0].get_text()
#             print(paper_chinese_title)
#         elif row[0].string=='論文名稱(外文):':
#             back=link_node[0].select("td.std2")
#             print(back[0].get_text())
#         elif row[0].string=='論文出版年:':
#             back=link_node[0].select("td.std2")
#             print(back[0].get_text())
#         elif row[0].string=='中文關鍵詞:':
#             back=link_node[0].select("td.std2")
#             print(back[0].get_text())
#         elif row[0].string=='外文關鍵詞:':
#             back=link_node[0].select("td.std2")
#             print(back[0].get_text())
    print("paper-"+str(i+1)+" finish!")
    next_paper=browser.find_element_by_css_selector('#bodyid > form:nth-child(16) > div > table > tbody > tr:nth-child(1) > td.etds_mainct > table > tbody > tr:nth-child(6) > td > div.cont_l2 > table > tbody > tr:nth-child(2) > td > div > table > tbody > tr > td:nth-child(1) > table > tbody > tr > td:nth-child(4) > input[type="image"]')
    next_paper.click()
browser.close()


# In[466]:


import pandas as pd
pd.DataFrame(data)[['chinese_title', 'english_title', 'chinese_keyword', 'english_keyword', 'paper_year','link','abstract']].head(10)


# In[441]:


data[4]


# In[ ]:


#format0_disparea > tbody

