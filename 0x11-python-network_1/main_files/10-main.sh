#!/usr/bin/env bash
task_file=$(dirname "$(dirname "$0")")/10-my_github.py
file=$(basename "$task_file")
if [ ! "$1" ]; then
	USERNAME=$gitUSER
else
	USERNAME="$1"
fi 
if [ ! "$2" ]; then
	PASSWORD=$gitTOKEN
else
	PASSWORD="$2"
fi
echo "Running $file with $USERNAME and $PASSWORD"
python3 "$task_file" "$USERNAME" "$PASSWORD"
