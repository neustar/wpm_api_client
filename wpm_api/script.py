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

class Script:
    def __init__(self, connection, id):
        self.connection = connection
        self.id = id
        self.service = "/script/1.0"
        
    def endpoint(self, url):
        """Creates a single-step test script that opens a browser and loads to the given URL.
        
        Arguments:
        url -- The url to be monitored.
        
        """
        new_script = {"url": url}
        return self.connection.post(self.service + "/url", json.dumps(new_script))
        
    def list(self):
        """Retrieves a list of all scripts."""
        return self.connection.get(self.service + "/AllScripts")
        
    def list_valid(self):
        """Retrieves a list of valid scripts."""
        return self.connection.get(self.service + "/ValidScripts")
        
    def list_invalid(self):
        """Retrieves a list of invalid scripts."""
        return self.connection.get(self.service + "/InvalidScripts")
        
    def upload(self, name, body):
        """Upload a test script file.
        
        Arguments:
        name -- The name of the script being uploaded.
        body -- The script being uploaded.
        
        """
        new_script = {"name": name, "scriptBody": body}
        return self.connection.post(self.service + "/upload/body", json.dumps(new_script))
        
    def clone(self, name):
        """Clone an existing test script.
        
        Arguments:
        name -- The name of the new script.
        
        """
        if self.id is None:
            raise Exception("Missing id: This API requires a monitor ID be supplied.")
        clone_script = {"id": self.id, "cloneName": name}
        return self.connection.post(self.service + "/clone", json.dumps(clone_script))