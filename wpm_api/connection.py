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
import requests, time, hashlib, json

class AuthError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)

class Connection:
    def __init__(self, api_key, secret):
        self.endpoint = "https://api.neustar.biz/performance"
        self.api_key = api_key
        self.secret = secret
        self._auth()

    # Authentication
    def _auth(self):
        timestamp = str(int(time.time()))
        sig_unencoded = self.api_key + self.secret + timestamp
        sig = hashlib.md5(sig_unencoded.encode()).hexdigest()
        params = {"apikey":self.api_key, "sig":sig}
        r1 = requests.get(self.endpoint+"/load/1.0/echo/credential_check", params=params)
        if r1.status_code == requests.codes.OK:
            return params
        else:
            raise AuthError(r1.json())
            
    def _is_json(self, rstring):
        try:
            json_object = json.loads(rstring)
        except ValueError as e:
            return False
        return True
        
    def _build_headers(self, content_type):
        result = {"Accept": "application/json"}
        if content_type != "":
            result["Content-Type"] = content_type
        return result

    def get(self, uri, params=None):
        if params is None:
            params = {}
        return self._do_call(uri, "GET", params=params)

    def post_multi_part(self, uri, files):
        return self._do_call(uri, "POST", files=files)

    def post(self, uri, json=None):
        if json is not None:
            return self._do_call(uri, "POST", body=json)
        else:
            return self._do_call(uri, "POST")

    def put(self, uri, json=None):
        if json is not None:
            return self._do_call(uri, "PUT", body=json)
        else:
            return self._do_call(uri, "PUT")

    def patch(self, uri, json):
        return self._do_call(uri, "PATCH", body=json)

    def delete(self, uri):
        return self._do_call(uri, "DELETE")

    def _do_call(self, uri, method, params=None, body=None, files=None, content_type="application/json"):
        if params is None:
            params = self._auth()
        else:
            params.update(self._auth())
        r1 = requests.request(method, self.endpoint+uri, params=params, data=body, headers=self._build_headers(content_type),files=files)
        # debugging
        # print r1.url
        # print r1.status_code
        if r1.status_code == requests.codes.NO_CONTENT:
            return {}
        if self._is_json(r1.text):
            return r1.json()
        else:
            return r1.text