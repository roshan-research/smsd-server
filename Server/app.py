# coding=utf8
from flask import Flask
from flask import request
import db
import json
import datetime

app = Flask(__name__)
app.config.from_object(__name__)


dbg = True

@app.route('/')
def hw():
	return 'Hey, Do you know how to use this? Or not?'

@app.route('/get/', methods=['GET', 'POST'])
def get():
	arr = []
	con = db.createCon()
	con.query("SELECT * FROM transactions WHERE delivered_at IS NULL LIMIT 10")
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

if __name__ == '__main__':
	if dbg:
		app.run(debug=True)
	else:
		app.run('0.0.0.0')