#####################################################################################
# Class that defines a Business Object - to be used to get new or existing business
# objects
#####################################################################################
import requests


class BusinessObject:

    """
        The BusinessObject class serves to simulate a Cherwell BusinessObject and removes
        the need to worry about Cherwell Business Object ID's and Field ID's. Its all taken care of automatically
        in this class.

        ----------
        ***NOTE***
        ----------
            This class should not be instantiated directly, but should be instantiated through the methods of the
            CherwellClient.Connection class

        Parameters
        ----------

        type_name : str

            The type_name refers to the Cherwell Business Object internalname that you wish to instantiate

        get_header_function : function

            The function to call when the authorisation token is needed for Cherwell. used for save and delete.

        save_uri : str

            The uri to use when attempting to save the BusinessObject

        delete_uri : str

            The uri to use when attempting to delete the BusinessObject

        busObId : str

            The Cherwell business object id, that relates to a Business Object in Cherwell

        busObRecId : str

            The Cherwell business object record id

        busObPublicId : str

            The Cherwell business object public id
        
        https_verify : bool

            Flag set to verify SSL Certificates during requests API Calls

        """

    def __init__(self, type_name, get_header_function, save_uri, delete_uri, busObID, busObRecId="", busObPublicId="", https_verify=False):

        self.type_name = type_name
        self.busObId = busObID
        self.busObPublicId = busObPublicId
        self.persist = True
        self.busobj_fields = []
        self.get_header = get_header_function
        self.save_uri = save_uri
        self.delete_uri = delete_uri
        self.busObRecId = busObRecId
        self.https_verify = https_verify
        self.has_Error = False
        self.error_Message = ""

    # Return whether we have an error or not
    def has_error(self):

        """ Returns true if the last call to Cherwell returned an error """

        return self.has_Error

    # return the current error message
    def error_message(self):

        """ Contains a description of an error that occured on the last call to Cherwell"""

        return self.error_Message

    # return the type name
    def get_type_name(self):

        """ Returns the 'Interalname' of the Cherwell business object"""

        return self.type_name

    # Return the business object id
    def busObId(self):

        """ Returns the Cherwell business object id"""

        return self.busObId

    # Return the public Id
    def busObPublicId(self):

        """ Returns the current Cherwell business object public id"""

        return self.busObPublicId

    # Return the loaded list of fields
    def fields(self):

        """ Returns the list of fields that have been populated in this BusinessObject"""

        return self.busobj_fields

    # return the business object record id
    def busObRecId(self):

        """ Returns the current Cherwell business object record id"""

        return self.busObRecId

    # Set the attributes dynamically for this object
    def __setattr__(self, key, value):

        """ Populates the attributes of this object instance, using the fields from the Business Object"""

        # Change the instance attribute
        self.__dict__[key] = value

    # Load the business object attributes from a passed in template
    def load(self, template):

        """ Loads the fields into this BusinessObject instance from a passed in template"""

        # Loop though the fields in the template and add them to the fields array
        for field in template["fields"]:
            self.busobj_fields.append(
                {"name": field["name"],
                 "displayName": field["displayName"],
                 "value": field["value"],
                 "html": field["html"],
                 "dirty": field["dirty"],
                 "fieldId": field["fieldId"]}
            )

            # Add the field names and values to instance attributes
            self.__dict__[field["name"]] = field["value"]

    def Save(self):

        """ Saves this BusinessObject back to Cherwell """

        # Loop through the fields originally loaded from the template
        # and find the instance attributes that have changed - setting them to dirty
        for field in self.busobj_fields:

            # Loop through the object attributes
            for instance_name in self.__dict__:

                if instance_name == field["name"] and self.__dict__[instance_name] != field["value"]:
                    # Instance attribute has been changed from original - set the dirty flag
                    field["dirty"] = True
                    field["value"] = self.__dict__[instance_name]

        # Build the payload for the save
        save_payload = {"Persist": True, "busObID": self.busObId, "busObPublicId": self.busObPublicId,
                        "busObRecId": self.busObRecId, "fields": self.busobj_fields}

        # Attempt to save the record
        result_save = requests.post(self.save_uri, json=save_payload, headers=self.get_header(),verify=self.https_verify)

        # Set the business object error states
        self.has_Error = result_save.json()["hasError"]
        self.error_Message = result_save.json()["errorMessage"]

        if result_save.status_code == 200:

            # Successfully saved the record
            self.busObPublicId = str(result_save.json()["busObPublicId"])
            self.busObRecId = str(result_save.json()["busObRecId"])
        else:
            # There was a problem with the API call, generate an exception
            raise Exception("Error saving business object '{}'. HTTP:{} '{}'".format(
                self.type_name,
                result_save.status_code,
                self.error_Message))

    # delete this record
    def Delete(self):

        """ Deletes this BusinessObject from the Cherwell Database """

        # Attempt to delete the current record if it has a busObId and busObRecId
        if self.busObId and self.busObRecId:

            # Create the the delete URL
            self.delete_uri = str(self.delete_uri).replace("[busobid]", self.busObId).replace("[busobrecid]", self.busObRecId)

            # Execute the delete
            result_delete = requests.delete(self.delete_uri, headers=self.get_header(),verify=self.https_verify)

            if result_delete.status_code == 200:

                # Successfully saved the record - remove the id's from this BusinessObject
                self.busObPublicId = ""
                self.busObRecId = ""

            else:

                # Set the business object error states
                self.has_Error = result_delete.json()["hasError"]
                self.error_Message = result_delete.json()["errorMessage"]

                # There was a problem with the API call, generate an exception
                raise Exception("Error deleting  business object '{}'. HTTP:{} '{}'".format(
                    self.type_name,
                    result_delete.status_code,
                    self.error_Message))

        else:

            # Raise an exception - record cannot be deleted without the record and object id
            raise ValueError("Record cannot be deleted as it has no active record id. busObRecId={}".format(self.busObRecId))


