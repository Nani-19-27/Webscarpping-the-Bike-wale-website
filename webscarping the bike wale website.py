#!/usr/bin/env python
# coding: utf-8

# # WEB SCARPING THE BIKE WALE WEBSITE
# 
# 
# > About the Project- This is a small part of work in the data analysis web scarping. By the Webscarping we can extract the data set from HTML to required formate. 
# Here this conversion we can understand the current market prices of the bikes rescpect brands. and we can draw conclusion by proper approach.
# 
# > Below I have built a one time function for each brand to extract the data into data frame quickly.we can understand to scrolling down.Like Hero, Honda, Royal Enfield etc.

# In[1]:


import requests
from bs4 import BeautifulSoup
#_______________________________

import pandas as pd
import warnings
warnings.filterwarnings('ignore')
#________________________________

from collections import OrderedDict 


# In[2]:


def page_url(url_link):
    req_ = requests.get(url_link)                                                                #step 1
    page = BeautifulSoup(req_.content,'lxml')
#________________________________________________________________________________________
    bike_name = page.find_all('h3',class_='bikeTitle margin-bottom10')
    name_list = [p.text for p in bike_name]                                                      #step 2
#_________________________________________________________________________________________
    specf = page.find_all('div',class_='text-xt-light-grey font14 margin-bottom15')
    specifications = [p.text.strip() for p in specf]                                             #step 3
#________________________________________________________________________________________
    prices = page.find_all('div',class_='text-bold')
    prices_ = [p.text for p in prices] #1
    prices__= OrderedDict.fromkeys(prices_) #2                                                   #step 4
    prices___ = list(prices__.keys()) #3        
    prices___.remove('AD')                                      
#_________________________________________________________________________________________
    df = pd.DataFrame({'Names':name_list,'Specifications':specifications,'Prices':prices___})
    df['Brand'] = df['Names'].str.split().str.get(0)
    df['Engine'] = df.Specifications.str.split().str.get(0)
    df['Mileage'] = df.Specifications.str.split().str.get(2)
    df['Power'] = df.Specifications.str.split().str.get(4)                                        #step 5
    df['Weight'] = df.Specifications.str.split().str.get(6)    
    df['Prices'] = df.Prices.str.split().str.get(1)
    df.drop(columns=['Specifications'],axis=1,inplace=True)
#___________________________________________________________________________________________
    return df


# Step 4 Explanation - 
# 
# 1. If we see the Thrid of coding in step 3 " OrderedDist.fromkeys() " i used for removeing "AD" string duplicate(repetation). and keep the value with its original position. Note - if we use " [*set()] it removes the duplicates but the values will be shuffled
# 
# 2. After it will be convered into dist type so that i used " .key() " and conversted again into list type 4th line coding
# 
# 3. and by " .remove() " method totally elimate the string value in the list 

# In[3]:


hero = page_url("https://www.bikewale.com/hero-bikes/")
ktm = page_url("https://www.bikewale.com/ktm-bikes/")
yamaha = page_url("https://www.bikewale.com/yamaha-bikes/")
honda=page_url('https://www.bikewale.com/honda-bikes/')
re = page_url('https://www.bikewale.com/royalenfield-bikes/')
tvs = page_url('https://www.bikewale.com/tvs-bikes/')
suzuki = page_url('https://www.bikewale.com/suzuki-bikes/')


# In[4]:


Df = pd.concat((hero,ktm,yamaha,honda,re,tvs,suzuki),axis=0,ignore_index=True)


# In[5]:


from IPython.display import display
with pd.option_context('display.max_rows',200):
    display(Df)

