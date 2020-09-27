from __future__ import print_function
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
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

base_uri = "http://ec2-3-104-173-24.ap-southeast-2.compute.amazonaws.com"
username = "SL1"
password = "Password123"
api_key = "2940baca-1e3a-4f5e-863a-a4e2370a8633"

#Create Encrypted Credentials
# CherwellCredentials.create_encrypted_cherwell_credentials(password,api_key)

# Create a new Cherwellclient connection
cherwell_client = CherwellClient.Connection(base_uri=base_uri, username=username)

# Pass the AdhocFilter object to the CherwellClient's get_business_records
num_records, business_objects = cherwell_client.get_saved_search_results("FederationRegistration","Global","All Active Federation Sources")

# Print number of records returned
print("Number of records: {}".format(num_records))

# Loop through the records returned
for business_object in business_objects:
    print(business_object)

