#!/usr/bin/python3
""" Main file """
import sys
import os
import subprocess
# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory by going one level up
parent_dir = os.path.dirname(current_dir)
# Add the parent directory to sys.path
sys.path.append(parent_dir)
"""
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.

You must use the packages urllib and sys
You are not allow to import packages other than urllib and sys
The value of this variable is different for each request
You don’t need to check arguments passed to the script (number or type)
You must use a with statement
"""
subprocess.run(["python3", "5-hbtn_header.py", sys.argv[1] if len(sys.argv) > 1 else "https://alx-intranet.hbtn.io"])
