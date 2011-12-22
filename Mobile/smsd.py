import android
dr = android.Android()
dr.makeToast('Sender is ready!')

import thread, json, time, urllib2

key = '039c86abf0a5d67205d40d756eb0c9c5'
url = 'http://emenbar.ir/files/messages.json'

def getMessages():
	msg = urllib2.urlopen(url).read()
	return json.loads(msg)['messages']

def sendMessages():
	messages = getMessages()
	for message in messages:
		print message['id'], message['to'], message['text'].encode("utf-8")
		dr.smsSend(message['to'], message['text'].encode("utf-8"))

sendMessages()