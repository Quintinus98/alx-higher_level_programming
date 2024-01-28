#!/usr/bin/python3
"""A Python script that  takes in a URL and an email, sends a
POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""

if __name__ == '__main__':
    from urllib import request, parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}

    data = parse.urlencode(values)
    data = data.encode()    # encode in utf-8
    req = request.Request(url, data)

    with request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
