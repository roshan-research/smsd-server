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

def isMobileValid(cur, name, key):
	if cur == None:
		return False
	else:
		