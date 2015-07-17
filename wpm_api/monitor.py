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

class Monitor:
    def __init__(self, connection, id):
        self.connection = connection
        self.id = id
        self.service = "/monitor/1.0"
        
    def create(self, name, interval, locations, **kwargs):
        """Creates a new monitor and returns the monitor id of the newly created monitor. Name, 
        interval, testScript and locations are required. Use the Get Monitoring Locations api to 
        retrieve a list of monitoring locations.
        
        Arguments:
        name -- The name of the monitor.
        interval -- How often the monitoring script will run for each of the locations.
        locations -- A CSV list of locations that this monitor should run from.
        
        Keyword Arguments:
        test_script -- The id of the test script that this monitor should run.
        description -- A description of what this monitor is for.
        alert_policy -- The id of the alert policy that this monitor should run.
        browser -- Specifies the browser type that this monitor should use (IE, CHROME or FF). 
                       Note: IE is available for Enterprise customers only.
        active -- True or False. Enables or disables this monitor from taking samples.
        type -- Set to network monitor type such as 'dns'. See related settings below. Leave this 
                  blank for script-based monitors. Note: this interface will not allow you to test network 
                  monitor creation. Please use your API client.
                      DNS
                      PING
                      SMTP
                      POP
                      PORT
        dns_settings -- A JSON object containing all DNS-related settings: 
                                  {
                                      "timeout": int, 
                                      "lookups": array
                                  } 
                              The "lookups" array contains JSON objects with this format:    
                                  {
                                      "lookupType": string ("A" or "AAAA"), 
                                      "authoritative": boolean, 
                                      "hostname": string, 
                                      "dnsServer": string, 
                                      "expectedIps": string of comma-separated IP addresses
                                  }
        ping_settings -- A JSON object containing all PING-related settings: 
                                   {
                                       "timeout": int, 
                                       "host": string
                                   }        
        pop_settings -- A JSON object containing all POP-related settings: 
                                  {
                                      "timeout": int, 
                                      "server": string, 
                                      "username": string, 
                                      "password": string
                                  }                      
        port_settings -- A JSON object containing all PORT-related settings: 
                                  {
                                      "timeout": int, 
                                      "server": string, 
                                      "port": int, 
                                      "protocol": string ("tcp" or "udp"), 
                                      "command": string, 
                                      "expected_response": string, 
                                      "data_format": string ("ascii" or "raw")
                                  }
        smtp_settings -- A JSON object containing all SMTP-related settings: 
                                    {
                                        "timeout": int, 
                                        "server": string, 
                                        "email": string
                                    }
                                    
        """
        new_monitor = {"name": name, "interval": interval, "locations": locations}
        if "test_script" in kwargs:
            new_monitor.update({"testScript": kwargs['test_script']})
        if "description" in kwargs:
            new_monitor.update({"description": kwargs['description']})
        if "alert_policy" in kwargs:
            new_monitor.update({"alertPolicy": kwargs['alert_policy']})
        if "browser" in kwargs:
            new_monitor.update({"browser": kwargs['browser']})
        if "active" in kwargs:
            new_monitor.update({"active": kwargs['active']})
        if "type" in kwargs:
            new_monitor.update({"type": kwargs['type']})
        if "dns_settings" in kwargs:
            new_monitor.update({"dnsSettings": kwargs['dns_settings']})
        if "ping_settings" in kwargs:
            new_monitor.update({"pingSettings": kwargs['ping_settings']})
        if "pop_settings" in kwargs:
            new_monitor.update({"popSettings": kwargs['pop_settings']})
        if "port_settings" in kwargs:
            new_monitor.update({"portSettings": kwargs['port_settings']})
        if "smtp_settings" in kwargs:
            new_monitor.update({"smtpSettings": kwargs['smtp_settings']})
        return self.connection.post(self.service, json.dumps(new_monitor))
        
    def list(self):
        """Retrieves a list of all monitors associated with your account, along with information about 
        each. The monitor id that is returned is used to make other api calls."""
        return self.connection.get(self.service)
        
    def get(self):
        """Retrieves information for a specific monitor associated with your account. The monitor id 
        that is returned is used to make other api calls."""
        if self.id is None:
            raise Exception("Missing id: This API requires a monitor ID be supplied.")
        return self.connection.get(self.service + "/" + self.id)
        
    def update(self, **kwargs):
        """Change some or all of the parameters of an existing monitor. Requires the monitor ID 
        retrieved from the List Monitors api.
        
        Keyword Arguments:
        name -- The name of the monitor.
        description -- A description of what this monitor is for
        interval -- How often the monitoring script will run for each of the locations.
        test_script -- The id of the test script that this monitor should run.
        locations -- A CSV list of locations that this monitor should run from.
        alert_policy -- The id of the alert policy that this monitor should run.
        browser -- Specifies the browser type that this monitor should use. Note: IE is available for 
                       Enterprise customers only.
        active -- Enables or disables this monitor from taking samples.
        
        """
        if self.id is None:
            raise Exception("Missing id: This API requires a monitor ID be supplied.")
        update_monitor = {}
        if "name" in kwargs:
            update_monitor.update({"name": kwargs['name']})
        if "description" in kwargs:
            update_monitor.update({"description": kwargs['description']})
        if "interval" in kwargs:
            update_monitor.update({"interval": kwargs['interval']})
        if "test_script" in kwargs:
            update_monitor.update({"testScript": kwargs['test_script']})
        if "locations" in kwargs:
            update_monitor.update({"locations": kwargs['locations']})
        if "alert_policy" in kwargs:
            update_monitor.update({"alertPolicy": kwargs['alert_policy']})
        if "browser" in kwargs:
            update_monitor.update({"browser": kwargs['browser']})
        if "active" in kwargs:
            update_monitor.update({"active": kwargs['active']})
        return self.connection.put(self.service + "/" + self.id, json.dumps(update_monitor))
            
    def delete(self):
        """Deletes the given monitor, stopping it from monitoring and removing all its monitoring
        data."""
        if self.id is None:
            raise Exception("Missing id: This API requires a monitor ID be supplied.")
        return self.connection.delete(self.service + "/" + self.id)
        
    def samples(self):
        """Returns all samples associated to this monitor for a given time period. This data is 
        returned at a high level, which timing for the overall sample. To get the details for the 
        specific sample, call the get raw sample data api. At a maximum, this api will return 2000
        samples. If there are more than 2000 results returned, the 'more' field will be set to true 
        and you can make another api call specifying an offset which would be equal to the 
        number of results returned in the first api call plus the offset of that call."""
        if self.id is None:
            raise Exception("Missing id: This API requires a monitor ID be supplied.")
        return self.connection.get(self.service + "/" + self.id + "/sample")
        
    def raw_sample_data(self, sample_id):
        """Retrieve the raw, HTTP Archive (HAR) data for a particular sample"""
        if self.id is None:
            raise Exception("Missing id: This API requires a monitor ID be supplied.")
        return self.connection.get(self.service + "/" + self.id + "/sample/" + sample_id)
        
    def aggregate_sample_data(self):
        """Retrieves the aggregated sample information for a given period of time. You can 
        choose to aggregate the data for each hour or each day. This is more effecient than 
        getting all the individual samples for a period of time and performing the aggregation 
        yourself."""
        if self.id is None:
            raise Exception("Missing id: This API requires a monitor ID be supplied.")
        return self.connection.get(self.service + "/" + self.id + "/aggregate")
        
    def summary(self):
        """The monitor summary api returns all of the data that is found when looking at your list of 
        monitors in the web portal. This includes things such as the average load time, sample 
        count and uptime for the day, week, month or year, the last time an error occurred, and 
        the last error message."""
        if self.id is None:
            raise Exception("Missing id: This API requires a monitor ID be supplied.")
        return self.connection.get(self.service + "/" + self.id + "/summary")
        
    def locations(self):
        """Get a list of all monitoring locations available."""
        return self.connection.get(self.service + "/locations")