# coding=utf8
import MySQLdb
import json
import log

SETTING_HOST = 'localhost'
SETTING_USER = 'root'
SETTING_PASSWD = ''
SETTING_DB = 'payambar'

admins = ['9376970224', '9128216439']
rabets = ['9125436744']

tafsir = ["09128083630","09123041652","09125143376","09124033658","09122016847","09124086716","09194728291","09127978670","09125227057","09124966143","09123761989","09124261477","09127056049","09128040602","09124485032","09131098647","09125367552","09126045074","09121075765","0924441451","09124334268","09123803341","09194701040","09126125601","09355123017","09127906932","09124058715","09127759634","09161620561","09329224030","09125500812","09177175257","09122057902","09125355713","09121083301","09127967418","09125103080","09352251690","0912394318","09358208442","09102108486","09126125601","09191237446","09125366687","09124783090","09124104547","09352144028","09122993015","0356283338","09122941610","09128208442","09121365501","09194063528","09352388135","09127080473","09192489300","09123588539","0912414732","09128216439","09126381411","09119130477","09125183196","09123907415","09127155263","09123765193","09125362319","09124950153","0912486712","09127114549","09122543215","09124500229","09126798273","09354203245","09127153915","09121499574","09122486876","09128118313","9121332524","09124946214","09123403862","09378636891","09127241240"]

admins_number = ['09128216439', '09376970224']
rabets_number = ['09125436744']

def createCon():
	return MySQLdb.connect(host = SETTING_HOST, user = SETTING_USER, passwd = SETTING_PASSWD, db = SETTING_DB, charset = 'utf8')

def getCursor(con = None):
	if con == None:
		con = createCon()
	return con.cursor()

def isMobileValid(con, name, key):
	if con == None:
		return False
	else:
		mobile_query = 'SELECT * FROM mobiles WHERE name = "%s" AND `key` = "%s"' % (name, key)
		con.query(mobile_query)
		r = con.store_result()
		if r.num_rows() > 0:
			return True
		else:
			return False

def setSentTime(con, s_ids):
	if con == None:
		return False
	else:
		u_query = "UPDATE transactions SET sent_at = NOW() WHERE id IN (%s)" % s_ids
		con.query(u_query)
	con.commit()

def setDeliveredTime(con, s_ids):
	if con == None:
		return False
	else:
		u_query = "UPDATE transactions SET delivered_at = NOW() WHERE id IN (%s)" % s_ids
		con.query(u_query)
	con.commit()

def handelRecieved(number, text):
	#log data
	log.receivedMessage(number, text)

	if number[-10:] in admins:
		if text.lower() == 'stop':
			return json.dumps({'status': 'stop'})
		elif text.lower == 'start':
			return json.dumps({'status': 'start'})
		elif text.lower() in ['hello', 'hi', 'hello world', 'salam']:
			sendThis = "Hello Admin"
			add_query = 'INSERT INTO transactions (`to`, `text`) VALUES ("%s", "%s")' %(number, sendThis)
			con = createCon()
			con.query(add_query)
			con.commit()
			j = json.dumps({'status': 'ok'})
			return j
	if number[-10:] in rabets or number[-10:] in admins:
		if text.lower() == 'help':
			addHelp(number)
			j = json.dumps({'status': 'ok'})
			return j
		else:
			parts = text.split("\n")
			if parts[0].lower().strip() == 'send to all':
				if parts[1].lower().strip() == 'admins':
					addForGroup(admins_number, "\n".join(parts[2:]))
					return json.dumps({'status': 'ok'})
				elif parts[1].lower().strip() == 'rabets':
					addForGroup(rabets_number, "\n".join(parts[2:]))
					return json.dumps({'status': 'ok'})
				elif parts[1].lower().strip() == 'tafsir':
					#TODO verfify
					return json.dumps({'status': 'ok'})
				else:
					print parts[1].lower().strip()
					return json.dumps({'status': 'Not OK'})
			else:
				print parts[0].lower().strip()
				return json.dumps({'status': 'Not OK'})

def handelRing(number):
	#log data
	log.phoneRang(number)
	return json.dumps({'status': 'OK'})

#This will add a help response message fot this number to the database so the phone will send it when it asks for it
def addHelp(number):
	sendThis = u'سلام\nبرای ارسال پیامک به تمام مشترکان مجموعه تفسیر قرآن حاج آقا قاسمیان یک پیامک مثل زیر به این شماره ارسال کنید. شاید لازم باشد که ارسال پیامک را تأیید کنید.\n\nsend to all\ntafsir\nمتنی که برای همه ارسال خواهد شد'.encode('UTF-8')
	add_query = 'INSERT INTO transactions (`to`, `text`) VALUES ("%s", "%s")' %(number, sendThis)
	con = createCon()
	con.query(add_query)
	con.commit()

def addForGroup(numbers, text):
	for t_n in numbers:
		add_query = 'INSERT INTO transactions (`to`, `text`) VALUES ("%s", "%s")' %(t_n, text)
		con = createCon()
		con.query(add_query.encode('UTF-8'))
		con.commit()