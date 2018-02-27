import uuid
import time
from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator
import couchbase.exceptions as cbexc

cluster = Cluster('couchbase://localhost')
authenticator = PasswordAuthenticator('Oursadmin','fitecours')
cluster.authenticate(authenticator)
cb = cluster.open_bucket('TPtest')

new_user = {
    'name': 'Arthur', 'email': 'kingarthur@couchbase.com', 'interests':
        ['Holy Grail', 'African Swallows'], 'type': 'user'
}
new_user2 = {
    'name': 'Karadoc', 'email': 'karadoc@couchbase.com', 'interests':
        ['Food', 'Chicken'], 'type': 'user'
}

try:
    key = 'key1'
    cb.insert(key, new_user)
except cbexc.KeyExistsError:
    print('Insert failed because the key already exists.')
    cb.replace(key, new_user)
    print(cb.get(key).value)

cb.upsert('key2',new_user2, ttl=8)
time.sleep(5)
print(cb.get('key2').value)
cb.touch('key2', ttl=0)
time.sleep(5)
try:
    print(cb.get('key2').value)
except cbexc.NotFoundError:
    print('The requested key is not present in the DB.')
