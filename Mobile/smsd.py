import android
dr = android.Android()
dr.makeToast('Sender is ready!')

import thread, json, time, urllib2

key = '039c86abf0a5d67205d40d756eb0c9c5'
url = 'http://192.168.1.2:5000/get/'

def getMessages():
	msg = urllib2.urlopen(url, {'name': 'htc-tatto', 'key': key}).read()
	return json.loads(msg)['messages']

def sendMessages():
	messages = getMessages()
	for message in messages:
		print message['id'], message['to'], message['text'].encode("utf-8")
		dr.smsSend(message['to'], message['text'].encode("utf-8"))

sendMessages()