import json, time, urllib2, urllib
from threading import Thread

deploy = True
if deploy:
	import android
	dr = android.Android()
	dr.makeToast('smsd is ready!')

def drSend(to, text):
	if deploy: dr.smsSend(to, text)
	print 'sms sent to %s' % to

def drGetMessages():
	if deploy: return dr.smsGetMessages(True).result

def drMarkMessageRead(mark):
	if deploy: dr.smsMarkMessageRead(mark,True)

# config
pollInterval = 2 if deploy else 1
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

		try:
			# download messages from server
			res = postData('get/')
			if not res: continue
			msgs = json.loads(res)['messages']

			# send messages
			success = []
			for message in msgs:
				drSend(message['to'], message['text'].encode("utf-8"))
				success.append(str(message['id']))
			msgs = []

			# inform server
			if len(success) > 0:
				postData('success/', {'ids': (','.join(success))})
		
		except Exception as e: print 'send error: ', e

def tReceiver():
	while 1:
		time.sleep(1)

		try:
			received = drGetMessages()
			mark = []
			if received != None:
				for sms in received:
					number = sms['address'].strip()
					text = sms['body'].encode("utf-8")
					mark.append(int(sms['_id']))
					cmd = postData('r/', {'from': number, 'text': text})
					if cmd: applyCommand(cmd)

				drMarkMessageRead(mark)

		except Exception as e: print 'receive error: ', e
			
# start threads
sender = Thread(target=tSender); sender.start()
receiver = Thread(target=tReceiver); receiver.start()

# sleep main thread
while 1:
	time.sleep(600)