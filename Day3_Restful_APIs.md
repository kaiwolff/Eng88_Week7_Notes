RESTful APIs

REST stands for REpresentational State Transfer.

Architectural style for applications

Ideally, a RESTful service is easy to implement, maintainable, extensible, and scalable.

RESTFUL service should have the following properties:
- Representaiton and data flow
- Messages
- URIs/Naming resources
- Statelessness


### Representation and Data Flow

First step in defining data sources. Taking an example of somethign like customer data, we might represent this as a JSON, or as an XML to contain the data to be used by a RESTful service.

### Messages

HTTP is protocol of internet communication. Works on simple methodology of request/response system. Whenever a request is sent, a response needs to be received back.

The Response Code section represents a status, e.g. the infamous 404 response code means that a resource cannot be found.


#### Requests

The "verb" part of the http request contains one of the following options:
- GET: Read a resource
- POST: Create a resource
- PUT: Update and replace a resource
- PATCH: Update and modify a resource
- DELETE: Delete a resource

URI's & Naming Resources

Key part of R (the representational part) of REST.

By entering a URL, eg `http://service.com/customer/id=1` would yield the customer details as a JSON, e.g:

```
{
"ID":"1",
"firstname:"Joe",
"surname":"Bloggs",
}
```
This will be covered in more detail later on via a practical exercise.



### Statelessness

Statelessness emans that a RESTful service does not maintain or hold the status of previously made requests. E.g. if sendign a request for customer 1 and then customer 2, the calls should be totally separate and the second call would be processed without regard for how the first request was handled.

"Stateful" services might have the ability to call customer 2 by calling customer 1 and then calling "next customer". In a stateless service this is not possible as there is no previous customer call saved. 

In a stateful design, it is necessary to connect to the same server every time. If the server was to go down for some reason, everything would need to be started from the beginning. Statelessness in RESTful APIs means several different servers can be used in the same session, as the need to maintain a record of state is removed.

The advantage of statelessness is that the server does not have to keep any session alive once a request has been received, simply to respond to each request. In a system where a load balancer might process requests, this means that the load balancer can more easily distribute the requests to connected servers, as each request needs only the one response and no session. it is also important as a secodn request might go to a different server, which in a stateful system would lead to problems with replying to requests depending on the state of a previous request.

Stateful systems are used only when it is acceptable or advantageous to have a session open on the service. the common problem associated with this is the aforementioned tendency to reset a session if the point of cotnact changes or a load alancer direts traffic to a different server.

 Authentication can still be handled in stateless systems. Once authenticated, the user receives a "token" that is sent with future requests, meaning that the request is authenticated without the need for a new session. 
 
n analogy would be having a keyfob or ID card instead of having to request access to a building each time the security guard changes.