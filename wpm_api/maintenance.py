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

class Maintenance:
    def __init__(self, connection, id):
        self.connection = connection
        self.id = id
        self.service = "/maintenance/1.0"
        
    def create(self, name, start_date, monitor, duration, **kwargs):
        """Create a new maintenance window and configure monitors to utilize it
        
        Arguments:
        name -- The name of the maintenance window.
        start_date -- ISO 8601 time format in UTC indicating what time the maintenance window 
                          will start. Example: 2012-05-10T13:34:00
        monitor -- An array of valid monitor IDs which will be affected by this maintenance window.
        duration -- How long (in minutes) the maintenance window will last.
        
        Keyword Arguments:
        description -- A description of what this maintenance window is for.
        recurrence -- How often will this maintenance window repeat or if it is a one-time window. 
                           W for weekly, M for monthly, Y for yearly, or 1 for one-time
        alert -- True or False. Allow monitors to alert during the maintenance window.
        
        """
        new_window = {"name": name, "startDate": start_date, "monitor": monitor, "duration": duration}
        if "description" in kwargs:
            new_window.update({"description": kwargs['description']})
        if "recurrence" in kwargs:
            new_window.update({"recurrence": kwargs['recurrence']})
        if "alert" in kwargs:
            new_window.update({"alert": kwargs['alert']})
        return self.connection.post(self.service, json.dumps(new_window))
        
    def list(self):
        """Retrieve a list of all maintenance windows as associated to your account."""
        return self.connection.get(self.service)
        
    def get(self):
        """Retrieves information for a specific maintennce window associated with your account. 
        The maintenance window id that is returned is used to make other api calls."""
        if self.id is None:
            raise Exception("Missing id: This API requires a maintenance window ID be supplied.")
        return self.connection.get(self.service + "/" + self.id)
        
    def update(self, **kwargs):
        """Modify an existing maintenance window.
        
        Keyword Arguments:
        name -- The name of the maintenance window.
        description -- A description of what this maintenance window is for.
        recurrence -- How often will this maintenance window repeat or if it is a one-time window. 
                           W for weekly, M for monthly, Y for yearly, or 1 for one-time
        alert -- Allow monitors to alert during the maintenance window.
        start_date -- ISO 8601 time format in UTC indicating what time the maintenance window 
                          will start. Example: 2012-05-10T13:34:00
        monitor -- An array of valid monitor IDs which will be affected by this maintenance window.
        duration -- How long (in minutes) the maintenance window will last.
        
        """
        if self.id is None:
            raise Exception("Missing id: This API requires a maintenance window ID be supplied.")
        update_window = {}
        if "name" in kwargs:
            update_window.update({"name": kwargs['name']})
        if "description" in kwargs:
            update_window.update({"description": kwargs['description']})
        if "recurrence" in kwargs:
            update_window.update({"recurrence": kwargs['recurrence']})
        if "alert" in kwargs:
            update_window.update({"alert": kwargs['alert']})
        if "start_date" in kwargs:
            update_window.update({"startDate": kwargs['start_date']})
        if "monitor" in kwargs:
            update_window.update({"monitor": kwargs['monitor']})
        if "duration" in kwargs:
            update_window.update({"duration": kwargs['duration']})
        return self.connection.put(self.service + "/" + self.id, json.dumps(update_window))
        
    def delete(self):
        """Deletes a given maintenance window"""
        if self.id is None:
            raise Exception("Missing id: This API requires a maintenance window ID be supplied.")
        return self.connection.delete(self.service + "/" + self.id)