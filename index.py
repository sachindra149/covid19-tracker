from flask import Flask, render_template, jsonify
import json
import requests
import time
# app = Flask(__name__, static_url_path="/public", static_folder='public')
app = Flask(__name__)

config_file = open("./static/api/config.json", "r")
config = json.loads(config_file.read())

ts = time.gmtime()
currentTime = time.strftime("%Y-%m-%d %H:%M:%S", ts)
# print currentTime.split()[0]


@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def home():
    totalCasesData = requests.get(config['totalList'])
    country = requests.get(config['getCountry'])
    countryRelatedData = requests.get(config['allCountriesData'])
    countrySpecificData = [i for i in countryRelatedData.json(
    ) if i['country'] == country.json()['country_name']]
    # print countrySpecificData
    # print country.json()
    print type(totalCasesData)
    # print "country"
    print type(totalCasesData.json())
    print type(country.json())
    # print country.json()["country_name"]
    # print countryRelatedData.json()
    # print type(config['faqs'])
    # print eval(totalCasesData.text())
    # print json.dumps(totalCasesData.json())
    # print type(totalCasesData.json())
    return render_template("home.html", data=totalCasesData.json(), country=country.json(), countrySpecificData=countrySpecificData[0], lastUpdated=currentTime)


@app.route("/getTotalCases", methods=['GET', 'POST'])
def getTotalCases():
    totalCasesData = requests.get(config['totalList'])
    return str(json.dumps(totalCasesData.json()))


@app.route("/countries")
def countries():
    countryRelatedData = requests.get(config['allCountriesData'])
    return render_template("countries.html", countryRelatedData=countryRelatedData.json())


@app.route("/faqs")
def faq():
    return render_template("faqs.html", faqs=config['faqs'])


@app.route("/app-info")
def appInfo():
    return render_template("info.html")


@app.errorhandler(404)
def notFound(e):
    return render_template("404.html")


if(__name__ == "__main__"):
    app.run(debug=True)
