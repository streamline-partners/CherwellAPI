from CherwellAPI import CherwellClient
import pickle

#########################################################################################
# This example demonstrates the use of the cache object used with the CherwellClient
# Caching is performed for
# 1) Business Object IDs
# 2) URI's
# 3) Business Object Templates
# 4) Business object summaries
# Once an item in in cache, its retrieved there first rather than making another REST Call
###########################################################################################

#############################################
# Change the following to suit your instance
#############################################

base_uri = "http://<Your Cherwell Host here>"
username = "<Your UserName Here>"
password = "<Your Password here>"
api_key = "<Your Cherwell REST API Client Key here>"

# Create a new cherwellclient connection - not passing in an existing cache object
cherwell_client = CherwellClient.Connection(base_uri, api_key, username, password)

# Show the current cache - should have some URI's
print "Current Cache is: {}\n".format(cherwell_client.cache)

# Show the currently cached business object ids - should be a few or none
print "Current Business IDS Cached are: {}\n".format(cherwell_client.cache.get_business_object_ids())

# add to the cache by getting some BusinessObjectId's
cherwell_client.get_business_object_id("Incident")
cherwell_client.get_business_object_id("Problem")
cherwell_client.get_business_object_id("ChangeRequest")

# Show the currently cached business object ids - should now have the ones retrieved above
print "Current Business IDS Cached are: {}\n".format(cherwell_client.cache.get_business_object_ids())

# Save the cache object to disk as a cache
pickle.dump(cherwell_client.cache, open("cache.pic","wb"))

# Retrieve the cache object from disk
cache_new = pickle.load(open("cache.pic","rb"))

# Print the contents of the saved cache
print "Cache object which was saved to disk: {}\n".format(cache_new)

# Create a new Cherwell client passing in the previously saved cache object
cherwell_client_new = CherwellClient.Connection(base_uri, api_key, username, password,cache_new)

# Show the current cache business object ids
# Should now already be starting with Incident, Problem, ChangeRequest
print "Current Business IDS Cached are: {}\n".format(cherwell_client_new.cache.get_business_object_ids())








