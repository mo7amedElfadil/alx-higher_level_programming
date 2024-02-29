#!/usr/bin/env bash
# takes in a URL and displays all HTTP methods the server will accept.
task_file=$(dirname "$(dirname "$0")")/3-methods.sh
if [ ! "$@" ]; then
	HOST=0.0.0.0:5000/route_4
else
	HOST="$1"
fi 


# sshpass allows you to provide the password for the user to ssh
# -p flag is used to provide the password
# < is used to redirect the file to the standard input of the command
sshpass -p "$pynetsandboxPW" ssh "$pynetsandboxUSER"@"$pynetsandboxHOST" 'bash -s' < "$task_file" "$HOST"

echo ""

# alternative methods:
# curl -sI "$1" | grep "Allow:" | awk '{print $2:}'
# curl -sI "$1" | grep "Allow:" | awk '{print substr($0, index($0,$2))}'
