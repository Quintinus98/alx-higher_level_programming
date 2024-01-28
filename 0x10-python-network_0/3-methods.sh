#!/bin/bash
# A Bash script that sends a DELETE request to the URL
curl -sI "$1" | grep -i Allow | awk '{print $2}'
