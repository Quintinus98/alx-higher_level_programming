#!/bin/bash
# A Bash script that sends a JSON POST request to a URL
curl -sH "Content-Type: application/json" -H "Accept: application/json" -d "@$2" "$1"
