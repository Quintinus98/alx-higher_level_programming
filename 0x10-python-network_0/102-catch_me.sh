#!/bin/bash
# A Bash script that sends a JSON POST request to a URL
curl -sLX PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
