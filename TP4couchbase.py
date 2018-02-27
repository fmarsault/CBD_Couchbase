import uuid
import time
from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator
import couchbase.exceptions as cbexc

cluster = Cluster('couchbase://localhost')
authenticator = PasswordAuthenticator('Oursadmin','fitecours')
cluster.authenticate(authenticator)
cb = cluster.open_bucket('travel-sample')

keys = map(lambda x:'airline_'+str(x),[10,10123,10226,10642,10748,10765,109,112,1191,1203])
# i = 0
# a = {}
# for key in keys:
#     a[i] = cb.get(key).value
#     print(cb.get(key).value)
#     i += 1

multi = cb.get_multi(keys)
print(multi)