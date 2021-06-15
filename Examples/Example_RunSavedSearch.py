from __future__ import print_function
from CherwellAPI import CherwellClient
from CherwellAPI import CherwellCredentials
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

# Pass the association, scope, saved search name to the CherwellClient's get_saved_search_results
num_records, business_objects = cherwell_client.get_saved_search_results("FederationRegistration","Global","All Active Federation Sources")

# Print number of records returned
print("Number of records: {}".format(num_records))

# Loop through the records returned
for business_object in business_objects:
    print(business_object)

