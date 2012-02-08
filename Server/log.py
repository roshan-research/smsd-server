# coding=utf8
import MySQLdb
import json
import db

SETTING_HOST = 'localhost'
SETTING_USER = 'root'
SETTING_PASSWD = ''
SETTING_DB = 'payambar'

def getCursor(con = None):
	if con == None:
		con = db.createCon()
	return con.cursor()

def closeCon(con = None):
	con.commit()

def receivedMessage(who, text):
	sms_received_type = 'sms-received'
	conn = db.createCon()
	text = conn.escape_string(text.encode('UTF-8'))
	comment_text = u"form: %s, text: %s".encode('UTF-8') %(who, text)
	logquery = u"INSERT INTO `logs`(`type`, `comment`) VALUES ('%s', '%s')".encode('UTF-8') %(sms_received_type, comment_text)
	conn.query(logquery)
	closeCon(conn)

def phoneRang(who):
	sms_received_type = 'phone-rang'
	conn = db.createCon()
	comment_text = "form: %s" %(who)
	logquery = "INSERT INTO `logs`(`type`, `comment`) VALUES ('%s', '%s')" %(sms_received_type, comment_text)
	conn.query(logquery)
	closeCon(conn)