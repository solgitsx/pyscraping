# [웹 스크레이핑]
# [6장: 237페이지]

from bs4 import BeautifulSoup

# ### 6.1.7 웹 사이트 주소에 부가 정보 추가하기

# #### 웹 사이트 주소에 경로 추가하기


# In[ ]:

base_url = "https://api.github.com/"
sub_dir = "events"
url = base_url + sub_dir # https://api.github.com/events
print(url)


# In[ ]:


import requests

base_url = "https://api.github.com/"
sub_dirs = ["events", "user", "emails"]

for sub_dir in sub_dirs:
    url_dir = base_url + sub_dir
    r = requests.get(url_dir)
    print(r.url)


# #### 웹 사이트 주소에 매개변수 추가하기

# [6장: 238페이지]

# In[ ]:


import requests

where_value = 'nexearch' 
sm_value = 'top_hty'
fbm_value = 1
ie_value = 'utf8'
query_value = 'python'

base_url = "https://search.naver.com/search.naver"
parameter = "?where={0}&sm={1}&fbm={2}&ie={3}&query={4}".format(where_value, sm_value, fbm_value, ie_value, query_value)
url_para = base_url + parameter
r = requests.get(url_para) # https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=python

# https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%9D%B4%EC%8B%9C%EC%9B%85

print(r.url)


# [6장: 239페이지]

# In[ ]:


import requests  

where_value = 'nexearch' 
sm_value = 'top_hty'
fbm_value = 1
ie_value = 'utf8'
query_value = 'python'

url = "https://search.naver.com/search.naver"
parameters = {"where":where_value, "sm":sm_value, "fbm":fbm_value, "ie":ie_value, "query":query_value}
r = requests.get(url, params=parameters)
print(r.url)


# ## 6.2 웹 사이트에서 데이터 가져오기

# ### 6.2.1 날씨 정보 가져오기

# #### 웹 사이트 분석해 날씨 정보 가져오기

# [6장: 241페이지]

# In[ ]:


import requests  
from bs4 import BeautifulSoup 

location = "서울시 종로구 청운동"
search_query = location + " 날씨"
search_url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q="
url = search_url + search_query

html_weather = requests.get(url).text
soup_weather = BeautifulSoup(html_weather, "lxml")
print(url)


# [6장: 243페이지]

# In[ ]:


txt_temp = soup_weather.select_one('strong.txt_temp').get_text()
txt_temp


# In[ ]:


txt_weather = soup_weather.select_one('span.txt_weather').get_text()
txt_weather


# In[ ]:


dl_weather_dds = soup_weather.select('dl.dl_weather dd')
dl_weather_dds


# [6장: 244페이지]

# In[ ]:


[wind_speed, humidity, pm10] = [x.get_text() for x in dl_weather_dds]

print(f"현재 풍속: {wind_speed}, 현재 습도: {humidity}, 미세 먼지: {pm10}")


# In[ ]:


import requests  
from bs4 import BeautifulSoup 
import time

def get_weather_daum(location):
    search_query = location + " 날씨"
    search_url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q="
    url = search_url + search_query
    html_weather = requests.get(url).text
    time.sleep(2)    
    soup_weather = BeautifulSoup(html_weather, "lxml")
    
    txt_temp = soup_weather.select_one('strong.txt_temp').get_text()
    txt_weather = soup_weather.select_one('span.txt_weather').get_text()

    dl_weather_dds = soup_weather.select('dl.dl_weather dd')
    [wind_speed, humidity, pm10] = [x.get_text() for x in dl_weather_dds]
    
    return (txt_temp, txt_weather, wind_speed, humidity, pm10)


# In[ ]:


location = "서울시 종로구 청운동" # 날씨를 알고 싶은 지역 
get_weather_daum(location)        # 함수 호출


# [6장: 245페이지]

# In[ ]:


location = "경기도 수원시" # 날씨를 알고 싶은 지역 

(txt_temp, txt_weather, wind_speed, humidity, pm10) = get_weather_daum(location)

