import MySQLdb

SETTING_HOST = 'localhost'
SETTING_USER = 'root'
SETTING_PASSWD = ''
SETTING_DB = 'payambar'

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
	print "OB"
	if con == None:
		return False
	else:
		u_query = "UPDATE transactions SET sent_at = NOW() WHERE id IN (%s)" % s_ids
		con.query(u_query)
	con.commit()	
