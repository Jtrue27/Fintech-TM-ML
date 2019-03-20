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
將文字轉json物件

## 流程圖

## 錯誤情況
1. 沒有抓到當天的Close，因為每天的收盤日期都不一樣，導致長度不同
無法用pandas顯示
2. 因為yahoo finance的資料不齊全，所以有些抓到也會導致長度不同無法顯示
3. 如果未來網站改prams 可能會撈不到資料
4. 如果改網站資料request 加驗證機制 可能會擋我們發送的request
5. 我們目前沒有加延遲發送request 的機制 如果server 負荷過大，可能會導致response error

## 無法完成的 ETF名稱
因為資料不齊全，所以無法以pandas顯示
ZJPN
PAF

