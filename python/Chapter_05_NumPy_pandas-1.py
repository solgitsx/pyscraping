#!/usr/bin/env python
# coding: utf-8

# # 5장 데이터 처리와 분석을 위한 라이브러리

# ## 5.1 배열 데이터 연산에 효율적인 넘파이(NumPy)

# ### 5.1.1 배열 데이터 생성

# #### 리스트 데이터로부터 배열을 생성

# [5장: 146페이지]

# In[ ]:


import numpy as np

list_data = [0, 1, 2, 3, 4, 5.0]
a1 = np.array(list_data)
print(type(a1), a1) # <class 'numpy.ndarray'> [0. 1. 2. 3. 4. 5.]



# [5장: 147페이지]

# In[ ]:


type(a1)


# In[ ]:

# 2차원 배열 : list -> ndarray
a2 = np.array([
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]])
a2


# #### 범위와 간격을 지정해 배열을 생성

# [5장: 148페이지]

# In[ ]:

# 10개의 배열을 생성
np.arange(0, 10, 1) # start, stop, step 모두 지정

#%%
# 0부터 10 - 1까지 2씩 증가 : 0,2,4,6,8
np.arange(0, 10, 2) # start, stop, step 모두 지정


# In[ ]:


np.arange(0, 10) # start, stop만 지정(step=1)


# In[ ]:


np.arange(10) # stop만 지정(start=0. step=1)


# In[ ]:

# 실수 지정
np.arange(0, 5, 0.5) # start, stop, step 모두 지정


# #### 범위와 개수를 지정해 배열을 생성

# [5장: 149페이지]

# In[ ]:

# 1부터 10까지의 수에서 10개의 숫자를 생성    
np.linspace(1, 10, 10) # start, stop, num 지정

#%%
# 1부터 10까지의 수에서 20개의 숫자를 생성    
np.linspace(1, 10, 20) # start, stop, num 지정

# In[ ]:

print("np.pi:", np.pi) # 3.141592653589793

np.linspace(0, np.pi, 20)

