CherwellAPI is a suite of Python modules that abstract the Cherwell REST API and simplify the process of connecting to, and interacting with Cherwell business objects. 

Base Functionality Included
===========================

1. AdHoc searching
2. Creating new business objects
3. Updating existing business objects
4. Deleting existing business objects

The modules also cater for caching of commonly used items such as templates, summaries and business object id's as well as self-managing the expiry and refreshing of the Bearer token used for authorisation. Additionally Tokens can be cached and reused.

Instantiating a connection object
=================================

All interaction typically takes place through a **_Connection_** object which can be instantiated as follows:

```python
from CherwellAPI import CherwellClient
  
cherwell_client = CherwellClient.Connection(<base_uri>,<api_key>,<username>,<password>)  
```
*Replace the parameters between '<>' with appropriate values from your own Cherwell instance.*

Creating a new business object
==============================

A new Incident could be created as follows:

```python
from CherwellAPI import CherwellClient

# Create a new CherwellClient Connection
cherwell_client = CherwellClient.Connection(<base_uri>,<api_key>,<username>,<password>)

# Create a new instance of an Incident business object
Incident = cherwell_client.get_new_business_object("Incident")

# Set the properties of the new Incident
Incident.CustomerDisplayName = "John Allard"
Incident.Description = "This is a test Incident"
Incident.Priority = 5
Incident.Service = "IT Service Desk"
Incident.Category = "Report Outage or Error"
Incident.Subcategory = "Submit Incident"
Incident.Source = "Event"

# Save the new Incident
Incident.Save()

# Show the new business object record id
print "RecId for new Incident: {}".format(Incident.busObRecId)
print "PublicId for new Incident: {}".format(Incident.busObPublicId)

```
Output from executing the script above would likely looks as follows:

*RecId for new Incident: 944cccbc07cde32400bea6482a8c3dd1f36dc57d6b*

*PublicId for new Incident: 102401*

**Note:** *Depending on how your Cherwell instance is configured, you might need to supply more or less property values, or even different values*

Updating a business object
==========================

The following code snippet, show an example of how to get an instance of the Incident we created in the previous step and update it.

For this we need to import and use the **_SimpleFilter_** object, which we can populate with one or more filters to aid in searching.

```python

from CherwellAPI import CherwellClient
from CherwellAPI import Filter

# Create a new CherwellClient Connection
cherwell_client = CherwellClient.Connection(<base_uri>,<api_key>,<username>,<password>)

# Create a new SimpleFilter object instance,
# indicating the filter is applicable for the Cherwell 'Incident' business object
search_filter = Filter.SimpleFilter("Incident")

# Add some search filters - we are looking for the Incident created previously
search_filter.add_search_fields("IncidentID", "eq", "102401")
search_filter.add_search_fields("Status", "eq", "New")
search_filter.add_search_fields("Description", "contains", "test")

# Pass the Simple filter object to the CherwellClient - 'get_business_objects' method
# This method returns the number of matching business objects as well as the list of matching business objects
num_records, business_objects = cherwell_client.get_business_objects(search_filter)

# Print number of records returned
print "Number of records: {}".format(num_records)

# Loop through the records returned
index = 0
for business_object in business_objects:
    index = index + 1
    print "Record: {}".format(index)
    print "Public Record Id: {}".format(business_object.busObPublicId)
    print "Status: {}".format(business_object.Status)

    # Change the Incident description
    business_object.Description = "Updated the description"

    # Save the updated business object
    business_object.Save()

```

Deleting the previously created Incident
========================================

Deleting an object is just as easy, see below for an example of deleting the Incident record we updated in the previous step.

```python

from CherwellAPI import CherwellClient
from CherwellAPI import Filter

# Create a new CherwellClient Connection
cherwell_client = CherwellClient.Connection(<base_uri>,<api_key>,<username>,<password>)

# Create a new SimpleFilter object, indicating the filter is applicable for the Cherwell Incident business object
search_filter = Filter.SimpleFilter("Incident")

# add a search filter where we are looking for the Incident created previously
search_filter.add_search_fields("IncidentID", "eq", "102401")

# Pass the SimpleFilter object instance to the CherwellClient
# This method returns the number of matching business objects as well as the list of matching business objects
num_records, business_objects = cherwell_client.get_business_objects(search_filter)

if num_records == 1:

    # We should only have 1
    business_objects[0].Delete()

```

For more examples, refer to our GitHub project [here](https://github.com/streamline-partners/CherwellAPI/tree/master/Examples).

Full source code can be found [here](https://github.com/streamline-partners/CherwellAPI).

To find out more about Streamline Partners and how we could assist you with future projects, click [here](http://www.streamlinepartners.com.au/)

  




