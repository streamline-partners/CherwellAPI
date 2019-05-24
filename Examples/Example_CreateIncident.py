from CherwellAPI import CherwellClient
import pickle

#########################################################################################
# This example demonstrates how the Cherwell API Connection object can be used to
# create a new business object
###########################################################################################

#############################################
# Change the following to suit your instance
#############################################

base_uri = "http://ec2-52-63-131-135.ap-southeast-2.compute.amazonaws.com"
username = "CSDAdmin"
password = "CSDAdmin"
api_key = "b24526ea-a86a-4eae-b3de-ec2107c4cfe9"

# Create a new cherwellclient connection - not passing in an existing cache object
cherwell_client = CherwellClient.Connection(base_uri, api_key, username, password)

# Get a template for a incident object
incident_template = cherwell_client.get_business_object_template("Incident")

# Update the necessary field values in the template - might need to modify these values to suit your instance
cherwell_client.set_business_object_field_value_in_template(incident_template, "CustomerDisplayName", "John Allard")
cherwell_client.set_business_object_field_value_in_template(incident_template, "Description", "This is a test incident")
cherwell_client.set_business_object_field_value_in_template(incident_template, "Customer ID", "9365dad2de6bb99d1639784ab8a566c5a31f46d243")
cherwell_client.set_business_object_field_value_in_template(incident_template, "CustomerTypeID", "93405caa107c376a2bd15c4c8885a900be316f3a72")
cherwell_client.set_business_object_field_value_in_template(incident_template, "Priority", "1")
cherwell_client.set_business_object_field_value_in_template(incident_template, "Service", "IT Service Desk")
cherwell_client.set_business_object_field_value_in_template(incident_template, "Category", "Report Outage or Error")
cherwell_client.set_business_object_field_value_in_template(incident_template, "SubCategory", "Submit Incident")
cherwell_client.set_business_object_field_value_in_template(incident_template, "CallSource", "Event")

# Save the new incident
new_inc_public_id, new_inc_rec_id, business_object_id = cherwell_client.create_business_object(incident_template, "incident")

# Show the new id
print "New incident public id is: {}".format(new_inc_public_id)
print "New incident record id is: {}".format(new_inc_rec_id)
print "Business Object ID is: {}".format(business_object_id)






