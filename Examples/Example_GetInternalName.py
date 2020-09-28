from __future__ import print_function
from CherwellAPI import CherwellClient
import pickle

#########################################################################################
# This example demonstrates how the CherwellAPI Connection object can be used to
# retrieve the business object template for a Cherwell Business Object
###########################################################################################

#############################################
# Change the following to suit your instance
#############################################
base_uri = "http://<Your Cherwell Host here>"
username = "<Your UserName Here>"
password = "<Your Password here>"
api_key = "<Your Cherwell REST API Client Key here>"

# Create a new CherwellClient connection
cherwell_client = CherwellClient.Connection(base_uri, api_key, username, password)

# Get the business object internal name - for the passed in business object id
print(cherwell_client.get_business_object_internalname("93ba37416cd565e13a2d2c4f2d8dcb287a17f7091f"))