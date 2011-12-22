import android
dr = android.Android()
dr.makeToast('Sender is ready!')

import thread, json, time, urllib2, urllib

def server(address, data = False):
	post = {'name': 'htc-tatto', 'key': '039c86abf0a5d67205d40d756eb0c9c5'}
	if data:
		post.update(data)
	url = 'http://192.168.1.2:5000/' + address

	try: return urllib2.urlopen(url, urllib.urlencode(post)).read()
	except Exception as e: print e
	return False;

def sendMessages():
	# download messages from server
	res = server('get/')
	if not res: return False
	messages = json.loads(res)['messages']

	# send messages
	success = []
	for message in messages:
		print message['id'], message['to'], message['text'].encode("utf-8")
		dr.smsSend(message['to'], message['text'].encode("utf-8"))
		success.append(str(message['id']))
	
	# inform server
	if len(success) > 0:
		server('success/', {'ids': (','.join(success))})

# threading
sending = True
def tSender():
	while 1:
		if sending:
			try: sendMessages()
			except Exception as e: print e
			
		time.sleep(1)

def tReceiver():
	thread.exit()

# start threads
thread.start_new_thread(tSender, ())
thread.start_new_thread(tReceiver, ())

# sleep main thread
while 1:
	time.sleep(600)