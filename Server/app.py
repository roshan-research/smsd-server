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
	LIMIT = 3 # Default value for a 

	# Validate and Get POST data
	keys = request.form.keys()
	has_key = has_name = has_limit = False
	for key in keys:
		if key == 'key':
			has_key = True
		if key == 'name':
			has_name = True
		if key == 'limit':
			has_limit = True
	
	if (not has_key) or (not has_name):
		return json.dump({'error': "NO, Input Error!"})
	
	mobile_key = request.form['key']
	mobile_name = request.form['name']

	if has_limit:
		LIMIT = request.form['limit']
	
	if not db.isMobileValid(con, mobile_name, mobile_key):
		con.close()
		return json.dump({'error': "NO! your name and/or key is not here!"})
	# RETURN THE MESSAGES
	get_query = "SELECT * FROM transactions WHERE delivered_to_phone_at IS NULL LIMIT %d" % LIMIT
	con.query(get_query)
	r = con.store_result()
	for i in xrange(0,r.num_rows()):
		dic = {}
		row = r.fetch_row()
		(m_id, m_to, m_text, c_CA, c_DTPA, d_SA, s_DA) = row[0]

		# Add to array
		dic['id'] = m_id
		dic['to'] = m_to
		dic['text'] = m_text
		arr.append(dic)

		# Update Database
		update_query = "UPDATE transactions SET delivered_to_phone_at = now() WHERE id = %d" % m_id
		con.query(update_query)
		con.commit()

	dic = {}
	dic['messages'] = arr
	j = json.dumps(dic)
	con.close()
	print j
	return j

@app.route('/sent/', methods=['POST'])
def sent():
	con = db.createCon()
	# Validate and Get POST data
	keys = request.form.keys()
	has_key = has_name = has_ids = False
	for key in keys:
		if key == 'key':
			has_key = True
		if key == 'name':
			has_name = True
		if key == 'ids':
			has_ids = True
	
	if not has_key or not has_name:
		return json.dump({'error': "NO, Input Error!"})
	mobile_key = request.form['key']
	mobile_name = request.form['name']

	if not db.isMobileValid(con, mobile_name, mobile_key):
		con.close()
		return json.dump({'error': "NO! your name and/or key is not here!"})
	
	if has_ids:
		success_ids = request.form['ids']
		db.setSentTime(con, success_ids)
		con.close()
		return json.dumps({'success': 'success'})
	else:
		con.close()
		return json.dumps({'error': 'NO! success'})

@app.route('/delivered/', methods=['POST'])
def delivered():
	con = db.createCon()
	# Validate and Get POST data
	keys = request.form.keys()
	has_key = has_name = has_ids = False
	for key in keys:
		if key == 'key':
			has_key = True
		if key == 'name':
			has_name = True
		if key == 'ids':
			has_ids = True
	
	if not has_key or not has_name:
		return json.dump({'error': "NO, Input Error!"})
	mobile_key = request.form['key']
	mobile_name = request.form['name']

	if not db.isMobileValid(con, mobile_name, mobile_key):
		con.close()
		return json.dump({'error': "NO! your name and/or key is not here!"})
	
	if has_ids:
		success_ids = request.form['ids']
		db.setDeliveredTime(con, success_ids)
		con.close()
		return json.dumps({'success': 'success'})
	else:
		con.close()
		return json.dumps({'error': 'NO! success'})

@app.route('/r/', methods=['POST'])
def r():
	con = db.createCon()
	keys = request.form.keys()
	has_key = has_name = has_from = has_text = False
	for key in keys:
		if key == 'key':
			has_key = True
		if key == 'name':
			has_name = True
		if key == 'from':
			has_from = True
		if key == 'text':
			has_text = True
	
	if not has_key or not has_name or not has_from or not has_key:
		con.close()
		return json.dumps({'error': "NO, Input Error!"})
	
	mobile_key = request.form['key']
	mobile_name = request.form['name']
	mobile_from = request.form['from']
	mobile_text = request.form['text']

	if not db.isMobileValid(con, mobile_name, mobile_key):
		con.close()
		return json.dump({'error': "NO! your name and/or key is not here!"})
	
	status = db.handelRecieved(mobile_from, mobile_text)
	return status

if __name__ == '__main__':
	if dbg:
		app.run('0.0.0.0', debug=True)
	else:
		app.run('0.0.0.0')