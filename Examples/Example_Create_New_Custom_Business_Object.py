# Import the Cherwell Client
from CherwellAPI import CherwellClient

#########################################################################################
# This example demonstrates how the Cherwell API Connection object can be used to
# create a custom object - Not OOTB
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

# Create an instance of the new custom object
new_object = cherwell_client.get_new_business_object("Federationregistration")

# print our record identifiers - before saving the new record
print "Business Object Record ID: {}".format(new_object.busObRecId)
print "Business Object Public ID: {}".format(new_object.busObPublicId)
print "Business Object ID: {}".format(new_object.busObId)

# Update required attributes
new_object.FederationName = "Fed100"
new_object.Description = "Fed 100 Object"
new_object.Status = "Inactive"

# Save the new record
new_object.Save()

# If there was an error - show the error
if new_object.has_error():
    print "\n***************************************"
    print "Business Object Has Error: {}".format(new_object.has_error)
    print "Business Object Error Message: {}".format(new_object.error_message)
    print "\n***************************************"
else:
    # print out record identifiers now that we have saved
    print("\n")
    print "Business Object Record ID: {}".format(new_object.busObRecId)
    print "Business Object Public ID: {}".format(new_object.busObPublicId)
    print "Business Object ID: {}".format(new_object.busObId)

    # Check if the user now wants to delete that record
    yesno = raw_input("Do you now want to delete this record (y/n)")
    if str(yesno).upper() == "Y":

        # If there was no error previously delete the record
        new_object.Delete()

        # If there was an error - show the error
        if new_object.has_error():
            print "\n***************************************"
            print "Business Object Has Error: {}".format(new_object.has_error)
            print "Business Object Error Message: {}".format(new_object.error_message)
            print "\n***************************************"



