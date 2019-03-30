from flask import Flask
from flask import request as req
from flask import render_template
from githubbot.utils import PULL_REQUEST_COMMENT_URL
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome"

@app.route('/recv', methods=['POST'])
def recv_webhook_event():
    payload = json.loads(req.data)
    print(str(payload))
    return str(payload)

def make_gh_request(endpoint):
    r = requests.get(endpoint)
    return r.status_code

def create_comment_on_pr(org, repo, pull):
    return make_gh_request(
        PULL_REQUEST_COMMENT_URL.format(org, repo, pull)
    )
