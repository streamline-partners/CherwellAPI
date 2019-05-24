from __future__ import print_function
from CherwellAPI import CherwellClient
import pickle
import time

#########################################################################################
# This example demonstrates the use of the REST API token that's retrieved from the Cherwell
# Server. The token contains a bearer token code once authenticated, and this is used in all
# subsequent REST API calls. This code also demonstrates that the token can be cached
# and reused if not expired.
###########################################################################################

from datetime import datetime
import time

def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset

#############################################
# Change the following to suit your instance
#############################################

base_uri = "http://192.168.224.15"
username = "CSDAdmin"
password = "CSDAdmin"
api_key = "c12a749a-7467-4979-beda-638f5735b685"

# Create a new cherwellclient connection - not passing in an existing token object
cherwell_client = CherwellClient.Connection(base_uri, api_key, username, password)

# Show the current token
print("Current Token is: {}\n".format(cherwell_client.token))

# The token is only retrieved when a api call is made for the first time,
# to do so - get an existing Business Object ID - assuming here its not already cached
print("Incident Business Object Id is: {}".format(cherwell_client.get_business_object_id("Incident2")))

# Show the current token - if authenticated, should now have a value
print("Token is now: {}\n".format(cherwell_client.token))

# Check whether the token is expired or not
print("Current Token Expiry time in GMT is: {}".format(cherwell_client.token.token_expiry_gmt()))
print("Current Local GMT Time is: {}".format(cherwell_client.token.current_time_gmt()))
print("Current Token is Expired: {}".format(cherwell_client.token.expired()))

# Sleep until the token has expired - (Tip: set the token value in Cherwell to a couple of mins or less)
while not cherwell_client.token.expired():
    time.sleep(5)
    print("#", end="")

# Retrieve another BusinessObject ID with an expired token
print("Change Request Business Object Id is: {}".format(cherwell_client.get_business_object_id("ChangeRequest")))

# Check the token details again - the CherwellClient Connection should take care of getting a new token
print("Current Token Expiry time in GMT is: {}".format(cherwell_client.token.token_expiry_gmt()))
print("Current Local GMT Time is: {}".format(cherwell_client.token.current_time_gmt()))
print("Current Token is Expired: {}".format(cherwell_client.token.expired()))

# Save the current token to disk
print("Saving Token - caching")
pickle.dump(cherwell_client.token,open("token_cached.pic", "wb"))

# Get the token back from disk
print("Retrieving Token from cache")
saved_token = pickle.load(open("token_cached.pic", "rb"))

# Create a new cherwell client passing in the saved token - so it doesn't need to create a new one
new_cherwell_client = cherwell_client = CherwellClient.Connection(base_uri, api_key, username, password, token=saved_token)

# Retrieve another BusinessObject ID with this cached token
print("Problem Business Object Id is: {}".format(cherwell_client.get_business_object_id("Problem")))

# Compare the values from the previous token to this one - should be same
print("\nCached Token Expiry time in GMT is: {}".format(new_cherwell_client.token.token_expiry_gmt()))
print("Cached Local GMT Time is: {}".format(new_cherwell_client.token.current_time_gmt()))
print("Cached Token is Expired: {}".format(new_cherwell_client.token.expired()))



