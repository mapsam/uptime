import os
import json
import time
import datetime as date

UPTIME_FILE = '/home/pi/Documents/uptime/data/uptime.json'

def ping(host, count):
        command = "ping -q -c {0} {1}".format(count, host)
        return os.system(command)

# get the response
response = ping("google.com", 1)

# if the response is anything other than 0, log it
# this means that we are only keeping track of downtime
# since all 0 responses are up and good to go
if response > -1:
        stamp = date.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        result_dict = {'stamp': stamp, 'response': response}

        # read our uptime.json file
        with open(UPTIME_FILE) as j:
                data = json.load(j);
                entries = data['entries']
                num_entries = len(entries)

        # update meta and append new entry to `entries`
        meta = {'last_updated': stamp, 'num_entries': num_entries}
        data.update(meta)
        entries.append(result_dict)

        # write file
        with open(UPTIME_FILE, 'w') as j:
                json.dump(data, j)