from flask import Flask
from flask import request as req
import githubbot.utils as gb
import requests

app = Flask(__name__)

@app.route('/')
def recv_webhook():
    print(req.get_json())
    return


def make_gh_request(endpoint):
    r = requests.get(endpoint)
    return r.status_code

def create_comment_on_pr(org, repo, pull):
    return make_gh_request(
        gb.PULL_REQUEST_COMMENT_URL.format(org, repo, pull)
    )
