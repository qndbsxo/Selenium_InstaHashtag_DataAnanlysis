from ssl import SSL_ERROR_SYSCALL
from bs4 import BeautifulSoup
from pandas.core import series
import selenium.webdriver as webdriver
import urllib.parse
from urllib.request import Request, urlopen
from time import sleep
import pandas as pd



search = input('검색어를 입력하세요 : ')
searching = str(search)
search = urllib.parse.quote(string=search)

url = 'https://www.instagram.com/explore/tags/' + str(search) + '/'
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get(url=url) # 검색어 입력한 인스타그램 url 저장
sleep(30) # 로딩 시간을 위한 속도 조절

SCROLL_PAUSE_TIME = 1.2 # 인스타 게시물 스크롤 속도 조절 (1.0 ~ 2.0까지 사양에 맞게 조절)

