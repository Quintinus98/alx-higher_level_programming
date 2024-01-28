#!/usr/bin/python3
"""A Python script that fetches
https://alx-intranet.hbtn.io/status"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    try:
        r = requests.get(url)
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError as e:
        print("Error code:", e.errno)
    except requests.exceptions.RequestException as e:
        print('Error code:', e.errno)
