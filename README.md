# Postman Take Home Challenge 
This code was written to complete the task for the take home assesment for the Data Engineer position, and involves using API PUBLIC PUBLICS api to get details
of public apis that can be used and store them into a database.

# Deliverables
- [x] Used OOPS Concepts in my code
- [x] Provided support for handling authentication requirements & token expiration of server
- [x] Providedd support for pagination to get all data
- [x] Develop work around for rate limited server
- [x] Crawled all API entries for all categories and stored it in a database

## How To Run My Code
My Code is now dockerized and can be run using the dockerfile in my codebase. Please Note there is no need for you to setup any database since the firebase is linked directly to my code as a link. Thus all the results are being added to my database table. To make this work on your firebase table change the firebase link near the import section, and put your link. Please use a real time database link as this is what I have used

## My Tables
I have used a NoSQL database because integration of firebase was really simple, and there is no need to do it locally as all of it is done online,
this makes it much easier for me to deploy this using docker.

There is only a single table called API-DATA in my Database 
### Schema

![Image of my table row](https://github.com/higgsboson1209/PublicAPIListCrawler/blob/main/schema.png)

#### API-DATA

API | Auth | Category | Cors | Description | HTTPS | Link |
----|------|----------|------|-------------|-------|------|
Name of API | Authorization Token Type | Category | Cross Origin Resource Sharing | Description of the API | HTTPS or not | Link to access|

## SCOPE OF IMPROVEMENT

- Split data into multiple table and make them SQL based to ensure easy querying of data
- Use a better way to overcome server limit rather than wait for 60 seconds after 10 queries, can be implemented easily by keeping track of time 
