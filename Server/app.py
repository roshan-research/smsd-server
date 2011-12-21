from flask import Flask
from flask import request
import hashlib
app = Flask(__name__)
app.config.from_object(__name__)


dbg = True

@app.route('/')
def hw():
	return 'Hey, Do you know how to use this? Or not?'

@app.route('/get/', methods=['GET', 'POST'])
def get():
	return str(request.method)

@app.route('/put/')
def put():
	pass

if __name__ == '__main__':
	if dbg:
		app.run(debug=True)
	else:
		app.run('0.0.0.0')