#!usr/bin/env python

import hmac, hashlib, base64
import urllib, urllib2 
from time import strftime, gmtime
import collections

class AWSSigner:

	def __init__(self, secret_key):
		self.secret_key = secret_key

	#def sign(self, service, operation, timestamp):
	def sign(self, data):
		#h = hmac.new(self.secret_key, str(service) + str(operation) + str(timestamp), hashlib.sha256)
		h = hmac.new(self.secret_key, data, hashlib.sha256)
		digest = h.digest()
		return base64.b64encode(digest)

AWSRequest = AWSSigner('****')

timestamp = strftime("%Y-%m-%dT%H:%M:%S.000Z", gmtime())
data={}

data['AWSAccessKeyId']="*****"
data['AssociateTag']="saranyaraj432-20"
data['Keywords']="Thermostat"
data['Operation']="ItemSearch"
data['ResponseGroup']="Images,ItemAttributes,Offers"
data['SearchIndex']="Software"
data['Service']="AWSECommerceService"
data['Timestamp']= timestamp

od_data = collections.OrderedDict(sorted(data.items()))
url=urllib.urlencode(od_data)
#print(url)

url= "GET\nwebservices.amazon.com\n/onca/xml\n"+url

print(url)


data['Signature'] = AWSRequest.sign(url)
print(data['Signature'])

url=urllib.urlencode(data)
url= "http://webservices.amazon.com/onca/xml?"+url
print(url)


'''
openurl=urllib2.urlopen(url)
print(openurl.read())
'''
