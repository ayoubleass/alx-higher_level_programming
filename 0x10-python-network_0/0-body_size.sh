#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response.

if [ -n "$1" ]
then
	size=$(curl -sI "$1" | grep -i "^Content-Length:" | cut -d ':' -f 2)
	echo "$size"
fi
