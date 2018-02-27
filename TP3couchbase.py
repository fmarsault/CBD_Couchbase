import uuid
import time
from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator
import couchbase.exceptions as cbexc

cluster = Cluster('couchbase://localhost')
authenticator = PasswordAuthenticator('Oursadmin','fitecours')
cluster.authenticate(authenticator)
cb = cluster.open_bucket('TPtest')

print(cb.get('key1').cas)
print(cb.get('key1').flags)

# cb.remove('key1')

cb.touch('key2', ttl=5)
cb.touch('key2', ttl=0)

cb.get

# try:
#     key = 'key1'
#     cb.insert(key, new_user)
# except cbexc.KeyExistsError:
#     print('Insert failed because the key already exists.')
#     cb.replace(key, new_user)
#     print(cb.get(key).value)