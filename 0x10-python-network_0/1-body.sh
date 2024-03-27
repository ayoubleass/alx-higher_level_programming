#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response
status=$(curl -sI "$1" | head -n 1 | cut -d ' ' -f 2); if [ "$status" -eq 200 ];then curl -sX GET "$1" -L; fi