print("-------[오늘의 날씨 정보] (Daum) ----------")
print(f"- 설정 지역: {location}")
print(f"- 기온: {txt_temp}")
print(f"- 날씨 정보: {txt_weather} ", )
print(f"- 현재 풍속: {wind_speed}, 현재 습도: {humidity}, 미세 먼지: {pm10}")


# #### 날씨 정보 주기적으로 가져오기

# [6장: 245페이지]

# In[ ]:


import schedule
import time
from datetime import datetime

# 작업을 위한 함수 지정
def job():
    now = datetime.now()
    print("[작업 수행 시각] {:%H:%M:%S}".format(now))
    location = "경기도 수원시" # 날씨를 알고 싶은 지역 

    (txt_temp, txt_weather, wind_speed, humidity, pm10) = get_weather_daum(location)

    print("-------[오늘의 날씨 정보] (Daum) ----------")
    print(f"- 설정 지역: {location}")
    print(f"- 기온: {txt_temp}")
    print(f"- 날씨 정보: {txt_weather} ", )
    print(f"- 현재 풍속: {wind_speed}, 현재 습도: {humidity}, 미세 먼지: {pm10}")

# 코드 테스트를 위해 5초마다 날씨 정보 가져와 출력하기 위한 스케줄 설정
schedule.every(5).seconds.do(job)  # 5초(second)마다 job() 함수 실행

# -- 매일 지정한 시각에 날씨 정보를 가져와 출력하기 위한 스케줄 설정
# schedule.every().day.at("07:00").do(job) # 매일 07시에 job() 함수 실행
# schedule.every().day.at("12:00").do(job) # 매일 12시에 job() 함수 실행
# schedule.every().day.at("18:00").do(job) # 매일 18시에 job() 함수 실행

while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except:
        print("작업 강제 종료")
        schedule.clear()  # 기본 스케줄러 객체를 제거          
        break            # while 문을 빠져 나옴


# ### 6.2.2 주식 정보 가져오기

# #### 주식 현재가 가져오기

# [6장: 248페이지]

# In[ ]:


import requests
from bs4 import BeautifulSoup

base_url = 'https://finance.naver.com/item/main.nhn'
stock_code = "005930"
url = base_url + "?code=" + stock_code

html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')

print(url)


# [6장: 250페이지]

# In[ ]:


soup.select_one('p.no_today')


# In[ ]:


stock_price = soup.select_one('p.no_today span.blind').get_text()
stock_price


# In[ ]:


import requests
from bs4 import BeautifulSoup

def get_current_stock_price(stock_code):
    
    base_url = 'https://finance.naver.com/item/main.nhn'
    url = base_url + "?code=" + stock_code
    
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    
    stock_price = soup.select_one('p.no_today span.blind').get_text()
    
    return stock_price


# [6장: 251페이지]

# In[ ]:


stock_code = "005930"
current_stock_price = get_current_stock_price(stock_code)
current_stock_price


# In[ ]:


company_stock_codes = {"삼성전자": "005930", "현대차":"005380", "NAVER":"035420"}

print("[현재 주식 가격(원)]")
for company, stock_code in company_stock_codes.items():
    current_stock_price = get_current_stock_price(stock_code)
    print(f"{company}: {current_stock_price}")


# #### 주식 종목 코드 가져오기

# [6장: 252페이지]

# In[ ]:


import pandas as pd

# 한국 거래소(KRX)에서 전체 상장법인 목록 가져오기
base_url = "http://kind.krx.co.kr/corpgeneral/corpList.do"
method = "download"
url = "{0}?method={1}".format(base_url, method)

df = pd.read_html(url, header=0)[0]

with pd.option_context('display.max_columns',4): # 최대 4개까지 열이 표시하도록 설정
    pd.set_option("show_dimensions", False)      # 행과 열 개수 출력 안 하기
    display(df.head())


# In[ ]:


df['종목코드']= df['종목코드'].apply(lambda x: f"{x:06d}")

with pd.option_context('display.max_columns',4): # 최대 4개까지 열이 표시하도록 설정
    pd.set_option("show_dimensions", False)      # 행과 열 개수 출력 안 하기
    display(df.head())


# In[ ]:


df = df[['회사명','종목코드']]
df.head()


# [6장: 254페이지]

# In[ ]:


