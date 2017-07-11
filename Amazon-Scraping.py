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

AWSRequest = AWSSigner('QcfpCpzijMjttVfdwcokL2Q5NcDWpZRRShHP0KgL')


# data = """GET
# webservices.amazon.com
# /onca/xml
# AWSAccessKeyId=AKIAINYUQ3YAQIKQONCA&AssociateTag=saranyaraj432-20&Keywords=Microsoft&Operation=ItemSearch&ResponseGroup=Images%2CItemAttributes%2COffers&SearchIndex=Software&Service=AWSECommerceService&Timestamp=2017-07-11T12%3A15%3A51.000Z"""

# print(AWSRequest.sign(data))


timestamp = strftime("%Y-%m-%dT%H:%M:%S.000Z", gmtime())
data={}

data['AWSAccessKeyId']="AKIAINYUQ3YAQIKQONCA"
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
