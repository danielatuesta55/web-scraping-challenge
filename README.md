# Web Scraping - Mission to Mars

## Web scraping Homework - Mission to Mars

### Intention of the Repository

This Repository has been made to summit the homework assignment for my Data Science Bootcamp at Northwestern University

Web scraping challenge

Student: Jorge Daniel Atuesta

May, 2021


### Inside of this repository

In this repository, the reader will encounter my solution to the homework assignment Web scraping challange. The repository is organized in folders and a README.md (The file you are currently reading). Here is the list of the folders and their contents so you can navigate through them.

I hope you find my work not only to be complete but to display all the knowledge learned throughout this portion of the Data Science Bootcamp at Northwestern University.

1. **Images**: Inside this folder you will find the images for the instructions provided by the institution. *You can skip this folder if you want*.
2. **app**: Inside this folder, you will have the chance to access my code for the assignment and all the output data. I encourage you to take a look inside as you will find the solution to the project. Here are what's inside:

* *app file*: You will find my app code used in flask.
* *scraped_mars*: The code used to scrapped the different urls.
* *templates*: You will find the template file for the webpage.
* *table*: This is a html file created after the scrapp of the table in one of the urls. This was created through jupyterlab notebook.

3. **mission_to_mars:** Here you will find the jupyter lab notebook used to run queries.
4. **README.md**: it's the current file you are reading. I strongly suggest navigating through it and look at the project's objective solution and analysis.

I hope you find my work not only to be complete but to display all the knowledge learned throughout this portion of the Data Science Bootcamp at Northwestern University.

## Web Scraping Project

![mission_to_mars](Images/mission_to_mars.png)


### Project's Aim

Using HTML, CSS, Bootstrap, python and pandas I was tasked to create a webpage to display the data scraped from some urls that had information on Mars.

#### Project's Challanges

#### Scraping

Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Create a Jupyter Notebook file called `mission_to_mars.ipynb` and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.

##### NASA Mars News

Scrape the [Mars News Site](https://redplanetscience.com/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

##### JPL Mars Space Images - Featured Image

* Visit the url for the Featured Space Image site [here](https://spaceimages-mars.com).
* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.
* Make sure to find the image url to the full size `.jpg` image.
* Make sure to save a complete url string for this image.

##### Mars Facts

* Visit the Mars Facts webpage [here](https://galaxyfacts-mars.com) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
* Use Pandas to convert the data to a HTML table string.

##### Mars Hemispheres

* Visit the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres.
* You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
* Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.
* Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

#### MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.
* Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

  * Store the return value in Mongo as a Python dictionary.
* Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.
* Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

## References

Richardson, L. (2020). *Beautiful Soup Documentation*. Retrieved from crummy: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

## Assignment instructions provided by Northwestern Data Science Bootcamp

### Web Scraping Homework - Mission to Mars

![mission_to_mars](Images/mission_to_mars.png)

In this assignment, you will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what you need to do.

#### Before You Begin

1. Create a new repository for this project called `web-scraping-challenge`. **Do not add this homework to an existing repository**.
2. Clone the new repository to your computer.
3. Inside your local git repository, create a directory for the web scraping challenge. Use a folder name to correspond to the challenge: **Missions_to_Mars**.
4. Add your notebook files to this folder as well as your flask app.
5. Push the above changes to GitHub or GitLab.

### Step 1 - Scraping

Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Create a Jupyter Notebook file called `mission_to_mars.ipynb` and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.

#### NASA Mars News

* Scrape the [Mars News Site](https://redplanetscience.com/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

```python
# Example:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
```

#### JPL Mars Space Images - Featured Image

* Visit the url for the Featured Space Image site [here](https://spaceimages-mars.com).
* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.
* Make sure to find the image url to the full size `.jpg` image.
* Make sure to save a complete url string for this image.

```python
# Example:
featured_image_url = 'https://spaceimages-mars.com/image/featured/mars2.jpg'
```

#### Mars Facts

* Visit the Mars Facts webpage [here](https://galaxyfacts-mars.com) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
* Use Pandas to convert the data to a HTML table string.

#### Mars Hemispheres

* Visit the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres.
* You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
* Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.
* Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

```python
# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]
```

---

### Step 2 - MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.
* Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

  * Store the return value in Mongo as a Python dictionary.
* Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.
* Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

![final_app_part1.png](Images/final_app.png)

---

### Step 3 - Submission

To submit your work to BootCampSpot, create a new GitHub repository and upload the following:

1. The Jupyter Notebook containing the scraping code used.
2. Screenshots of your final application.
3. Submit the link to your new repository to BootCampSpot.
4. Ensure your repository has regular commits (i.e. 20+ commits) and a thorough README.md file

### Hints

* Use Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.
* Use Pymongo for CRUD applications for your database. For this homework, you can simply overwrite the existing document each time the `/scrape` url is visited and new data is obtained.
* Use Bootstrap to structure your HTML template.

### Rubric

[Unit 12 Rubric - Web Scraping Homework - Mission to Mars](https://docs.google.com/document/d/1paGEIFS5yp2VQu6G8F45B4uj1t1t29zL73KEQrD0xpo/edit?usp=sharing)

---

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
