# Copyright 2000 - 2015 NeuStar, Inc.All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
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