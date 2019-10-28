# Service Desk Walk Up Kiosk

This project allows an end user to walk up to a kiosk and scan their badge (to get their name and email) and then fill out a short questionaire which will then create a ticket for the incident and assign it to the agent/tech they have selected. 

### NOTE: Requires a ServiceNow production environment

<img src="https://tylerjdev.sfo2.cdn.digitaloceanspaces.com/snwalkup.png">

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

## API
### Set environment variables
Powershell
```
$env:SERVICENOW_USERNAME=""
$env:SERVICENOW_PASSWORD=""
$env:FLASK_APP="main"
```
### Activate venv
```
.\venv\bin\Activate
```
### Install python modules
```
pip install -r requirements.txt
```
### Run API
```
python -m flask run
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
