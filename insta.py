from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import time
from func import *

# 오류 해결 라라
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# driver = webdriver.Chrome(options=options)




# 크롤링 시작
""" 
driver.get(url)을 통해 검색 페이지 접속하고, 
target 변수에 크롤링할 게시글의 수를 바인딩
"""

# 크롬 부라우저 열기
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)

driver.get(url='https://www.instagram.com')
time.sleep(3)

# 인스타그램 로그인을 위한 계정 정보
email = 'qndbsxo@gmail.com'
input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]
input_id.clear()
input_id.send_keys(email)

password = "wasdas5257!"
input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]
input_pw.clear()
input_pw.send_keys(password)
input_pw.submit()

time.sleep(5)

# 게시물을 조회할 검색 키워드 입력 요청
word = input('검색어를 입력하세요 :')
word = str(word)
url = insta_searching(word)

# 검색 결과 페이지 열기
driver.get(url)
time.sleep(10)

# 첫 번째 게시물 클릭
select_first(driver)

# 본격적으로 데이터 수집 시작
results = []

# 수집할 게시물의 수
target = 5
for i in range(target):

    try:
        data = get_content(driver)  # 데이터가 추가가 안되는 부분
        results.append(data)
        move_next(driver)
    except:
        time.sleep(2)
        move_next(driver)

print(results[:2])
# -----------------------여기까지 확인 --------------------


# 결과가 데이터프레임으로 저장
import pandas as pd

result_df = pd.DataFrame(data=results)
result_df.columns = ['content', 'date', 'like', 'place', 'tags']
result_df.to_excel('koreanfood.xlsx')


