#!/usr/bin/env bash
task_file=$(dirname "$(dirname "$0")")/7-error_code.py
file=$(basename "$task_file")
if [ ! "$1" ]; then
	HOST=http://0.0.0.0:5000/status_401
else
	HOST="$1"
fi 

# sshpass allows you to provide the password for the user to ssh
# -p flag is used to provide the password
# < is used to redirect the file to the standard input of the command

echo "checking if file exists remotely"
sshpass -p "$pynetsandboxPW" ssh  "$pynetsandboxUSER"@"$pynetsandboxHOST" "test -f ~/$file"
if [ $? -eq 0 ]; then
	echo "file exists remotely"
else
	echo "file does not exist remotely. Sending file to remote host."
	sshpass -p "$pynetsandboxPW" scp -o StrictHostKeyChecking=no "$task_file" "$pynetsandboxUSER"@"$pynetsandboxHOST":~/
fi

# sshpass -p "$pynetsandboxPW" ssh "$pynetsandboxUSER"@"$pynetsandboxHOST" "python3 ~/$file $HOST $EMAIL"
sshpass -p "$pynetsandboxPW" ssh "$pynetsandboxUSER"@"$pynetsandboxHOST" 'bash -s' <<EOF 
	python3 ~/"$file" "$HOST" 
EOF
sshpass -p "$pynetsandboxPW" ssh "$pynetsandboxUSER"@"$pynetsandboxHOST" "rm ~/$file"
echo ""

