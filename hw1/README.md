# README
## 用什麼套件
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import requests
import json
爬蟲套件
處理資料的套件
處理時間套件
發送請求套件
將字串轉字典

## 流程圖

## 錯誤情況
1. 沒有抓到當天的Close，因為每天的收盤日期都不一樣，導致長度不同
無法用pandas顯示
2. 因為yahoo finance的資料不齊全，所以有些抓到也會導致長度不同無法顯示
3. 沒問題
4. 沒問題
5. 沒問題

## 無法完成的 ETF名稱
因為資料不齊全，所以無法以pandas顯示
ZJPN
PAF

