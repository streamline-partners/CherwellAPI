from __future__ import print_function
from CherwellAPI import CherwellClient
from CherwellAPI import Filter

#########################################################################################
# This example demonstrates how the CherwellAPI Connection object can be used to
# retrieve the business object summary for a Cherwell Business Object
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

# Create a new Simple filter object
search_filter = Filter.SimpleFilter("CustomerInternal")

# add a search filter where you are looking for a customer
search_filter.add_search_fields("FirstName", "contains", "Susan")

# Pass the SimpleFilter object to the CherwellClient's get_business_objects method
# to retrieve the list of matching business objects
num_records, business_objects = cherwell_client.get_business_objects(search_filter)

# Print number of records returned
print("Number of records: {}".format(num_records))

# Loop through the records returned
index = 0
for business_object in business_objects:
    index = index + 1
    print("Record: {}".format(index))
    print("Public Record Id: {}".format(business_object.busObPublicId))
    print("Status: {}".format(business_object.Status))
