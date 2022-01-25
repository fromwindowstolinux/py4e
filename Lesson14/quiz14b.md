# Quiz: JSON

1. Who is credited with getting the JSON movement started?
- Douglas Crockford
- Mitchell Baker
- Pooja Sankar
- Bjarne Stroustrup

2. Who is credited with the REST approach to web services?
- Leonard Klienrock
- Roy Fielding
- Vint Cerf
- Daphne Koller
- Bjarne Stroustrup

3. What Python library do you have to import to parse and handle JSON?
- import json
- BeautifulSoup
- ElementTree
- import re

4. Which of the following is true about an API?
- An API is a contract that defines how to use a software library
- An API defines the pin-outs for the USB connectors
- An API keeps servers running even when the power is off
- An API defines the header bits in the first 8 bits of all IP packets

5. What is the method used to parse a string containing JSON data so that you can work with the data in Python?
- json.loads()
- json.read()
- json.connect()
- json.parse()

6. Which of the following is a web services approach used by the Twitter API?
- REST
- CORBA
- XML-RPC
- SOAP

7. What kind of variable will you get in Python when the following JSON is parsed:
```
[ "Glenn", "Sally", "Jen" ]
```
- Three tuples
- A list with three items
- A dictionary with one key / value pair
- One Tuple
- A dictionary with three key / value pairs

8. What kind of variable will you get in Python when the following JSON is parsed:
```
{ "id" : "001",
  "x" : "2",
  "name" : "Chuck"
}
```
- A tuple with three items
- A dictionary with three key / value pairs
- A list with six items
- A list of tuples
- A list with three items

9. Which of the following is not true about the service-oriented approach?
- An application runs together all in one place
- Web services and APIs are used to transfer data between applications
- Standards are developed where many pairs of applications must work together
- An application makes use of the services provided by other applications

10. If the following JSON were parsed and put into the variable x,
```
{
    "users": [
        {
            "status": {
                "text": "@jazzychad I just bought one .__.",
             },
             "location": "San Francisco, California",
             "screen_name": "leahculver",
             "name": "Leah Culver",
         },
   ...
```
what Python code would extract "Leah Culver" from the JSON?
- x["users"][0]["name"]
- x[0]["name"]
- x["name"]
- x["users"]["name"]

11. Which of these two web service approaches is preferred in most modern service-oriented applications?
- REST - Representational state transfer
- SOAP - Simple Object Access Protocol

12. What library call do you make to append properly encoded parameters to the end of a URL like the following:
http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=Ann+Arbor%2C+MI
- urllib.parse.urlencode()
- re.match()
- re.encode()
- urllib.urlcat()

13. What happens when you exceed the Google geocoding API rate limit?
- You cannot use the API for 24 hours
- Your application starts to perform very slowly
- You canot use the API until you respond to an email that contains a survey question
- The API starts to perform very slowly

14. What protocol does Twitter use to protect its API?
- SOAP
- Java Web Tokens
- OAuth
- PKI-HMAC
- SHA1-MD5
- WS*Security

15. What header does Twitter use to tell you how many more API requests you can make before you will be rate limited?
- x-rate-limit-remaining
- x-request-count-down
- content-type
- x-max-requests