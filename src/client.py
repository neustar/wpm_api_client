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
from .connection import Connection
from .load import Load
from .instanttest import InstantTest
from .monitor import Monitor
from .maintenance import Maintenance
from .script import Script
from .alert import Alert
from .rum import Rum
from .file import File

class Client:
    def __init__(self, api_key, secret):
        """Initialize the API client.

        Arguments:
        api_key -- The WPM user's API key
        secret -- Shared secret

        """
        self.connection = Connection(api_key, secret)
        
    def load(self, id=None):
        return Load(self.connection, id)
        
    def instanttest(self, id=None):
        return InstantTest(self.connection, id)
        
    def monitor(self, id=None):
        return Monitor(self.connection, id)
        
    def maintenance(self, id=None):
        return Maintenance(self.connection, id)
        
    def script(self, id=None):
        return Script(self.connection, id)
        
    def alert(self, id=None):
        return Alert(self.connection, id)
        
    def rum(self, id=None):
        return Rum(self.connection, id)

    def file(self, id=None):
        return File(self.connection, id)