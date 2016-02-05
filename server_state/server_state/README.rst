=====
Server state switcher project
=====

There one BASE table with single object in it: ServerState.
Table consists from two fields:
- last_updated :  will be updated automatically each time you for each change,
- current_state : contains current server state, that was received from WEB

Quick start
-----------

1. To install the package: pip install server_state
2. Install nginx, copy nginx.conf (that comes with archive), to the nginx etc/ dir
3. Run : pip install supervisord
4. Copy supervisord.conf to the supervisor etc/ dir


WIKI page
---------

Project link
---------
Currently project is hosted on coookit.org server and available under: http://coookit.org:8000
