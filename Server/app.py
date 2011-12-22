# coding=utf8
from flask import Flask
from flask import request
import db
import json
import datetime

app = Flask(__name__)
app.config.from_object(__name__)


dbg = True
# dbg = False

@app.route('/')
def hw():
	return 'Hey, Do you know how to use this? Or not?'

@app.route('/get/', methods=['POST'])
def get():
	arr = []
	con = db.createCon()
	LIMIT = 10 # Default value for a 

	# Validate and Get POST data
	keys = request.form.keys()
	print keys
	has_key = has_name = has_limit = False
	for key in keys:
		if key == 'key':
			has_key = True
		if key == 'name':
			has_name = True
		if key == 'limit':
			has_limit = True
	
	if not has_key or not has_name:
		return "NO"
	mobile_key = request.form['key']
	mobile_name = request.form['name']
	if has_limit:
		LIMIT = request.form['limit']

	mobile_query = "SELECT * FROM mobiles WHERE name = \"%s\"" % mobile_name
	con.query(mobile_query)
	r = con.store_result()
	if r.num_rows() < 1:
		return "NO! your key is not here!"
	else:
		row = r.fetch_row()
		(m_id, m_name, m_key) = row[0]
		if mobile_key != m_key:
			return "NO! you have the wrong key!"



	# RETURN THE MESSAGES
	get_query = "SELECT * FROM transactions WHERE delivered_at IS NULL LIMIT %d" % LIMIT
	con.query(get_query)
	r = con.store_result()
	for i in xrange(0,r.num_rows()):
		dic = {}
		row = r.fetch_row()
		(m_id, m_to, m_text, c_DT, d_DT, s_DT) = row[0]

		# Add to array
		dic['id'] = m_id
		dic['to'] = m_to
		dic['text'] = m_text
		arr.append(dic)

		# Update Database
		update_query = "UPDATE transactions SET delivered_at = now() WHERE id = %d" % m_id
		con.query(update_query)
		con.commit()

	dic = {}
	dic['messages'] = arr
	j = json.dumps(dic)
	return j

@app.route('/put/', methods=['POST'])
def put():
	pass

@app.route('/success/', methods=['POST'])
def success():
	keys = request.form.keys()

if __name__ == '__main__':
	if dbg:
		app.run(debug=True)
	else:
		app.run('0.0.0.0')