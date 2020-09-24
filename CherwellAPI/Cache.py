#####################################################################################
# Class that is used to cache various elements of an API Interaction
#####################################################################################

import json

class ObjectCache:

    """
    The ObjectCache class serves as an in memory cache of data that is often needed during Cherwell
    REST API interaction. This is data that changes infrequently and benefits can be had by caching it rather
    than fetching if whenever needed.

    The cache object is instantiated automatically and used by the CherwellAPI.CherwellClient.Connection class,
    but can be pickled to persistent storage and passed to subsequent instances of the CherwellClient class when its instantiated again.

    ----------
    ***NOTE***
    ----------
        This class should not be instantiated directly, but is instantiated by the
        CherwellAPI.CherwellClient.Connection class

    Parameters
    ----------

    base_uri : str

        The base uri of the Cherwell instance

    api_key : str

        The Cherwell REST API client key used for authorisation

    """

    def __init__(self, base_uri, api_key):

        # Start the cache
        self.cache = {}

        # add the base uri and other attributes
        self.cache["base_uri"] = base_uri
        self.cache["api_key"] = api_key

        # Add various uri's for accessing the api
        self.cache["uris"] = {
            "Token": "{0}/CherwellAPI/token?auth_type=Internal&api_key={1}".format(base_uri, api_key),
            "BusinessObjectID": "{0}/CherwellAPI/api/V1/getbusinessobjectsummary/busobname/".format(base_uri),
            "BusinessObjectTemplate": "{0}/CherwellAPI/api/V1/GetBusinessObjectTemplate/".format(base_uri),
            "BusinessObjectSummary": "{0}/CherwellAPI/api/V1/getbusinessobjectsummary/busobname/".format(base_uri),
            "BusinessObjectSave": "{0}/CherwellAPI/api/V1/SaveBusinessObject".format(base_uri),
            "BusinessSearchResults": "{0}/CherwellAPI/api/V1/getsearchresults".format(base_uri),
            "RunSavedSearch": "{0}/CherwellAPI/api/V1/getsearchresults/association/[association]/scope/[scope]/scopeowner/[scopeowner]/searchname/[searchname]?includeschema=[includeschema]&resultsAsSimpleResultsList=[resultsAsSimpleResultsList]".format(base_uri),
            "BusinessObjectDelete": "{0}/CherwellAPI/api/V1/deletebusinessobject/busobid/[busobid]/busobrecid/[busobrecid]".format(base_uri),
            "BusinessObjectSchema": "{0}/CherwellAPI/api/V1/getbusinessobjectschema/busobid/".format(base_uri),
            }

        # Setup the cache to hold business object id's
        self.cache["business_object_ids"] = {}

        # Setup the cache to hold business object templates
        self.cache["business_object_templates"] = {}

        # Setup the cache to hold summaries
        self.cache["business_object_summaries"] = {}

        # Setup the cache to hold schema's
        self.cache["business_object_schemas"] = {}

    def contents(self):

        """ Returns the content of the cache"""

        return self.cache

    def get_uri(self, name):

        """ Returns the cached Cherwell base uri"""

        return self.cache["uris"].get(name, None)

    def get_business_object_id(self, name):

        """

        Returns the cached Cherwell object id for a specific object or 'None' if not found

        Parameters:
        ----------

        name : str

            The name of the Business Object ID to get

        """

        return self.cache["business_object_ids"].get(name, None)

    def get_business_object_ids(self):

        """ Returns the list of cached Business Object Id's"""

        return json.dumps(self.cache["business_object_ids"])

    def set_uri(self, name, value):

        """

        Adds to the list of cached uri's

        Parameters:
        ----------

        name : str

            The descriptive name of the uri to save. Used for retrieving from the cache

        name : value

            The value to store as the uri

        """

        self.cache["uris"][name] = value

    def set_business_object_id(self, name, value):

        """

        Saves a new Business Object ID into cache

        Parameters:
        ----------

        name : str

            The name of the business object

        name : value

            The business object id

        """

        self.cache["business_object_ids"][name] = value

    def get_business_object_template(self,name):

        """ Returns a cached Business object template"""

        return self.cache["business_object_templates"].get(name, None)

    def set_business_object_template(self, name, value):

        """

        Saves a new Business Object template into cache

        Parameters:
        ----------

        name : str

            The name of the business object

        name : value

            The template to store in cache

        """

        self.cache["business_object_templates"][name] = value

    def get_business_object_summary(self,name):

        """ Returns a cached Business object summary"""

        return self.cache["business_object_summaries"].get(name, None)

    def set_business_object_summary(self, name, value):
        """

        Saves a new Business Object Summary into cache

        Parameters:
        ----------

        name : str

            The name of the business object

        name : value

            The business object sumamry to save into cache

        """

        self.cache["business_object_summaries"][name] = value

    def get_business_object_schema(self, business_object_id):

        """ Returns a cached Business object schema"""

        return self.cache["business_object_schemas"].get(business_object_id, None)

    def set_business_object_schema(self, business_object_id, value):
        """

        Saves a new Business Object Schema into cache

        Parameters:
        ----------

        business_object_id : str

            The id of the business object

        name : value

            The business object schema to save into cache

        """

        self.cache["business_object_schemas"][business_object_id] = value

    def __repr__(self):

        """ Returns a string representation of the cache"""

        return json.dumps(self.contents())
