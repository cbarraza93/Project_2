from flask import Flask, render_template
import pymongo

app = Flask(__name__)

# setup mongo connection
conn = 'mongodb+srv://cbarraza:Gramercy1@cluster0.q26pfay.mongodb.net/Cluster0'
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.SWFilmss


@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    movies = list(db.segment.find())
    print(movies)

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", movies=movies)


if __name__ == "__main__":
    app.run(debug=True)
