from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_application")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():
   
    # Find one record of data from the mongo database
    mars_data = mongo.db.collection.find_one()

    #make auto generated table a bootstrap style table
    mars_data["Mars_Table"]=mars_data["Mars_Table"].replace('<table border="1" class="dataframe">',"<table class='table table-sm'>")
    
    print("--- MONGO DATA ---")
    print(mars_data)
    print("--- END MONGO DATA ---")

    # Return template and data
    return render_template("index.html", mission_mars=mars_data)



# Route that will trigger the scrape function
@app.route("/scrape") #insided the html this will be put inside the <a href="/scrape"></a>
def scrape():
    
    # Run the scrape function
    mars_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/",302)



if __name__ == "__main__":
    app.run(debug=True)