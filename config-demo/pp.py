import sys
import json

doc = json.load(sys.stdin)
json.dump(doc, sys.stderr, indent=4)
