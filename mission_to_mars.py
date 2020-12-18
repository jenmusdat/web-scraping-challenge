#!/usr/bin/env python
# coding: utf-8

# In[17]:


from splinter import Browser
from bs4 import BeautifulSoup
import time


# In[2]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[4]:


html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')


# In[5]:


news = soup.find_all("div", class_="content_title")[1]
news_title = news.get_text()
news_title


# In[6]:


news_paragraph = soup.find_all("div", class_="article_teaser_body")[0]
news_p = news_paragraph.get_text()
news_p


# In[7]:


url="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)
browser.links.find_by_partial_text("FULL IMAGE").click()


# In[8]:


browser.links.find_by_partial_text("more info").click()


# In[9]:


html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
image = soup.find_all("figure", class_="lede")[0]
image_href=image.find_all("a", href = True)[0]
image_href["href"]


# In[10]:


featured_image_url = 'https://www.jpl.nasa.gov'+image_href["href"]
featured_image_url


# In[11]:


import pandas as pd


# In[12]:


nasa_df=pd.read_html("https://space-facts.com/mars/")[0]
nasa_df


# In[27]:


hemisphere_image_urls = []
title = []
#hemisphere_image_titles = []
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)

#find the first image
browser.links.find_by_partial_text("Hemisphere Enhanced")[0].click()
html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
image = soup.find_all("div", class_="downloads")[0]
image_href=image.find_all("a", href = True)[0]
image_href["href"]

hemisphere = {}
hemisphere["img_url"]=image_href["href"]
hemisphere_image_urls.append(hemisphere)
hemisphere['title'] = browser.find_by_css("h2.title").text
browser.back()
time.sleep(1)

#find the second image
browser.links.find_by_partial_text("Hemisphere Enhanced")[1].click()
html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
image = soup.find_all("div", class_="downloads")[0]
image_href=image.find_all("a", href = True)[0]
image_href["href"]

hemisphere = {}
hemisphere["img_url"]=image_href["href"]
hemisphere_image_urls.append(hemisphere)
hemisphere['title'] = browser.find_by_css("h2.title").text
browser.back()
time.sleep(1)

#find the third image
browser.links.find_by_partial_text("Hemisphere Enhanced")[2].click()
html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
image = soup.find_all("div", class_="downloads")[0]
image_href=image.find_all("a", href = True)[0]
image_href["href"]

hemisphere = {}
hemisphere["img_url"]=image_href["href"]
hemisphere_image_urls.append(hemisphere)
hemisphere['title'] = browser.find_by_css("h2.title").text
browser.back()
time.sleep(1)

#find the fourth image
browser.links.find_by_partial_text("Hemisphere Enhanced")[3].click()
html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
image = soup.find_all("div", class_="downloads")[0]
image_href=image.find_all("a", href = True)[0]
image_href["href"]

hemisphere = {}
hemisphere["img_url"]=image_href["href"]
hemisphere_image_urls.append(hemisphere)
hemisphere['title'] = browser.find_by_css("h2.title").text
browser.back()
time.sleep(1)
      
print(hemisphere_image_urls)
#print(title)


# In[28]:


#quit the browser when finished
browser.quit()


# In[ ]:




