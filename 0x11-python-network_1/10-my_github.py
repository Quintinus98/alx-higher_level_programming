#!/usr/bin/python3
"""A Python script that fetches
https://alx-intranet.hbtn.io/status"""

if __name__ == '__main__':
    import requests
    import sys

    username = sys.argv[1]
    passwd = sys.argv[2]
    url = f'https://api.github.com/users/{username}'
    headers = {"Authorization": f"Bearer {passwd}",
               "X-GitHub-Api-Version": "2022-11-28",
               "Accept": "application/vnd.github+json"}

    r = requests.get(url, headers=headers)
    print(r.json().get('id'))
