# Copyright 2000 - 2015 NeuStar, Inc.All rights reserved.
# NeuStar, the Neustar logo and related names and logos are registered
# trademarks, service marks or tradenames of NeuStar, Inc. All other
# product names, company names, marks, logos and symbols may be trademarks
# of their respective owners.
import json

class Script:
    def __init__(self, connection, id):
        self.connection = connection
        self.id = id
        self.service = "/script/1.0"
        
    def endpoint(self, url):
        """Creates a single-step test script that opens a browser and loads to the given URL."""
        new_script = {"url": url}
        return self.connection.post(self.service + "/url", json.dumps(new_script))
        
    def list(self):
        """Retrieves a list of valid scripts."""
        return self.connection.get(self.service)