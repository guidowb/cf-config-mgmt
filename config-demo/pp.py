import sys
import json

input = sys.stdin.readlines()
try:
	doc = json.loads(''.join(input))
	json.dump(doc, sys.stderr, indent=4)
	print
except:
	for line in input:
		print line
