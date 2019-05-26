from __future__ import print_function
# Import the Cherwell Client
from CherwellAPI import CherwellClient


#########################################################################################
# This example demonstrates how the CherwellAPI Connection object can be used to
# create a custom object
###########################################################################################

#############################################
# Change the following to suit your instance
#############################################

base_uri = "http://<Your Cherwell Host here>"
username = "<Your UserName Here>"
password = "<Your Password here>"
api_key = "<Your Cherwell REST API Client Key here>"

# Create a new Cherwellclient connection
cherwell_client = CherwellClient.Connection(base_uri, api_key, username, password)

# Create an instance of the new custom object - modify as needed to your instance
new_object = cherwell_client.get_new_business_object("Federationregistration")

# Print out record identifiers - modify as needed to your instance
print("Business Object Record ID: {}".format(new_object.busObRecId))
print("Business Object Public ID: {}".format(new_object.busObPublicId))
print("Business Object ID: {}".format(new_object.busObId))

# Update required attributes - modify as needed to your instance
new_object.FederationName = "Fed200"
new_object.Description = "Fed 200 Object"
new_object.Status = "Inactive"

# Save the new record
new_object.Save()

# If there was an error - show the error
if new_object.has_error():
    print("\n***************************************")
    print("Business Object Has Error: {}".format(new_object.has_error))
    print("Business Object Error Message: {}".format(new_object.error_message))
    print("\n***************************************")
else:
    # Print out record identifiers now that we have saved
    print("\n")
    print("Business Object Record ID: {}".format(new_object.busObRecId))
    print("Business Object Public ID: {}".format(new_object.busObPublicId))
    print("Business Object ID: {}".format(new_object.busObId))

    # Check if the user now wants to delete that record
    yesno = input("Do you now want to delete this record (y/n)")
    if str(yesno).upper() == "Y":

        # If there was no error previously delete the record
        new_object.Delete()

        # If there was an error - show the error
        if new_object.has_error():
            print("\n***************************************")
            print("Business Object Has Error: {}".format(new_object.has_error))
            print("Business Object Error Message: {}".format(new_object.error_message))
            print("\n***************************************")
