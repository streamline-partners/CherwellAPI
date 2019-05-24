from CherwellAPI import CherwellClient
import pickle
from CherwellAPI import Filter

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

# Create a new Adhoc filter object - passing True as the 2nd parameter will cause all fields to be returned
search_filter = Filter.AdHocFilter("CustomerInternal")

# add a search filter where you are looking for a customer called "John Allard"
search_filter.add_search_fields("FirstName", "contains", "Susan")

# Specify the fields you want returned
search_filter.add_fields("Email")
search_filter.add_fields("Phone")
search_filter.add_fields("FullName")

# Pass the Adhoc filter object to the cherwellclient
num_records, business_objects = cherwell_client.get_business_records(search_filter)

# Print number of records returned
print "Number of records: {}".format(num_records)

# Loop through the records returned
for business_object in business_objects:
    print business_object

