from CherwellAPI import CherwellClient
import pickle
from CherwellAPI import Filter

#########################################################################################
# This example demonstrates how the Cherwell API Connection object can be used to
# retrieve a Business Object and then delete it
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

# Create a new Adhoc filter object
search_filter = Filter.SimpleFilter("Incident")

# add a search filter where you are looking for a incident with a specific Id
# *** MODIFY the id to suit your instance - record must exist***
search_filter.add_search_fields("IncidentID", "eq", "102199")

# Pass the Adhoc filter object to the cherwellclient to retrieve the list of matching business objects
num_records, business_objects = cherwell_client.get_business_objects(search_filter)

# Print number of records returned
print "Number of records: {}".format(num_records)

# Loop through the records returned
index = 0
for business_object in business_objects:
    index = index + 1
    print "Record: {}".format(index)
    print "Public Record Id: {}".format(business_object.busObPublicId)
    print "Record Id: {}".format(business_object.busObRecId)

    # Now delete the record
    business_object.Delete()

    # Now show the attributes again
    print "Record: {}".format(index)
    print "Public Record Id: {}".format(business_object.busObPublicId)
    print "Record Id: {}".format(business_object.busObRecId)

