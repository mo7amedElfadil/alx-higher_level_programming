#!/usr/bin/env bash
# takes in a URL and displays all HTTP methods the server will accept.
# Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)

# The email must be sent in the email variable
# You must use the packages urllib and sys
# You are not allowed to import packages other than urllib and sys
# You don’t need to check arguments passed to the script (number or type)
# You must use the with statement
task_file=$(dirname "$(dirname "$0")")/6-post_email.py
file=$(basename "$task_file")
if [ ! "$1" ]; then
	HOST=http://0.0.0.0:5000/post_email
else
	HOST="$1"
fi 
if [ ! "$2" ]; then
	EMAIL="hr@holbertonschool.com"
else
	EMAIL="$2"
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
	python3 ~/"$file" "$HOST" "$EMAIL"
EOF
sshpass -p "$pynetsandboxPW" ssh "$pynetsandboxUSER"@"$pynetsandboxHOST" "rm ~/$file"
echo ""
