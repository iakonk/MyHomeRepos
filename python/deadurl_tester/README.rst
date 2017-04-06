### ABOUT THE PROJECT
Simple app that scans given url and returns list of dead urls.

HTMLParser is used for html parsing - it allows to parse a feed.

Twisted used to handle HTTP GET requests;
Twisted task.Cooperator() allows to run tasks in parallel;
Cooperator allows to limit number of concurrent jobs (HTTP GET requests);
With twisted there are no need to use threads and implent some kind of a queue;
It is not possible to kill python thread from outside;

### DEPENDENCIES
N/A
