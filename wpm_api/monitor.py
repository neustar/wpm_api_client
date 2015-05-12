# Copyright 2000 - 2015 NeuStar, Inc.All rights reserved.
# NeuStar, the Neustar logo and related names and logos are registered
# trademarks, service marks or tradenames of NeuStar, Inc. All other
# product names, company names, marks, logos and symbols may be trademarks
# of their respective owners.
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