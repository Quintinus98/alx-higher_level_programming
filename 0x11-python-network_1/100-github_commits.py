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

    r = requests.get(url, headers=headers, params={'per_page': 10})
    commits = r.json()
    for commit in commits:
        sha = commit.get('sha')
        author = commit['commit']['author']['name']
        print("{}: {}".format(sha, author))
