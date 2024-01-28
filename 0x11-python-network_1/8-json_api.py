#!/usr/bin/python3
"""A Python script that fetches
https://alx-intranet.hbtn.io/status"""

if __name__ == '__main__':
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    q = "" if sys.argv[1] is None else sys.argv[1]
    try:
        r = requests.post(url, data={'q': q})
        json_obj = r.json()
        if not bool(json_obj):
            print('No result')
            exit(1)
        print('[{}] {}'.format(json_obj['id'], json_obj['name']))
    except requests.exceptions.JSONDecodeError as e:
        print('Not a valid JSON')
