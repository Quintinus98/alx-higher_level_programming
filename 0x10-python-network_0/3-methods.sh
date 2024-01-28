#!/bin/bash
# A Bash script that displays all HTTP methods the server will accept
curl -sIL -X "OPTIONS" "$1" | grep -i Allow | awk '{$1=""; print $0}' | sed 's/^ //g'
