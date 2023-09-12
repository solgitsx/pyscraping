# [웹 스크레이핑]
# [6장: 232페이지]

from bs4 import BeautifulSoup

# In[ ]:

# get_ipython().run_cell_magic('writefile', 'C:/myPyScraping/data/ch06/HTML_example_my_site.html', '<!doctype html>\n<html>\n  <head>\n    <meta charset="utf-8">\n    <title>사이트 모음</title>\n  </head>\n  <body>\n    <p id="title"><b>자주 가는 사이트 모음</b></p>\n    <p id="contents">이곳은 자주 가는 사이트를 모아둔 곳입니다.</p>\n    <a href="http://www.naver.com" class="portal" id="naver">네이버</a> <br>\n    <a href="https://www.google.com" class="search" id="google">구글</a> <br>\n    <a href="http://www.daum.net" class="portal" id="daum">다음</a> <br>\n    <a href="http://www.nl.go.kr" class="government" id="nl">국립중앙도서관</a>\n  </body>\n</html>\n')


# In[ ]:

f = open('./HTML_example_my_site.html', encoding='utf-8')

html3 = f.read()
f.close()

soup3 = BeautifulSoup(html3, "lxml")


# In[ ]:


soup3.select('a')


# [6장: 233페이지]

# In[ ]:

# 셀렉터 : 클래스(class) 속성을 가진 요소들을 선택
soup3.select('a.portal')

#%%
soup3.select('.portal')


# In[ ]:


soup3.select_one('a').get_text()


# In[ ]:

# 요소 'a'를 모두 찾아서 리스트로 생성
[x.get_text() for x in soup3.select('a')]


# #### 웹 브라우저의 요소 검사

# [6장: 235페이지]

# In[ ]:


soup3.select('a')


# In[ ]:


soup3.select('a.portal')


# [6장: 236페이지]

# In[ ]:

# 요소 'a'에서 id가 'naver'인 모든 요소 선택
soup3.select('a#naver')
soup3.select('#naver')


# In[ ]:

# 요소 'a'에서 id(naver), class(portal)인 모든 요소 선택
soup3.select('a#naver.portal')


# In[ ]:


soup3.select('a.portal#naver')

