#def scrape():
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_info():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)


    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')


    news = soup.find_all("div", class_="content_title")[1]
    news_title = news.get_text()
    news_title


    news_paragraph = soup.find_all("div", class_="article_teaser_body")[0]
    news_p = news_paragraph.get_text()
    news_p


    url="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    browser.links.find_by_partial_text("FULL IMAGE").click()


    browser.links.find_by_partial_text("more info").click()


    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    image = soup.find_all("figure", class_="lede")[0]
    image_href=image.find_all("a", href = True)[0]
    image_href["href"]

    featured_image_url = 'https://www.jpl.nasa.gov'+image_href["href"]
    featured_image_url

nasa_df=pd.read_html("https://space-facts.com/mars/")[0]
nasa_df = nasa_df.rename(columns={nasa_df.columns[0]: "Description", nasa_df.columns[1]: "Mars"}).set_index("Description")
nasa_df 


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


    #quit the browser when finished
    browser.quit()

    data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image": featured_image_url,
        "facts": nasa_df,
        "hemispheres": hemisphere_image_urls
    }
    return data

