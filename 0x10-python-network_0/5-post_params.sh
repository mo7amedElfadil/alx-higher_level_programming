#!/bin/bash
# Sends a POST request to the passed URL, and displays the body of the response
curl -sd "email=test%40gmail.com&subject=I+will+always+be+here+for+PLD" "$1"
