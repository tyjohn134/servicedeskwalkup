import pprint
import pysnow
import snowapi
import config
import os
import json


c = pysnow.Client(instance=config.servicenow['instance'], user=os.environ['SERVICE_NOW_USERNAME'], password=os.environ['SERVICE_NOW_PASSWORD'])

res = snowapi.searchForUser(c, 'Tyler', 'Johnson')
emails = []
for item in res:
    if item['email'] != '':
        emails.append(dict(email=item['email']))
            
pprint.pprint(json.dumps(emails))
