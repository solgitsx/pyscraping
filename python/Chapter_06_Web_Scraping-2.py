# [웹 스크레이핑]

# ### 6.1.6 웹 페이지의 소스 분석하고 처리하기
# #### 데이터 찾고 추출하기

# [6장: 222페이지]

# In[ ]:

# pip install beautifulsoup4
    

from bs4 import BeautifulSoup

# 테스트용 html 소스
html = """<html><body><div><span>\
        <a href=http://www.naver.com>naver</a>\
        <a href=https://www.google.com>google</a>\
        <a href=http://www.daum.net/>daum</a>\
        </span></div></body></html>""" 

# BeautifulSoup를 이용해 HTML 소스를 파싱
soup = BeautifulSoup(html, 'lxml') 
soup


# In[ ]:

# HTML의 DOM 구조 형태로 출력
print(soup.prettify())


# [6장: 224페이지]

# In[ ]:


# 첫 번째 만나는 요소(a) : Element
soup.find('a')


# In[ ]:


# text 영역의 값을 추출
soup.find('a').get_text()


# In[ ]:

soup.find('a')['href'] # soup.find('a').get('href') 도 동일
soup.find('a').get('href')

#%%

# 모든 해당 요소를 찾음
soup.find_all('a')

[ x.get_text() for x in soup.find_all('a') ] # ['naver', 'google', 'daum']

#%%

# [문제] 위에 코드를 분해하여 코딩하라.
a_find_all = [] # 빈 리스트
for x in soup.find_all('a'):
    print('x:', x)
    a_find_all.append(x.get_text())

print("a_find_all :", a_find_all)


