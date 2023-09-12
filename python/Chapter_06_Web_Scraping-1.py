#!/usr/bin/env python
# coding: utf-8

# # 6장 웹 스크레이핑
# ## 6.1 웹 스크레이핑을 위한 기본 지식
# ### 6.1.1 웹 스크레이핑의 과정
# ### 6.1.2 웹 스크레이핑 시 주의 사항
# #### 주요 주의 사항
# #### 웹 사이트 이용 규약
# ### 6.1.3 웹 데이터의 요청과 응답 과정
# ### 6.1.4 웹 페이지 언어(HTML) 구조

# [6장: 215페이지]

# In[ ]:


# get_ipython().run_cell_magic('writefile', 'C:\\myPyScraping\\data\\ch06\\HTML_example.html', '<!doctype html>\n<html>\n <head>\n  <meta charset="utf-8">\n  <title>이것은 HTML 예제</title>\n </head>\n <body>\n  <h1>출간된 책 정보</h1>\n  <p id="book_title">이해가 쏙쏙 되는 파이썬</p>\n  <p id="author">홍길동</p>\n  <p id="publisher">위키북스 출판사</p>\n  <p id="year">2018</p>\n </body>\n</html>\n')


# [6장: 216페이지]

# In[ ]:


# get_ipython().run_cell_magic('writefile', 'C:/myPyScraping/data/ch06/HTML_example2.html', '<!doctype html>\n<html>\n <head>\n  <meta charset="utf-8">\n  <title>이것은 HTML 예제</title>\n </head>\n <body>\n  <h1>출간된 책 정보</h1>\n  <p>이해가 쏙쏙 되는 파이썬</p>\n  <p>홍길동</p>\n  <p>위키북스 출판사</p>\n  <p>2018</p>\n  </body>\n</html>\n')


# ### 6.1.5 웹 페이지의 소스 가져오기

# #### 웹 브라우저로 웹 페이지 소스 보기

# ####  requests 라이브러리 활용

# ####  GET 메서드로 웹 사이트의 소스 가져오기

# [6장: 220페이지]

# In[ ]:


import requests

# return : Response 객체
r = requests.get("https://www.google.co.kr")
r


# In[ ]:


r.status_code # 성공: HTTP 200


# [6장: 221페이지]

# In[ ]:


r.text[0:100]


# In[ ]:


r.headers


# In[ ]:


import requests

html = requests.get("https://www.google.co.kr").text
html[0:100]


#%%

