#!usr/bin/env python

import hmac, hashlib, base64
from time import strftime, gmtime

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

#timestamp = strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())

data = """GET
webservices.amazon.com
/onca/xml
AWSAccessKeyId=AKIAINYUQ3YAQIKQONCA&AssociateTag=saranyaraj432-20&Keywords=Microsoft&Operation=ItemSearch&ResponseGroup=Images%2CItemAttributes%2COffers&SearchIndex=Software&Service=AWSECommerceService&Timestamp=2017-07-11T10%3A26%3A51.000Z"""

#print(timestamp.encode())
print(AWSRequest.sign(data))


