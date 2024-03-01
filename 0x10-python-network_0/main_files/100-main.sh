#!/bin/bash
task_file=$(dirname "$(dirname "$0")")/100-status_code.sh
if [ ! "$@" ]; then
	HOST=0.0.0.0:5000
else
	HOST="$1"
fi 


# sshpass allows you to provide the password for the user to ssh
# -p flag is used to provide the password
# < is used to redirect the file to the standard input of the command
sshpass -p "$pynetsandboxPW" ssh "$pynetsandboxUSER"@"$pynetsandboxHOST" 'bash -s' < "$task_file" "$HOST"

echo ""

