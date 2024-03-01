#!/usr/bin/env bash
task_file=$(dirname "$(dirname "$0")")/101-post_json.sh
json_file="my_json_0"
 
if [ ! "$@" ]; then
	HOST=0.0.0.0:5000/route_json
else
	HOST="$1"
fi 


# sshpass allows you to provide the password for the user to ssh
# -p flag is used to provide the password
# < is used to redirect the file to the standard input of the command
sshpass -p "$pynetsandboxPW" ssh "$pynetsandboxUSER"@"$pynetsandboxHOST" 'bash -s' < "$task_file" "$HOST" "$json_file"

echo ""

