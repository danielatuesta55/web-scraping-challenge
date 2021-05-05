#import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import urllib.request
import requests
from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser
def scrape():
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

    #featured_image_url 
    # STUCK !!!
    featured_image_url = 'https://mars.nasa.gov/#red_planet/0'
    browser.visit(featured_image_url)
    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    #relative image path
    #<img alt="Perseverance's Selfie with Ingenuity" id="main_image" src="/system/news_items/main_images/8936_First_selfie_animation_1200.jpg">
    image_name= soup.find('div', class_='image_container')
    mars_img = url + relative_image_path

    # Store data in a dictionary
    mars_data = {
            "News_Title": news_title,
            "Paragraph_Text": news_p,
            "Most_Recent_Mars_Image": featured_image_url,
            "Mars_Weather": mars_weather,
            "Mars_Table": html_table,
            "Mars_Hemispheres": hemisphere_img_urls
        }


    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
