

import pysnow
import config
import os
from datetime import datetime, timedelta

def getUser(c, email):
    user = c.resource(api_path='/table/sys_user')
    response = user.get(query={'email': email})
    return (response.one()['sys_id'])

def searchForUser(c, first_name, last_name):
    user = c.resource(api_path='/table/sys_user')
    response = user.get(query={'first_name':first_name, 'last_name':last_name})
    return (response.all())

def closeTask(task_number, comment, username, passwd):
    c = pysnow.Client(instance=config.servicenow['instance'], user=username, password=passwd)
    # Define a resource, here we'll use the incident table API
    task = c.resource(api_path='/table/task')

    update = {"state":"3", "active": "false", "work_notes":"%s" % comment}

    # Update 'short_description' and 'state' for 'INC012345'
    updated_record = task.update(query={'number': "%s" % task_number}, payload=update)

    # Print out the updated record
    pprint.pprint(updated_record.one)

def updateTask(task_number, comment, username, passwd):
    c = pysnow.Client(instance=config.servicenow['instance'], user=username, password=passwd)
    # Define a resource, here we'll use the incident table API
    incident = c.resource(api_path='/table/task')

    update =  {"comments_and_work_notes": "%s" % comment} 

    # Update 'short_description' and 'state' for 'INC012345'
    updated_record = incident.update(query={'number': '%s' % task_number} , payload=update)

    # Print out the updated record
    pprint.pprint(updated_record.one)


def closeIncident(incident_number, comment, username, passwd):
    c = pysnow.Client(instance=config.servicenow['instance'], user=username, password=passwd)
    # Define a resource, here we'll use the incident table API
    incident = c.resource(api_path='/table/incident')

    update =  {"close_code":"Closed/Resolved by Caller", "close_notes": "%s" % comment, "incident_state":"6","state":"6"} 

    # Update 'short_description' and 'state' for 'INC012345'
    updated_record = incident.update(query={'number': '%s' % incident_number} , payload=update)

    # Print out the updated record
    pprint.pprint(updated_record.one)

def updateIncident(incident_number, comment, username, passwd):
    c = pysnow.Client(instance=config.servicenow['instance'], user=username, password=passwd)
    # Define a resource, here we'll use the incident table API
    incident = c.resource(api_path='/table/incident')

    update =  {"comments_and_work_notes": ""} 

    # Update 'short_description' and 'state' for 'INC012345'
    updated_record = incident.update(query={'number': '%s' % incident_number} , payload=update)

    # Print out the updated record
    pprint.pprint(updated_record.one)

def createTicket(userId, assignedToId, reason, username, passwd):
    # Create client object
    c = pysnow.Client(instance=config.servicenow['instance'], user=username, password=passwd)

    # Define a resource, here we'll use the incident table API
    incident = c.resource(api_path='/table/incident')

    # Set the payload
    new_record = {
        'caller_id': '%s' % userId,
        'assignment_group': config.assignment_group['assign_id'],
        'assigned_to': '%s' % assignedToId,
        'short_description': '%s' % reason,
        'contact_type': 'Walk-in',
        'u_internal':'true',
        'category':'Inquiry / Help',
        'impact':'2',
        'urgency':'2',
        'u_preferred_language':'en',
        'u_business_service': config.u_business_service['bus_id'],
        'location': config.location['loc_id']
    }

    # Create a new incident record
    result = incident.create(payload=new_record)

    return result

