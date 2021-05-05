# Importing the necessarcy dependencies 
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import urllib.request
import requests
from webdriver_manager.chrome import ChromeDriverManager

# first step initiate browser
def init_browser():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser

def scrape():
    # Initiate scrape for articel title and paragraph 
    browser = init_browser()

    # Visit https://mars.nasa.gov/news/
    url= "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    
    # Set time sleep for it not to crash 
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    #News title
    news_title = soup.find('div', class_= "content_title").text

    #News paragraph
    news_p = soup.find('div', class_ = "article_teaser_body").text
    
    print(f"News_Titel:{news_title}")
    print(f"News_Paragraph :{news_p}")
    
    # Close the browser after scraping
    browser.quit()

    #featured_image_url 
    browser = init_browser()
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    # Set time sleep for it not to crash 
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    #scrapping for images name
    #image_name = soup.find('div', class_='floating_text_area')

    image_name = soup.find('img', class_= 'headerimage fade-in')['src']
    print(image_name)

    featured_image_url = url + image_name
    print(f"The image complete url for the featured image is: {featured_image_url}")
    
    # Close the browser after scraping
    browser.quit()

    #Mars Facts step 3 
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    mars_df = tables[0]
    mars_df.columns = ['Mars_Planet_Profile', 'Values']
    html_table = mars_df.to_html(header = None, index = False)
    html_table.replace('\n','')

    # Close the browser after scraping
    browser.quit()
    
    #Step 4 hemisphere 
    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    # Set time sleep for it not to crash 
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    #scrapping 

    product = soup.find('div', class_ = 'collapsible results')
    hemisphere_items = product.find_all('div', class_='item')
    hemisphere_img_urls = []
    
    #Creating conditional while scrapping 
    for i in hemisphere_items:
        #Create a try statement
        try:
            hemisphere_title = i.find('h3').text
            hemisphere_href = i.find('a')['href']
            hemisphere_url = "https://astrogeology.usgs.gov/" + hemisphere_href
            hemisphere_page = requests.get(hemisphere_url).text
            soup = bs(hemisphere_page, 'html.parser')

            hemisphere_page_img = soup.select('#wide-image > div > ul > li:nth-child(1) > a')
            hemisphere_img_url = hemisphere_page_img[0]['href']
            hemisphere_img_dict = {"title": hemisphere_title, "img_url": hemisphere_img_url}
            hemisphere_img_urls.append(hemisphere_img_dict)

         #Except clause
        except Exception as e:
            print(e)





    # Store data in a dictionary
    mars_data = {
            "News_Title": news_title,
            "Paragraph_Text": news_p,
            "Most_Recent_Mars_Image": featured_image_url,
            "Mars_Table": html_table,
            "Mars_Hemispheres": hemisphere_img_urls
        }


    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
