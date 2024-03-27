#!/bin/bash


if [ -n "$1" ]
then
	size=$(curl -sI "$1" | grep -i "^Content-Length:" | cut -d ':' -f 2)
	echo "$size"
fi
