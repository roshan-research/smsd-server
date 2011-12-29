import json, time, urllib2, urllib
from threading import Thread

deploy = False # True
if deploy:
	import android
	dr = android.Android()
	dr.makeToast('smsd is ready!')

def drSend(to, text):
	if deploy: dr.smsSend(to, text)

def drGetMessages():
	if deploy: return dr.smsGetMessages(True).result

def drMarkMessageRead(mark):
	if deploy: dr.smsMarkMessageRead(mark,True)

# config
pollInterval = 60 if deploy else 1
deviceInfo = {'name': 'htc-tatto', 'key': '2f1a5ee55fe8435b6aa82782d318f5e2'}
serverAddress = 'http://192.168.1.4:5000/' # 'http://50.56.222.11:5000/'
sending = True

def postData(address, data = False):
	post = deviceInfo
	if data: post.update(data)
	url = serverAddress + address

	try: return urllib2.urlopen(url, urllib.urlencode(post), 10).read()
	except Exception as e: print address, data, e
	return False

def applyCommand(cmd):
	if cmd == 'stop': sending = False
	elif cmd == 'start': sending = True

# threading
def tSender():
	while 1:
		time.sleep(pollInterval)
		if not sending: continue

		# download messages from server
		res = postData('get/')
		if not res: continue
		messages = json.loads(res)['messages']

		# send messages
		success = []
		for message in messages:
			print message['id'], message['to'], message['text'].encode("utf-8")
			drSend(message['to'], message['text'].encode("utf-8"))
			success.append(str(message['id']))

		# inform server
		if len(success) > 0:
			postData('success/', {'ids': (','.join(success))})

def tReceiver():
	while 1:
		time.sleep(1)

		received = drGetMessages()
		mark = []
		if received != None:
			for sms in received:
				number = sms['address'].strip()
				text = sms['body']
				mark.append(int(sms['_id']))
				cmd = postData('r/', {'from': number, 'text': text})
				if cmd: applyCommand(cmd)

			drMarkMessageRead(mark)
			
# start threads
sender = Thread(target=tSender); sender.start()
receiver = Thread(target=tReceiver); receiver.start()

# sleep main thread
while 1:
	time.sleep(600)