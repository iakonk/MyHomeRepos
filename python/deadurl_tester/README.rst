### ABOUT THE PROJECT
Simple app that scans given url and returns list of dead urls.

BeautifulSoup is used for html parsing - it works with selectors, html text, very simply in use.
For instance python HTMLParser does not recognize <script> with type=application/json;
etree.HTMLParser - does not allow to use target parser interface like etree.XMLParser does;

Twisted used to handle HTTP GET requests;
Twisted task.Cooperator() allows to run tasks in parallel;
Cooperator allows to limit number of concurrent jobs (HTTP GET requests);
With twisted there are no need to use threads and implent some kind of a queue;
It is not possible to kill python thread from outside;

### DEPENDENCIES
N/A
