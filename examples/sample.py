# Import the client and create a connection using your apikey and secret
import wpm_api, json
apikey = ''
secret = ''
c = wpm_api.Client(apikey, secret)

# Monitor
# Return a list of all monitors
monitors = c.monitor().list()
# Select first monitor from the list
first_monitor = monitors['data']['items'][0]
# Return monitor summary
print json.dumps(c.monitor(first_monitor['id']).summary())

# Script
# Upload a new script
new_script = c.script().upload('API test script', 'beginTransaction(function(){beginStep(function(){/*Test1*/})})')
script_id = new_script['data']['script']['id']
# Update the existing script
print json.dumps(c.script(script_id).update('API test script', 'beginTransaction(function(){beginStep(function(){/*Test2*/})})'))
# Delete it
print json.dumps(c.script(script_id).delete())

# File
# Upload a new file (test.txt from the example directory)
new_file = c.file().upload('test.txt')
file_id = new_file['data']['filesReceived'][0]['id']
# Get file info
print json.dumps(c.file(file_id).retrieve())
# Delete file
print json.dumps(c.file(file_id).delete())