#!/usr/bin/env bash
# This script will print the size of the body of the response

task_file=$(dirname "$(dirname "$0")")/0-body_size.sh
if [ ! "$@" ]; then
	HOST=0.0.0.0:5000
else
	HOST="$1"
fi 

# sshpass allows you to provide the password for the user to ssh
# -p flag is used to provide the password
# < is used to redirect the file to the standard input of the command
sshpass -p "$pynetsandboxPW" ssh "$pynetsandboxUSER"@"$pynetsandboxHOST" 'bash -s' < "$task_file" "$HOST"
# in the task:
# -s flag is used to silent the output
# -I flag is used to only get the headers of the response
# grep is used to get the line that contains the Content-Length
# awk is used to print the second word of the line
