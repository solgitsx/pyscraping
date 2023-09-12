# [웹 스크레이핑]
# [6장: 230페이지]
# CSS(Cascading Style Sheets) : 스타일 시트
# selector : 선택자
#   - element : tag
#   - id : #
#   - class : .

from bs4 import BeautifulSoup

# 테스트용 HTML 코드
html2 = """
<html>
 <head>
  <title>작품과 작가 모음</title>
 </head>
 <body>
  <h1>책 정보</h1>
  <h2>대하소설</h2>
  <p id="book_title">토지</p>
  <p id="author">박경리</p>
  
  <p id="book_title">태백산맥</p>
  <p id="author">조정래</p>

  <h2>역사소설</h2>
  <p id="book_title">감옥으로부터의 사색</p>
  <p id="author">신영복</p>
  </body>
</html>
""" 

soup2 = BeautifulSoup(html2, "lxml")

# In[ ]:

# 셀렉터 : body의 하위 요소의 첫 번째 만나는 'h1'    
soup2.select_one('body h1') # body 내의 h1 태그를 갖는 최초의 요소 찾기


# In[ ]:

# 셀렉터 : body의 하위 요소의 모든 'h2' 요소
h2 = soup2.select('body h2') # body 내의 h2 태그를 갖는 모든 요소 찾기 


# In[ ]:

# body의 하위 요소에서 처음 요소 'p' 요소
soup2.select_one('body p')


# In[ ]:

# body의 하위 요소에서 모든 요소 'p'
soup2.select('body p')


# In[ ]:

# 모든 요소 'p'를 찾음
soup2.select('p')


# [6장: 231페이지]

# In[ ]:

# [주의] id는 고유해야 함, 요소에 하나만 지정되어야 한다.
# 요소 'p'에서 id가 'book_title'인 요소
soup2.select('p#book_title')


# In[ ]:


soup2.select('p#author')

