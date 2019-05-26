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

# Show the template for the incident object
print("Cherwell Template for Incident is:\n{}".format(
    cherwell_client.get_business_object_template("Incident")
))

