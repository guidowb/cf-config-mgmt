#!/bin/sh

python ../config-client/get-config.py | while read key value
do
	export "$key"="$value"
done
