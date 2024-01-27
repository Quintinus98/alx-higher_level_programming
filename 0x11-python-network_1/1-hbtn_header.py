#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as res:
        req_id = res.headers.get('X-Request-Id')
        print(req_id)
