#!/bin/bash
# This script makes the server respond with a message containing You got me!
curl -sLX PUT -d  "user_id=98" -H "Origin: School" -e 0.0.0.0:5000/catch_me 0.0.0.0:5000/catch_me_2
