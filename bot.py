from flask import Flask
from flask import request as req
from flask import render_template
import githubbot.utils as gb
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('Hello')

@app.route('/recv', methods=['POST'])
def recv_webhook_event():
    return req.get_json()

def make_gh_request(endpoint):
    r = requests.get(endpoint)
    return r.status_code

def create_comment_on_pr(org, repo, pull):
    return make_gh_request(
        gb.PULL_REQUEST_COMMENT_URL.format(org, repo, pull)
    )
