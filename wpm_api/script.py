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
        """Creates a single-step test script that opens a browser and loads to the given URL."""
        new_script = {"url": url}
        return self.connection.post(self.service + "/url", json.dumps(new_script))
        
    def list(self):
        """Retrieves a list of valid scripts."""
        return self.connection.get(self.service)
        
    # def create(self, name, script_body, bypass_validation=False):
        # """Create a custom test script.
        
        # Arguments:
        # name -- The name of your test script.
        # script_body -- The JavaScript body of your test scenario.
        
        # """
        # new_script = {"name": name, "scriptBody": script_body, "format": "JavaScript"}
        # if bypass_validation is True:
            # new_script.update({"validationBypassed": True})
        # return self.connection.post(self.service, new_script)