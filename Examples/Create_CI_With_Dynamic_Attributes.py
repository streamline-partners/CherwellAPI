from __future__ import print_function
from CherwellAPI import CherwellClient
from CherwellAPI import Filter

#########################################################################################
# This example demonstrates how the CherwellAPI Connection object can be used to
# create a new business object
###########################################################################################

# Function to search for a specific CI - return the RecID if found
def find_ci(ci_type, search_attributes, cherwell_client):

    search_filter = Filter.SimpleFilter(ci_type)

    for search_key in search_attributes:

        # Add the attributes to search with
        print(search_key + search_attributes[search_key])
        search_filter.add_search_fields(search_key, "eq", search_attributes[search_key])

    # Perform the search
    num_records, business_objects = cherwell_client.get_business_objects(search_filter)

    print("Records: {}".format(num_records))

    if num_records > 0:
       # return business_objects[0]["fields"][0]["value"]
        return business_objects[0].RecID
    else:
        return None

#############################################
# Change the following to suit your instance
#############################################

base_uri = "http://<Your Cherwell Host here>"
username = "<Your UserName Here>"
password = "<Your Password here>"
api_key = "<Your Cherwell REST API Client Key here>"

# Create a set of attributes to use to add/update the CI
ci_attributes = {
    "FriendlyName" : "Bob",
    "IPAddress" : "127.0.0.1"
}

# Create a set of attributes to search for a CI
ci_search = {
    "FriendlyName" : "Bob",
    "IPAddress" : "127.0.0.1"
}

# Create a new CherwellClient connection
cherwell_client = CherwellClient.Connection(base_uri, api_key, username, password)

# Check if a CI already exists
rec_id = find_ci("ConfigNetworkDevice", ci_search, cherwell_client)

print(rec_id)

if rec_id is None:


    print("Not Found - Creating")

    # Get a new business object
    ci_computer = cherwell_client.get_new_business_object("ConfigNetworkDevice")

    # add the attributes
    for key in ci_attributes:
        setattr(ci_computer, key, ci_attributes[key])

    #Save the new record
    ci_computer.Save()

else:

    print("Found - RecID: {}".format(rec_id))
