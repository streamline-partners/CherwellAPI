from __future__ import print_function
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from CherwellAPI import CherwellClient
import pickle
from CherwellAPI import Filter

#########################################################################################
# This example demonstrates how the CherwellAPI Connection object can be used to
# search for and retrieve one or more business objects matching a search query
###########################################################################################

#############################################
# Change the following to suit your instance
#############################################

base_uri = "http://<Your Cherwell Host here>"
username = "<Your UserName Here>"
password = "<Your Password here>"
api_key = "<Your Cherwell REST API Client Key here>"

# Create a new Cherwellclient connection
cherwell_client = CherwellClient.Connection(base_uri, api_key, username, password)

# Create a new AdhocFilter object - (passing True as the 2nd parameter will cause all fields to be returned)
search_filter = Filter.AdHocFilter("CustomerInternal")

# add a search filter where you are looking for a specific customer
search_filter.add_search_fields("FirstName", "contains", "Susan")
search_filter.add_search_fields("FirstName", "contains", "Teri")

# Specify the fields you want returned - (We didn't pass True as 2nd parameter when initialising the AdHocFilter)
search_filter.add_fields("Email")
search_filter.add_fields("Phone")
search_filter.add_fields("FullName")

# Pass the AdhocFilter object to the CherwellClient's get_business_records
num_records, business_objects = cherwell_client.get_business_records(search_filter)

# Print number of records returned
print("Number of records: {}".format(num_records))

# Loop through the records returned
for business_object in business_objects:
    print(business_object)

