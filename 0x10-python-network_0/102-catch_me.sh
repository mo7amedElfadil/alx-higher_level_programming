#!/usr/bin/env bash
# This script makes the server respond with a message containing You got me!
curl -sX PUT -d "user_id=98" -L 0.0.0.0:5000/catch_me
