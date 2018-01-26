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

class Alert:
    def __init__(self, connection, id):
        self.connection = connection
        self.id = id
        self.service = "/alert/1.0"
        
    def create(self, name, email_addresses, strikes, **kwargs):
        """Creates a new Alert policy.
        
        Arguments:
        name -- The name of the alert policy.
        email_addresses -- An array of comma-separated email addresses associated with the alert 
                                    policy (e.g. ["alert@mycompany.com","myemail@gmail.com"]).
        strikes -- The number of strikes before triggering an alert.
        
        Keyword Arguments:
        description -- A description for the alert policy.
        
        """
        if type(email_addresses) is not list:
            email_addresses = [email_addresses]
        new_policy = {"name": name, "emailAddresses": email_addresses, "strikes": strikes}
        if "description" in kwargs:
            new_policy.update({"description": kwargs['description']})
        return self.connection.post(self.service + "/policy", json.dumps(new_policy))
        
    def list(self):
        """Retrieves a list of policies ordered by date in descending order."""
        return self.connection.get(self.service + "/policy")