import pandas as pd

#----------------------------------------------------
# 한국 주식의 종목 이름과 종목 코드를 가져오는 함수
#----------------------------------------------------
def get_stock_info(maket_type=None):
    # 한국거래소(KRX)에서 전체 상장법인 목록 가져오기
    base_url =  "http://kind.krx.co.kr/corpgeneral/corpList.do"
    method = "download"
    if maket_type == 'kospi':
        marketType = "stockMkt"  # 주식 종목이 코스피인 경우
    elif maket_type == 'kosdaq':
        marketType = "kosdaqMkt" # 주식 종목이 코스닥인 경우
    elif maket_type == None:
        marketType = ""
    url = "{0}?method={1}&marketType={2}".format(base_url, method, marketType)

    df = pd.read_html(url, header=0)[0]
    
    # 종목코드 열을 6자리 숫자로 표시된 문자열로 변환
    df['종목코드']= df['종목코드'].apply(lambda x: f"{x:06d}") 
    
    # 회사명과 종목코드 열 데이터만 남김
    df = df[['회사명','종목코드']]
    
    return df


# In[ ]:


df_kospi = get_stock_info('kospi')
df_kospi.head()


# [6장: 255페이지]

# In[ ]:


df_kosdaq = get_stock_info('kosdaq')
df_kosdaq.head()


# In[ ]:


#--------------------------------------------------
# 회사 이름을 입력하면 종목 코드를 가져오는 함수
#--------------------------------------------------
def get_stock_code(company_name, maket_type=None):
    df = get_stock_info(maket_type)
    code = df[df['회사명']==company_name]['종목코드'].values
    
    if(code.size !=0):
        code = code[0]    
        return code
    else:
        print(f"[Error]입력한 [{company_name}]에 대한 종목 코드가 없습니다.")


# In[ ]:


get_stock_code('삼성전자', 'kospi') # 삼성전자 주식 종목 코드 가져오기, 코스피(kospi) 지정


# [6장: 256페이지]

# In[ ]:


get_stock_code('삼성전자') # 삼성전자 주식 종목 코드 가져오기, 주식 종류는 지정 안 함


# In[ ]:


get_stock_code('현대차')


# In[ ]:


get_stock_code('현대자동차')


# In[ ]:


company_names = ["삼성전자", "현대자동차", "NAVER"]

print("[현재 주식 가격(원)]")
for company_name in company_names:
    stock_code = get_stock_code(company_name)
    current_stock_price = get_current_stock_price(stock_code)
    print(f"{company_name}: {current_stock_price}")


# [6장: 257페이지]

# In[ ]:


get_stock_code('CJ 바이오사이언스', 'kosdaq') # 주식 종목 코드 가져오기, 코스닥(kosdaq) 지정


# In[ ]:


get_stock_code('CJ 바이오사이언스') # 주식 종목 코드 가져오기, 주식 종류는 지정 안 함


# ### 6.2.3 환율 정보 가져오기

# #### 현재의 환율 정보 가져오기

# [6장: 259페이지]

# In[ ]:


import pandas as pd

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8'

# url에서 표 데이터를 추출해 DataFrame 데이터의 리스트로 반환
dfs = pd.read_html(url)
dfs


# [6장: 260페이지]

# In[ ]:


len(dfs)


# In[ ]:


dfs[0]


# In[ ]:


exchange_rate_df = dfs[0].replace({'전일대비상승': '▲', 
                                   '전일대비하락': '▼'}, regex=True)
exchange_rate_df


# [6장: 262페이지]

# In[ ]:


import pandas as pd

# 네이버 금융의 환율 정보 웹 사이트 주소
url = 'https://finance.naver.com/marketindex/exchangeList.nhn' 

# 웹 사이트의 표 데이터에서 두 번째 줄을 DataFrame 데이터의 columns로 선택
dfs = pd.read_html(url, header=1) 

dfs[0].head() # 전체 데이터 중 앞의 일부분만 표시


# #### 과거의 환율 정보 가져오기

# [6장: 264페이지]

# In[ ]:


import pandas as pd

