### ABOUT THE PROJECT
Simple REST API service example.

User registration form for events, 
Authorized user is allowed to view all registrations.

### DEPENDENCIES
N/A

### DB MIGRATIONS
To initiate DB migration:
        cd migrations;
        ${PYENV_HOME}/bin/nomad init;
        ${PYENV_HOME}/bin/nomad apply 0-initial

### Local dev Google app engine env
[restapi_project]# dev_appserver.py --admin_host=0.0.0.0 --host=0.0.0.0 app.yaml
