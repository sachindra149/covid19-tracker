# import the flask library and its underlying objects, making the code available to the rest of the application.

from flask import Flask, jsonify
import requests

# Then initialise a new Flask object to a variable called app. Every Flask application must create an application instance. The web server will pass all the requests to this object under the WSGI protocol.
# Creates the Flask application object, which contains data about the application and also methods (object functions) that tell the application to do certain actions.
app = Flask(__name__)

# Starts the debugger. With this line, if your code is malformed, you will see an error when you visit your app. Otherwise you will only see a generic message such as Bad Gateway in the browser when there is a problem with your code.
app.config["DEBUG"] = True

books = [
    {
        'id': 0,
        'title': 'A Fire Upon the Deep',
        'author': 'Vernor Vinge',
        'first_sentence': 'The coldsleep itself was dreamless.',
        'year_published': '1992'
    },
    {
        'id': 1,
        'title': 'The Ones Who Walk Away From Omelas',
        'author': 'Ursula K. Le Guin',
        'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
        'published': '1973'
    },
    {
        'id': 2,
        'title': 'Dhalgren',
        'author': 'Samuel R. Delany',
        'first_sentence': 'to wound the autumnal city.',
        'published': '1975'
    }
]


@app.route("/", methods=["GET"])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route("/try-api")
def tryApi():
    return jsonify(books)


@app.route("/countries", methods=["GET"])
def getCountries():
    countries = requests.get("http://api.worldbank.org/v2/country?format=json")
    print countries.text
    return "Test"


if(__name__ == "__main__"):
    # A method that runs the application server.
    app.run(debug=True, port=8089)
