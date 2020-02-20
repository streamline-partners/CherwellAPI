#####################################################################################
# Class that is used to create a filter to search for objects
#####################################################################################


class Filter(object):

    """
    The Filter class serves as object filter when searching for Cherwell business objects.

    ----------
    ***NOTE***
    ----------
        This class should not be instantiated directly, but rather the subclasses of 'SimpleFilter'
        and 'AdHocFilter' should be used instead

    Parameters
    ----------

    business_object_name : str

        The name of the Cherwell business object that will be searched with this filter

    include_all_fields : bool

        Whether any searches should return all fields, or only the ones specified in the filter

    """

    def __init__(self, business_object_name, include_all_fields=False):

        # Save the business object name
        self.business_object_name = business_object_name

        # Create a list to store the search fields
        self.search_fields = []

        # Set the value for search all fields - defaults to True for this type of Filter
        self.include_all_fields = include_all_fields

    def add_search_fields(self, field_name, operator, value):

        """
        This method adds field to the search filter, thus limiting the search.

        Parameters
        ----------

        field_name : str

            The name of the field to search

        operator : str

            The operator to use for comparison

            Valid values are:
            -- 'eq' for equal to
            -- 'gt' for greater than
            -- 'lt' for less than
            -- 'contains' for a like comparison to see if the field contains that value
            -- 'startswith' to check if the fields starts with the supplied value

        value : str

            The value to search for in the 'field_name' using the comparison 'operator'

        """

        if operator not in ["eq", "gt", "lt", "contains", "startswith"]:

            # Not a valid operator - generate an exception
            raise Exception("Not a valid search operator:\nValid values are 'eq','gt','lt','contains','startswith'")

        self.search_fields.append(
            {
                "Field": field_name,
                "Operator": operator,
                "Value": value
            }
        )

    def search_fields(self):

        """ Returns the list of search fields that have been configured/added"""

        return self.search_fields

    def include_all_fields(self):

        """ Returns true to return all fields, or false if the search is to be restricted by a field filter i.e.
        return only certain fields"""

        return self.include_all_fields

    def business_object_name(self):

        """ Returns the cherwell business object name configured in this search filter"""

        return self.business_object_name()


class SimpleFilter(Filter):

    """
    Subclass of the 'Filter' class which serves as a search filter to be passed to:

     -- The 'get_business_records' method of the CherwellAPI.CherwellClient.Connection class

    ----------
    ***NOTE***
    ----------

    This class allows for the adding of a 'fields' filter that allows only certain fields to be returned in a search

    Parameters
    ----------

    business_object_name : str

        The name of the Cherwell business object that will be searched with this filter

    """

    def __init__(self, business_object_name):

        # Call the Super Class initialisation
        Filter.__init__(self, business_object_name)

        # Set the value for search all fields - defaults to True for this type of Filter
        self.include_all_fields = True


class AdHocFilter(Filter):

    """
    Subclass of the 'Filter' class which serves as a search filter to be passed to:

     -- The 'get_business_objects' method of the CherwellAPI.CherwellClient.Connection class

    ----------
    ***NOTE***
    ----------

    This class forces the setting of 'include_all_fields' = 'True'

    Parameters
    ----------

    business_object_name : str

        The name of the Cherwell business object that will be searched with this filter

    include_all_fields : bool

        Whether any searches should return all fields, or only the ones specified in the filter

    """

    def __init__(self, business_object_name, include_all_fields=False):

        # Call the Super Class initialisation
        Filter.__init__(self, business_object_name, include_all_fields)

        # Create a list to store the fields to be returned
        self.fields = []

    def add_fields(self, field_name):

        """
        This method adds field to the list of fields to be returned

        Parameters
        ----------

        field_name : str

            The name of the field to add to the list, if 'include_all_fields' is set to 'False', then only the fields
            in this list will be returned

        """

        # Make sure we don't have duplicates
        if field_name not in self.fields:
            self.fields.append(field_name)

    def fields(self):

        """
        Returns the list of fields that will be returned by the search filter
        if 'include_all_fields' is set to 'False'
        """

        return self.fields
