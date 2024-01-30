#!/bin/bash
# A Bash script that sends a JSON POST request to a URL
curl -sX PUT -d "user_id=98" 0.0.0.0:5000/catch_me
