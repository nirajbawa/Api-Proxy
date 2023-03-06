from flask import Flask, request
import requests
from flask_cors import CORS


app = Flask(__name__)

CORS(app)

@app.route("/", methods=["GET"])
def Home():
    return "hello"

@app.route("/api", methods=["GET"])
def api():
    url = request.args.get("url");
    print(url)
    Apiurl = url.replace("|", "&")
    print(Apiurl)
    response = requests.get(Apiurl)
    response_json = response.json()
    print(response_json)
    return response_json
