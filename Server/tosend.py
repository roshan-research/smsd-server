# coding=utf8
import MySQLdb
import json
import db

SETTING_HOST = 'localhost'
SETTING_USER = 'root'
SETTING_PASSWD = ''
SETTING_DB = 'payambar'

def addSendToAll(number, text):
	conn = db.createCon()
	text = conn.escape_string(text.encode('UTF-8'))
	#UPSERT
	addquery = u"REPLACE INTO `to_send`(`number`, `text`) VALUES ('%s', '%s')".encode('UTF-8') %(number, text)
	conn.query(addquery)
	conn.commit()

def hasPendingSendToAll(number):
	conn = db.createCon()
	dbquery = 'SELECT * FROM `to_send` WHERE `number` = "%s" LIMIT 1' % (number)
	conn.query(dbquery)
	r = conn.store_result()
	if r.num_rows() > 0:
		return True
	else:
		return False

def getSendToAll(number):
	conn = db.createCon()
	dbquery = 'SELECT * FROM `to_send` WHERE `number` = "%s" LIMIT 1' % (number)
	conn.query(dbquery)
	r = conn.store_result()
	conn.commit()
	if r.num_rows() > 0:
		row = r.fetch_row()
		return row[0][1]
	else:
		return False
	
def removeSendToAll(number):
	conn = db.createCon()
	dbquery = 'DELETE FROM `to_send` WHERE `number` = %s' % (number)
	conn.query(dbquery)
	conn.commit()