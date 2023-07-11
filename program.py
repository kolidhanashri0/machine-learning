from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/car-price-prediction")
def carpriceprediction():
    return render_template("carpriceprediction.html")


@app.route("/car-price-prediction-result")
def carpricepredictionresult():
    return render_template("carpricepredictionresult.html")