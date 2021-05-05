#import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit https://mars.nasa.gov/news/
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    
    # Set time sleep for it not to crash 
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    #News title
    news_title = soup.find('div', 'class' == "content_title")

    #News paragraph
    news_p = soup.find('div','class' == "article_teaser_body")

    #featured_image_url 
    featured_image_url = 'https://mars.nasa.gov/system/news_items/main_images/8936_First_selfie_animation_1200.jpg'
    
    #relative image path
    #<img alt="Perseverance's Selfie with Ingenuity" id="main_image" src="/system/news_items/main_images/8936_First_selfie_animation_1200.jpg">
    relative_image_path = soup.find_all('img')[2]["src"]
    mars_img = url + relative_image_path

    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "mars_img" : mars_img
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
