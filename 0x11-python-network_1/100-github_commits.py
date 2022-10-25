#!/usr/bin/python3
"""
A Python script that shows the last 10 commits of a repository
in GitHub
"""
from requests import get, auth
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    headers = {
            'Accept': 'application/vnd.github.v3+json',
            }
    params = {
            'page':10,
            }

    url_res = requests.get('https://api.github.com/repos/{}/{}/commits'.format(owner, repo),
            headers=headers, params=params)
    r = get(url)
    json_o = url_res.json()
    for commit in json_o:
        print(commit(['sha'] + ':', commit['commit']['author']['name'])
