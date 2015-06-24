import os
import json
from flask import jsonify

from flask import Flask
app = Flask(__name__)

@app.route("/env")
def environment():
	properties = []
	for k,v in sorted(os.environ.iteritems()):
		properties.append(k + "=" + v)
	return json.dumps(properties, indent=4)

if __name__ == "__main__":
	print "before app.run"
	print os.getenv('PORT')
	app.run(host='0.0.0.0', port=int(os.getenv('PORT', '8080')))
