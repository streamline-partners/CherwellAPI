from CherwellAPI import CherwellClient
import pickle

#########################################################################################
# This example demonstrates how the Cherwell API Connection object can be used to
# retrieve the business object template for a Cherwell Business Object
###########################################################################################

#############################################
# Change the following to suit your instance
#############################################

base_uri = "http://192.168.224.15"
username = "CSDAdmin"
password = "CSDAdmin"
api_key = "c12a749a-7467-4979-beda-638f5735b685"

# Create a new cherwellclient connection - not passing in an existing cache object
cherwell_client = CherwellClient.Connection(base_uri, api_key, username, password)

# Show the summary for the incident object
print "Cherwell Template for Incident is:\n{}".format(
    cherwell_client.get_business_object_template("Incident")
)

