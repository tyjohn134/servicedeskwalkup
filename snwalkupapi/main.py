from flask import Flask, escape, request, jsonify
from flask_cors import CORS
import pprint
import pysnow
import snowapi
import config
import os
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
c = pysnow.Client(instance=config.servicenow['instance'], user=os.environ['SERVICE_NOW_USERNAME'], password=os.environ['SERVICE_NOW_PASSWORD'])
emails = config.tech_emails
@app.route('/ticket/create', methods=['POST'])
def create_ticket():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        userdId = snowapi.getUser(c, post_data.get('email'))
        assignedToId = snowapi.getUser(c, emails[post_data.get('assignedTo')])
        reason = post_data.get('reason')
        ticket = snowapi.createTicket(userdId, assignedToId, reason, os.environ['SERVICE_NOW_USERNAME'], os.environ['SERVICE_NOW_PASSWORD'])
        pprint.pprint(ticket.one())
        response_object['message'] = '%s ticket created!' % ticket.one()['number']
    return jsonify(response_object)

@app.route('/ticket/searchuser', methods=['GET'])
def search_user():
    res = snowapi.searchForUser(c, request.args['fname'], request.args['lname'])
    emails = []
    for item in res:
        if item['email'] != '':
            emails.append(item['email'])
    return json.dumps(emails)