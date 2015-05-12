# Copyright 2000 - 2015 NeuStar, Inc.All rights reserved.
# NeuStar, the Neustar logo and related names and logos are registered
# trademarks, service marks or tradenames of NeuStar, Inc. All other
# product names, company names, marks, logos and symbols may be trademarks
# of their respective owners.
import json

class InstantTest:
    def __init__(self, connection, id):
        self.connection = connection
        self.id = id
        self.service = "/tools/instanttest/1.0"
        
    def create(self, url, callback=None):
        """Creates a new instant test job and return the job id of the new instant test job. Url is required. 
        You may optionally supply a callback URL. For every stage of the instant test process, we will 
        POST the current status of your instant test job.
        
        Arguments:
        url -- The url to test.
        callback -- A callback url to post the results to.
        
        """
        new_test = {"url": url}
        if callback is not None:
            new_test.update({"callback": callback})
        return self.connection.post(self.service, json.dumps(new_test))
        
    def get(self):
        """Retrieves information for a specific instant test job, along with information from each location 
        being tested."""
        if self.id is None:
            raise Exception("Missing id: This API requires an instant test ID be supplied.")
        return self.connection.get(self.service + "/" + self.id)
        
    def get_by_location(self, location):
        """Retrieves information for a specific instant test job by location.
        
        Arguments:
        location -- Location to query.
        
        """
        if self.id is None:
            raise Exception("Missing id: This API requires an instant test ID be supplied.")
        return self.connection.get(self.service + "/" + self.id + "/" + location)