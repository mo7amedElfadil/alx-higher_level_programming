#!/usr/bin/env bash
task_file=$(dirname "$(dirname "$0")")/5-post_params.sh
if [ ! "$@" ]; then
	HOST=0.0.0.0:5000/route_6
else
	HOST="$1"
fi 


# sshpass allows you to provide the password for the user to ssh
# -p flag is used to provide the password
# < is used to redirect the file to the standard input of the command
sshpass -p "$pynetsandboxPW" ssh "$pynetsandboxUSER"@"$pynetsandboxHOST" 'bash -s' < "$task_file" "$HOST"

echo ""

# sends a POST request to the passed URL, and displays the body of the response

# A variable email must be sent with the value test@gmail.com
# A variable subject must be sent with the value I will always be here for PLD
# You have to use curl
# Alt
# curl -sX POST -d  "email=test%40gmail.com&subject=I+will+always+be+here+for+PLD" "$1"
