from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_view():
    return "<h1>Welcome to my website</h1>"

@app.route("/Shreyas")
def mypage():
    return "<h1>This page blongs to Shreyas</h1>" 

app.run()