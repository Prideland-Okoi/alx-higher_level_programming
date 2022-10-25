#!/usr/bin/python3
"""
A Python script that shows the last 10 commits of a repository
in GitHub
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    url = requests.get('https://api.github.com/repos/{}/{}/commits'
                       .format(argv[2], argv[1]))
    json_o = url.json()
    for commit in json_o[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
