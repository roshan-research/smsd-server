import android
dr = android.Android()
dr.makeToast('Sender is ready!')

import thread, json, time, urllib2, urllib

def server(address, data = False):
	post = {'name': 'htc-tatto', 'key': '039c86abf0a5d67205d40d756eb0c9c5'}
	if data:
		post.update(data)
	url = 'http://50.56.222.11:5000/' + address

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

# control
sending = True
admins = ['+989376970224', '+989128216439']
def applySms(number, text):
	global sending
	print number, text

	if number in admins:
		text = text.lower().strip()
		if text == 'start':
			sending = True
			print '>> Started'
		elif text == 'stop':
			sending = False
			print '>> Stopped'

# threading
def tSender():
	while 1:
		if sending:
			try: sendMessages()
			except Exception as e: print e
			
		time.sleep(60)

def tReceiver():
	while 1:
		messages = dr.smsGetMessages(True).result
		mark = []
		if messages != None:
			for message in messages:
				number = message['address'].strip()
				text = message['body']
				mark.append(int(message['_id']))
				applySms(number, text)

			dr.smsMarkMessageRead(mark,True)
			
		time.sleep(1)

# start threads
thread.start_new_thread(tSender, ())
thread.start_new_thread(tReceiver, ())

# sleep main thread
while 1:
	time.sleep(600)