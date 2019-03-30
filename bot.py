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
    event_type = req.headers['X-GitHub-Event']
    if event_type == 'pull_request':
        payload = json.loads(req.data)
        if payload['action'] == 'opened':
            print(str(payload))
    
    return "Success"


def make_gh_request(endpoint):
    r = requests.get(endpoint)
    return r.status_code

def create_comment_on_pr(org, repo, pull):
    return make_gh_request(
        PULL_REQUEST_COMMENT_URL.format(org, repo, pull)
    )
