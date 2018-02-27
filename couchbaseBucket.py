from couchbase.bucket import Bucket
from couchbase.cluster import PasswordAuthenticator

authenticator = PasswordAuthenticator('Oursadmin','fitecours')
bucket = Bucket('couchbase://localhost/TPtest').authenticate(authenticator)
print bucket