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
from mimetypes import MimeTypes
from ntpath import basename

class File:
    def __init__(self, connection, id):
        self.connection = connection
        self.id = id
        self.service = "/script/1.0/file"

    def list(self):
        """List all existing files in account."""
        return self.connection.get(self.service)

    def retrieve(self):
        """Retrieve an existing file info by id."""
        if self.id is None:
            raise Exception("Missing id: This API requires a monitor ID be supplied.")
        return self.connection.get(self.service + "/" + self.id)

    def delete(self):
        """Delete an existing file by id."""
        if self.id is None:
            raise Exception("Missing id: This API requires a monitor ID be supplied.")
        return self.connection.delete(self.service + "/" + self.id)

    def upload(self, file_path, mime_type=None):
        """Upload a new data file.

        Arguments:
        file_path -- Path to the file on the system making the request.

        Keyword Arguments:
        mime_type -- The MIME type of the file. If not specific, the client
                     will attempt to use the mimetypes library to guess.

        """
        if mime_type == None:
            mime = MimeTypes()
            mime_type = mime.guess_type(file_path)[0]
        file_name = basename(file_path)
        file = {'file': (file_name, open(file_path, 'rb'), mime_type)}
        params = {'qqfile': file_name}
        return self.connection.post_multi_part(self.service, file, params=params)
