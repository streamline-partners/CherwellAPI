name = "CherwellAPI"

"""
The 'CherwellAPI Package' can be used as a wrapper around the Cherwell REST API to interact 
with Business Objects in a Cherwell instance. 

Usage:
------

Create an instance of the CherwellClient and interact with the Cherwell REST API using its methods:

    Example - how to create an instance of the Cherwell Client
    ----------------------------------------------------------
    
    # Import the Cherwell Client
    from CherwellAPI import CherwellClient
    
    #############################################
    # Change the following to suit your instance
    #############################################

    base_uri = "http://192.168.224.15"
    username = "CSDAdmin"
    password = "CSDAdmin"
    api_key = "c12a749a-7467-4979-beda-638f5735b685"

    # Create a new cherwellclient connection
    cherwell_client = CherwellClient.Connection(base_uri, api_key, username, password)
    
"""






