# [웹 스크레이핑]
# P-225

from bs4 import BeautifulSoup

# 테스트용 HTML 코드
html2 = """
<html>
 <head>
  <title>작품과 작가 모음</title>
 </head>
 <body>
  <h1>책 정보</h1>
  <p id="book_title">토지</p>
  <p id="author">박경리</p>
  
  <p id="book_title">태백산맥</p>
  <p id="author">조정래</p>

  <p id="book_title">감옥으로부터의 사색</p>
  <p id="author">신영복</p>
  </body>
</html>
""" 

soup2 = BeautifulSoup(html2, "lxml")


# [6장: 226페이지]

# In[ ]:

# 요소를 속성처럼 접근해서 Element 객체를 사용
soup2.title

#%%
soup2.title.text # '작품과 작가 모음'

# In[ ]:

# body의 요소를 접근해서 사용
soup2.body


# [6장: 227페이지]

# In[ ]:


soup2.body.h1 # <h1>책 정보</h1>


# In[ ]:

# 전체 문서에서 처음 만나는 요소
soup2.p # <p id="book_title">토지</p>
soup2.p.text # '토지'
soup2.body.p.text # '토지'

# In[ ]:

soup2.find_all('p')


# [6장: 228페이지]

# In[ ]:

# 찾을 속성을 dict로 지정
# 처음 만나는 요소('p')에서 
# 속성('id')의 값이 'book_title'인 것을 찾음
soup2.find('p', {"id":"book_title"})


# In[ ]:


soup2.find('p', {"id":"author"}) # <p id="author">박경리</p>


# In[ ]:


soup2.find_all('p', {"id":"book_title"})


# In[ ]:


soup2.find_all('p', {"id":"author"})


# In[ ]:


from bs4 import BeautifulSoup

soup2 = BeautifulSoup(html2, "lxml")

book_titles = soup2.find_all('p', {"id":"book_title"})
authors = soup2.find_all('p', {"id":"author"})

for book_title, author in zip(book_titles, authors):
    print(book_title.get_text() + '/' + author.get_text())

books = []
for book_title, author in zip(book_titles, authors):
    books.append((book_title.text, author.text))
    
print(books)    

#%%

books2 = [(book[0].text, book[1].text) for book in zip(book_titles, authors)]
print(books2)

#%%

