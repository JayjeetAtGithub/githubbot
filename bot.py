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
            create_comment_on_pr('JayjeetAtGithub', 'git-workshop-test', payload['number'])
    
    return "Success"


def make_gh_request(endpoint, req_type='GET', payload=None):
    headers = {
        'Authorization': 'Basic SmF5amVldEF0R2l0aHViOkpheWplZXRAMTk5OQ=='
    }
    if req_type == 'POST':
        r = requests.post(endpoint, json=payload,headers=headers)
    elif req_type == 'GET':
        r = requests.get(endpoint,headers=headers)
    return r.status_code

def create_comment_on_pr(org, repo, pull):
    payload = {
        'body':'Thanks for opening this PR'
    }
    return make_gh_request(
        PULL_REQUEST_COMMENT_URL.format(org, repo, pull),
        'POST',
        payload
    )
