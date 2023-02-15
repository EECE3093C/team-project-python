# UC Campus Shortest Route Traversal
## by: Jordan Shaheen, Chris Vu, Hung Vo

### Vision
__What is your product (high-level view)?__<br>
Our software application will allow the user to input a starting position and ending position.

__Whom is it for?__<br>
This application can be used for anyone who wants to find the shortest route on UC, including handicapped people.

__What problem does it solve?__<br>
This application solves the problem of wasting time/getting lost finding your destination within UC campus.  

__What alternatives are available, who are your competitors?__<br>
Competitors are Google Maps and well as other GPS applications.

__What is novel in your approach, that is why is this project compelling and worth developing?__<br>
This project is worth developing because it will allow a more detailed description on what campus paths to take to any building on campus.
Most GPS application are not too specific when it comes to UC's campus routes. This will also potentially display the various entree ways
for each building and information about those entree points.
_________________________
### Software Architecture

__Describe at a very high level the system's architecture, identifying the components/modules that will interact.__<br>

__Describe the specific data you will access/store.__<br>
The specific data that we will be storing is the geodata of the buildings, and entraces to those buildings within UC's main campus.  When storing this data, we will also be marking areas within UC's campus that can be accessable by handicapped people since this application will have to work for all types of UC students.  

__What languages/toolkits do you intend to use for the development?__<br>
For this application our team has decided to use the Python programming language.  With Python we will be able to access GoogleMaps API that will allow us to get specific coordinates of buildings around UC's campus.  Here is an example of how we can implement the googlemaps package.

```python
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='Add Your Key here')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

# Validate an address with address validation
addressvalidation_result =  gmaps.addressvalidation(['1600 Amphitheatre Pk'], 
                                                    regionCode='US',
                                                    locality='Mountain View', 
                                                    enableUspsCass=True)
```

Also, since this is a web application, we decided to use the Python webframework Django because it is considered one of the best Python web frameworks for building websites.  Read the [Django Documentation](https://www.djangoproject.com/) to learn more about how it works.
_________________________

### Challenges and Risks
__What is the single most serious challenge you see in developing the product on schedule?__<br>
We believe that the most serious challenge we will have when trying to complete this application is the amount of new software development tools we will be using.  The dedication to time when researching will hopefully not cut extensively into our time developing.
  
__How will you minimize or mitigate the risk?__<br>
When researching, it will be very important to collaborate with our team on our findings and also work together to find the best solution to a problem.  Jordan Shaheen is also familiar with using Django in multipule Co-ops, so he will also be able to navigate the Django development process.
