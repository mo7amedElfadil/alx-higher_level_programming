#!/usr/bin/env bash
task_file=$(dirname "$(dirname "$0")")/102-catch_me.sh
 
if [ ! "$@" ]; then
	HOST=0.0.0.0:5000/catch_me
else
	HOST="$1"
fi 


# sshpass allows you to provide the password for the user to ssh
# -p flag is used to provide the password
# < is used to redirect the file to the standard input of the command
sshpass -p "$pynetsandboxPW" ssh "$pynetsandboxUSER"@"$pynetsandboxHOST" 'bash -s' < "$task_file" 

echo ""

# curl -si 0.0.0.0:5000/catch_me
# curl -svX OPTIONS 0.0.0.0:5000/catch_me
# curl -sL -X PUT -H "text/html" 0.0.0.0:5000/catch_me ## gets the user id
# curl -v -L -sX PUT -H "Content-Type: application/json" -d '{"username": "val"}' 0.0.0.0:5000/catch_me
# curl -sLX PUT -d "user_id=98"  "0.0.0.0:5000/catch_me"
# curl -sLX PUT -H "Origin:UserName" -d "user_id=98"  "0.0.0.0:5000/catch_me"
