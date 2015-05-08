# Copyright 2000 - 2013 NeuStar, Inc.All rights reserved.
# NeuStar, the Neustar logo and related names and logos are registered
# trademarks, service marks or tradenames of NeuStar, Inc. All other
# product names, company names, marks, logos and symbols may be trademarks
# of their respective owners.

class Load:
    def __init__(self, connection, id):
        self.connection = connection
        self.id = id
        self.service = "/load/1.0"
        
    def who_am_i(self):
        """Retrieves the username associated with the credentials used to issue the API call."""
        return self.connection.get(self.service + "/whoami")