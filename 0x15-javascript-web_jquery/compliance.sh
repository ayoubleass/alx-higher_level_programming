#!/bin/bash
# This script change all the double quote to single quote

for file in $(find -type f -name '*js')
do
	sed -i "s/\"/'/g" "$file"
done
