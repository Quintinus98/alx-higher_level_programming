#!/usr/bin/python3
"""A Python script that fetches
https://alx-intranet.hbtn.io/status"""

if __name__ == '__main__':
    import requests
    import sys

    repo = sys.argv[1]
    owner = sys.argv[2]
    headers = {"accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28"}
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'

    r = requests.get(url, headers=headers)
    for i in range(10):
        res = r.json()[i].get('commit')
        sha = res.get('tree').get('sha')
        author = res.get('author').get('name')
        print("{}: {}".format(sha, author))
