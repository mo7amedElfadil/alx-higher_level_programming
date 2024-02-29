#!/usr/bin/env bash
# This script  takes in a URL, sends a GET request to the URL, and displays the body of the response

task_file=$(dirname "$(dirname "$0")")/1-body.sh
if [ ! "$@" ]; then
	HOST=0.0.0.0:5000/route_1
else
	HOST="$1"
fi 


# sshpass allows you to provide the password for the user to ssh
# -p flag is used to provide the password
# < is used to redirect the file to the standard input of the command
sshpass -p "$pynetsandboxPW" ssh "$pynetsandboxUSER"@"$pynetsandboxHOST" 'bash -s' < "$task_file" "$HOST"

echo ""
