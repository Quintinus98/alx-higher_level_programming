#!/usr/bin/python3
"""A  Python script that takes in a URL, sends a request to the
URL and displays the body of the response (decoded in utf-8)."""

if __name__ == '__main__':
    from urllib import request, error
    import sys

    url = sys.argv[1]
    req = request.Request(url)

    try:
        with request.urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
    except error.URLError as e:
        print('Reason: ', e.reason)
