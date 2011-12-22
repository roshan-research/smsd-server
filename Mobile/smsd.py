import android
dr = android.Android()
dr.makeToast('Sender is ready!')

import thread, json, time, urllib2, urllib

def server(address, data = False):
	post = {'name': 'htc-tatto', 'key': '039c86abf0a5d67205d40d756eb0c9c5'}
	if False:
		post.update(data)
	url = 'http://192.168.1.2:5000/' + address
	return urllib2.urlopen(url, urllib.urlencode(post)).read();

def getMessages():
	try:
		msg = server('get/')
		return json.loads(msg)['messages']
	except Exception as e:
		print e
	return []

def sendMessages():
	# download messages from server
	messages = getMessages()

	# send messages
	success = []
	for message in messages:
		print message['id'], message['to'], message['text'].encode("utf-8")
		dr.smsSend(message['to'], message['text'].encode("utf-8"))
		success.append(str(message['id']))
	
	# inform server
	server('success/', {'ids': (','.join(success))})

# threading
sending = True
def tSender():
	while 1:
		if sending:
			sendMessages()
		time.sleep(1)

def tReceiver():
	thread.exit()

# start threads
thread.start_new_thread(tSender, ())
thread.start_new_thread(tReceiver, ())

# sleep main thread
while 1:
	time.sleep(1)