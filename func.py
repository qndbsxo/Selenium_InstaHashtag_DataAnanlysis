from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re


# 검색어 조건에 따른 url 생성
def insta_searching(word):
    url = "https://www.instagram.com/explore/tags/" + str(word)
    return url


# 열린 펭지에서 첫 번째 게시물 클릭 + sleep 메소드 통하여 시차 두기
def select_first(driver):
    first = driver.find_elements_by_css_selector("div._9AhH0")[0]
    first.click()
    time.sleep(3)


# 본문 내용, 작성일자, 좋아요 수, 위치 정보, 해시태그 가져오기
def get_content(driver):
    html = driver.page_source
    soup = BeautifulSoup(markup=html, features="lxml")
    # 본문 내용
    try:
        content = soup.select(selector="div.C4VMK > span")[0].text
    except:
        content = " "
    # 해시태그
    tags = re.findall(pattern=r"#[^\s#,\\]+", string=content)
    # 작성일자
    date = soup.select(selector="time._1o9PC.Nzb55")[0]["datetime"][:10]
    # 좋아요
    try:
        like = soup.select(selector="div.Nm9Fw > button")[0].text[4:-1]
    except:
        like = 0
    # 위치
    try:
        place = soup.select(selector="div.M30cS")[0].text
    except:
        place = ""
    data = [content, date, like, place, tags]
    return data


# 첫 번째 게시물 클릭 후 다음 게시물 클릭
def move_next(driver):
    right = driver.find_element_by_css_selector("a.coreSpriteRightPaginationArrow")
    right.click()
    time.sleep(3)
