# import android
# dr = android.Android()
# dr.makeToast('Sender is ready!')

import thread, json, time, urllib2, urllib

key = '039c86abf0a5d67205d40d756eb0c9c5'
url = 'http://192.168.1.2:5000/get/'

def getMessages():
	data = {'name': 'htc-tatto', 'key': key}
	try:
		msg = urllib2.urlopen(url, urllib.urlencode(data)).read()
		return json.loads(msg)['messages']
	except Exception as e:
		print e
	return []

def sendMessages():
	messages = getMessages()
	for message in messages:
		print message['id'], message['to'], message['text'].encode("utf-8")
		dr.smsSend(message['to'], message['text'].encode("utf-8"))

	# todo: success

# threading
sending = True
def tSender():
	while 1:
		if sending:
			sendMessages()
		time.sleep(1)

def tReceiver():
	thread.exit()

thread.start_new_thread(tSender, ())
thread.start_new_thread(tReceiver, ())

# sleep main thread
while 1:
	time.sleep(1)