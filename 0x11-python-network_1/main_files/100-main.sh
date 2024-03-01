#!/usr/bin/env bash
task_file=$(dirname "$(dirname "$0")")/100-github_commits.py
file=$(basename "$task_file")
if [ ! "$1" ]; then
	REPO="rails"
else
	REPO="$1"
fi 
if [ ! "$2" ]; then
	NAME="rails"
else
	NAME="$2"
fi
echo "Running $file with $REPO and $NAME"
python3 "$task_file" "$REPO" "$NAME"

