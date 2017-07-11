#!usr/bin/env python

import hmac, sha, base64

class AWSSigner:

	def __init__(self, secret_key):
		self.secret_key = secret_key

	def sign(self, service, operation, timestamp):
		h = hmac.new(self.secret_key, str(service) + str(operation) + str(timestamp), sha)
		digest = h.digest()
		return base64.b64encode(digest)

AWSRequest = AWSSigner('QcfpCpzijMjttVfdwcokL2Q5NcDWpZRRShHP0KgL')

print(AWSRequest.sign("AWSECommerceService", "ItemSearch", "2017-07-11T04:35:51.000Z"))

