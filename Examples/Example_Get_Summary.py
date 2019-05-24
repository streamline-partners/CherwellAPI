from CherwellAPI import CherwellClient
import pickle

#########################################################################################
# This example demonstrates how the Cherwell API Connection object can be used to
# retrieve the business object summary for a Cherwell Business Object
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

# Show the summary for the incident object
print "Cherwell Summary for Incident is:\n{}".format(
    cherwell_client.get_business_object_summary("Incident")
)

