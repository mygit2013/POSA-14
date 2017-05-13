#!/usr/bin/python3
import http.client
import urllib.request
import urllib.parse
import json
import time
 
api_url = "http://api.carriots.com/streams"
device="defaultDevice@JCarriot.JCarriot"
api_key = "11a793435d0a8b061e829ddb3b23edda3facce13c57ded5dfcf8d23999530461" # Poner la apikey



#apikey stream 11a793435d0a8b061e829ddb3b23edda3facce13c57ded5dfcf8d23999530461
#apikeyreadonly 2447585f28859ba6ce342682d1d25d686322df6d41849c26787950da6e850aef
 #Automatic apikey full 27817cfff89c3e1e49c4a130e22a983bf56692ff0229527b88d450af1ed09133




 
#Parameters - Body
timestamp = int(time.time())
params = {"protocol": "v2",
   "device": device,
   "at": timestamp,
	"data":dict(
		"hum": "58",
		"temp": "21")}

# Reverse order, to get newest first
binary_data = json.dumps(params).encode('ascii')

# Header
header = {"User-Agent": "raspberrycarriots",
				 "Content-Type": "appllication/json",
				 "carriots.apikey": api_key}

# Request
req = urllib.request.Request(api_url,binary_data,header)
f = urllib.request.urlopen(req)

# Print response
#print(f.read().decode('utf-8'))

# Print in a pretty way
data=json.loads(f.read().decode('utf-8'))
print(json.dumps(data,indent=4,sort_keys=True))
