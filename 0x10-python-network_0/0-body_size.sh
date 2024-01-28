#!/bin/bash
# A Bash script that takes in a URL, displays the size of the body of the response
curl -s -I "$1" | grep -i Content-Length | awk '{print $2}'