base_url = "https://finance.naver.com/marketindex/exchangeDailyQuote.nhn"
currency_code = "FX_USDKRW" # 통화 코드
page_num = 1

url = f"{base_url}?marketindexCd={currency_code}&page={page_num}"
dfs = pd.read_html(url, header=1)

# 행과 열의 최대 표시 개수를 임시로 설정
with pd.option_context('display.max_rows',4, 'display.max_columns',6): 
    pd.set_option("show_dimensions", False) # 행과 열 개수 정보 숨기기
    display(dfs[0])


# [6장: 265페이지]

# In[ ]:


import pandas as pd
import time

# 날짜별 환율 데이터를 반환하는 함수
# - 입력 인수: currency_code(통화코드), last_page_num(페이지 수)
# - 반환: 환율 데이터
def get_exchange_rate_data(currency_code, last_page_num):
    base_url = "https://finance.naver.com/marketindex/exchangeDailyQuote.nhn"

    df = pd.DataFrame()

    for page_num in range(1, last_page_num+1):
        url = f"{base_url}?marketindexCd={currency_code}&page={page_num}"
        dfs = pd.read_html(url, header=1)

        if dfs[0].empty: # 통화 코드가 잘못 지정됐거나 마지막 페이지의 경우 for 문을 빠져나오기 위한 코드
            if (page_num==1):
                print(f"통화 코드({currency_code})가 잘못 지정됐습니다.")
            else:
                print(f"{page_num}가 마지막 페이지입니다.")
            break

        df = pd.concat([df, dfs[0]], ignore_index=True) # page별로 가져온 DataFrame 데이터 연결
        time.sleep(0.1) # 0.1초간 멈춤
        
    return df


# [6장: 266페이지]

# In[ ]:


df_usd = get_exchange_rate_data('FX_USDKRW', 2)

# 행과 열의 최대 표시 개수를 임시로 설정
with pd.option_context('display.max_rows',4, 'display.max_columns',6):
    pd.set_option("show_dimensions", False) # 행과 열 개수 정보 숨기기
    display(df_usd)


# [6장: 267페이지]

# In[ ]:


df_eur = get_exchange_rate_data('FX_EURKRW', 1)

# 행과 열의 최대 표시 개수를 임시로 설정
with pd.option_context('display.max_rows',4, 'display.max_columns',6):
    pd.set_option("show_dimensions", False) # 행과 열 개수 정보 숨기기
    display(df_eur.head())


# ### 6.2.4 부동산 정보 가져오기

# [6장: 269페이지]

# In[ ]:


import pandas as pd

base_url = "https://land.naver.com/news/trendReport.naver"
page_num = 1

url = f"{base_url}?page={page_num}"
dfs = pd.read_html(url)

df = dfs[0] # 리스트의 첫 번째 항목에 동향 보고서 제목 데이터가 있음

# 행과 열의 최대 표시 개수를 임시로 설정
with pd.option_context('display.max_rows',4, 'display.max_columns',6): 
    pd.set_option("show_dimensions", False) # 행과 열 개수 정보 숨기기
    display(df)


# [6장: 270페이지]

# In[ ]:


import pandas as pd

# 원본 DataFrame의 제목 열에 있는 문자열을 분리해 
# 전국, 서울, 수도권의 매매가 변화율 열이 있는 DataFrame 반환하는 함수
def split_title_to_rates(df_org):
    df_new = df_org.copy()

    df_temp = df_new['제목'].str.replace('%', '') # 제목 문자열에서 % 제거
    df_temp = df_temp.str.replace('보합', '0')    # 제목 문자열에서 보합을 0으로 바꿈
    df_temp = df_temp.str.replace('보합세', '0')  # 제목 문자열에서 보합세를 0으로 바꿈
    
    regions = ['전국', '서울', '수도권']    
    for region in regions:
        df_temp = df_temp.str.replace(region, '') # 문자열에서 전국, 서울, 수도권 제거

    df_temp = df_temp.str.split(']', expand=True) # ]를 기준으로 열 분리
    df_temp = df_temp[1].str.split(',', expand=True) # ,를 기준으로 열 분리
    
    df_temp = df_temp.astype(float)
    
    df_new[regions] = df_temp # 전국, 서울, 수도권 순서대로 DataFrame 데이터에 할당

    return df_new[['등록일'] + regions + ['번호']] # DataFrame에서 필요한 열만 반환


