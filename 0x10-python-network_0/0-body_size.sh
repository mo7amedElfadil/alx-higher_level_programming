#!/usr/bin/env bash
# This script will print the size of the body of the response
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'