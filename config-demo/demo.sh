#!/bin/bash

set -o nounset -o errexit -o pipefail

history=()
history_index=0

while IFS= read -r -n 1 -s char
do
	if [ "$char" == $'\x1b' ]
	then
		while IFS= read -r -n 2 -s rest
		do
			char+="$rest"
			break
		done
	fi

	if [ "$char" == $'\x1b[A' ]
	then
		echo "up"	
	elif [ "$char" == $'\x1b[B' ]
	then
		echo "down"
	fi
done