# [6장: 271페이지]

# In[ ]:


df_rate = split_title_to_rates(df) # split_title_to_rates() 함수 호출
df_rate.head()                     # 앞의 일부만 출력


# In[ ]:


import pandas as pd

base_url = "https://land.naver.com/news/trendReport.naver"

df_rates = pd.DataFrame() # 전체 데이터가 담길 DataFrame 데이터
last_page_num = 8 # 가져올 데이터의 마지막 페이지 

for page_num in range(1, last_page_num+1):

    url = f"{base_url}?page={page_num}"
    dfs = pd.read_html(url)

    df_page = dfs[0] # 리스트의 첫 번째 항목에 동향 보고서 제목 데이터가 있음
    df_rate = split_title_to_rates(df_page)
    
    # 세로 방향으로 연결 (기존 index를 무시)
    df_rates = pd.concat([df_rates, df_rate], ignore_index=True) 

# 최신 데이터와 과거 데이터의 순서를 바꿈. index도 초기화함  
df_rates = df_rates[::-1].reset_index(drop=True)
df_rates.head() # 앞의 일부만 출력

# 행과 열의 최대 표시 개수를 임시로 설정
with pd.option_context('display.max_rows',4, 'display.max_columns',6): 
    pd.set_option("show_dimensions", False) # 행과 열 개수 정보 숨기기
    display(df_rates)


# [6장: 273페이지]

# In[ ]:


import matplotlib as mpl

mpl.rcParams['font.family'] = 'Malgun Gothic' # '맑은 고딕'으로 폰트 설정 
mpl.rcParams['axes.unicode_minus'] = False # 마이너스(-) 폰트 깨짐 방지


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

df_rates.tail(40).plot(x='등록일', y=['전국', '서울', '수도권'], 
                       figsize=(10, 8), subplots=True, layout=(3,1),
                       style = '-o', grid=True) # 그래프 그리기
plt.show()


# ### 6.2.5 웹 페이지에서 이미지 가져오기

# [6장: 275페이지]

# In[ ]:


import requests  

image_url = 'https://www.python.org/static/img/python-logo.png' # 이미지 링크(주소)
r = requests.get(image_url) # 이미지 주소의 HTTP 응답 객체
r


# [6장: 276페이지]

# In[ ]:


file_name = image_url.split("/")[-1]
file_name


# In[ ]:


from pathlib import Path

download_folder = 'C:/myPyScraping/data/ch06/download' 
image_dir_path = Path(download_folder)

if not image_dir_path.exists():
    image_dir_path.mkdir(parents=True, exist_ok=True)
    
print("생성한 폴더:", download_folder)


# [6장: 277페이지]

# In[ ]:


image_path = image_dir_path/file_name
image_path


# [6장: 278페이지]

# In[ ]:


r = requests.get(image_url) # 이미지 주소의 HTTP 응답 객체
image_data = r.content # 응답 객체(r)을 이용해 받은 이미지 데이터

with open(image_path, 'wb') as f:
    f.write(image_data)


# In[ ]:


import requests 
from pathlib import Path

# Unsplash의 사진 이미지 주소
image_url = "https://images.unsplash.com/photo-1645956734658-8b6e62e7d35a"
  
file_name = image_url.split("/")[-1] + ".jpg" # 파일 이름 생성(확장자 추가)
download_folder = 'C:/myPyScraping/data/ch06/download' # 다운로드 폴더 지정

# 지정한 다운로드 폴더를 생성하지 않았으면 생성
image_dir_path = Path(download_folder)
if not image_dir_path.exists():
    image_dir_path.mkdir(parents=True, exist_ok=True)
    
image_path = image_dir_path/file_name # 전체 경로(폴더 + 파일명)

r = requests.get(image_url, stream=True)
if r.status_code == 200:  
    with open(image_path, 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
    print("- 이미지를 다운로드했습니다")
else:
    print("- 지정한 이미지 링크의 응답이 없습니다.")


# ## 6.3 정리
