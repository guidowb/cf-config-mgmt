#!/bin/bash

while read key value
do
	export "$key"="$value"
done < <( python app/config-client/get-config.py )
