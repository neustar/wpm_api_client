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
import urllib, json

class Load:
    def __init__(self, connection, id):
        self.connection = connection
        self.id = str(id)
        self.service = "/load/1.0"
        
    def echo(self, msg):
        """Echos a message back to the API caller.
        
        Arguments:
        msg -- The message to echo.
        
        """
        # Automatically encode the msg string to be used in a url.
        msg = urllib.quote_plus(msg)
        return self.connection.get(self.service + "/echo/" + msg)
        
    def who_am_i(self):
        """Retrieves the username associated with the credentials used to issue the API call."""
        return self.connection.get(self.service + "/whoami")
        
    def list_most_recent_jsonp(self, limit, callback):
        """Retrieves a list of recent load tests ordered by date in descending order.
        
        Arguments:
        limit -- The maximum number of load tests to retrieve.
        callback -- The name of a javascript function to be called when the JSONP result is received
        
        """
        params = {"limit": limit, "callback": callback}
        return self.connection.get(self.service + "/list/mostRecent", params)
        
    def list(self, limit):
        """Retrieves a list of recent load tests ordered by date in descending order.
        
        Arguments:
        limit -- The maximum number of load tests to retrieve.
        
        """
        params = {"limit": limit}
        return self.connection.get(self.service + "/list", params)
        
    def add_tag(self, tag_name):
        """Add a name tag to a load test.
        
        Arguments:
        tag_name -- The name tag to be added.
        
        """
        if self.id is None:
            raise Exception("Missing id: This API requires a load test ID be supplied.")
        tag_name = urllib.quote_plus(tag_name)
        return self.connection.put(self.service + "/" + self.id + "/tag/" + tag_name)
        
    def remove_tag(self, tag_name):
        """Remove a name tag from a load test.
        
        Arguments:
        tag_name -- The name tag to be added.
        
        """
        if self.id is None:
            raise Exception("Missing id: This API requires a load test ID be supplied.")
        tag_name = urllib.quote_plus(tag_name)
        return self.connection.delete(self.service + "/" + self.id + "/tag/" + tag_name)
        
    def get(self):
        """Get a load test by its ID."""
        if self.id is None:
            raise Exception("Missing id: This API requires a load test ID be supplied.")
        return self.connection.get(self.service + "/id/" + self.id)
        
    def delete(self):
        """Delete a load test."""
        if self.id is None:
            raise Exception("Missing id: This API requires a load test ID be supplied.")
        return self.connection.delete(self.service + "/" + self.id + "/delete")
        
    def pause(self):
        """Pause a running load test."""
        if self.id is None:
            raise Exception("Missing id: This API requires a load test ID be supplied.")
        return self.connection.put(self.service + "/" + self.id + "/pause")
        
    def resume(self):
        """Pause a running load test."""
        if self.id is None:
            raise Exception("Missing id: This API requires a load test ID be supplied.")
        return self.connection.put(self.service + "/" + self.id + "/resume")
        
    def schedule(self, name, region, start, scripts, parts, override=None):
        """Schedule a load test.
        
        Arguments:
        name -- The name of the load test.
        region -- The geographic region where the source of load test traffic will originate from.
                        US_WEST
                        US_EAST
                        EU_WEST
                        AP_SOUTHEAST
                        AP_NORTHEAST
                        SA_EAST
        start -- The date and time when the load test should begin. If this property is not specified, 
                   then the load test will be scheduled to start in about 10 minutes. The start date 
                   must be at least 10 minutes in the future.
        scripts -- An array of scripts that will be executed through the load test. A script object looks 
                      as follows: 
                      
                          { "percentage" : int, "scriptId" : string }
                          
        parts -- The load test plan (represents the number of users in the load test over time). An 
                   array of part objects where each part looks as follows:
                   
                       { "duration" : int, "maxUsers" : int, "type" : string }
                   
                   Duration represents number of minutes, maxUsers is the maximum number of users 
                   that will execute during this part of the test plan, type is either RAMP (linear increase 
                   in number of users over the duration) or CONSTANT (flat).
        override -- The override code that alters the behaviour of the load test. Neustar may provide you 
                       with a specific override code depending on your needs.
                   
        """
        if type(scripts) is not list:
            scripts = [scripts]
        if type(parts) is not list:
            parts = [parts]
        load_test = {"name": name, "region": region, "start": start, "scripts": scripts, "parts": parts}
        if override is not None:
            load_test.update({"overrideCode": override})
        return self.connection.post(self.service + "/schedule", json.dumps(load_test))