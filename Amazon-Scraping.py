#!usr/bin/env python

import hmac, hashlib, base64

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

data = """http://webservices.amazon.com/onca/xml?AWSAccessKeyId=AKIAINYUQ3YAQIKQONCA&AssociateTag=saranyaraj432-20&Keywords=Microsoft&Operation=ItemSearch&ResponseGroup=Images%2CItemAttributes%2COffers&SearchIndex=Software&Service=AWSECommerceService&Timestamp=2017-07-11T04%3A35%3A51.000Z"""

print(AWSRequest.sign(data))

