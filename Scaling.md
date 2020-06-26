# SCALING
Scalability is the property of a system to handle a growing amount of work by adding resources to the system.

There are two types of scaling:-
- **Horizontal scaling or Scale out** 
- **Vertical scaling or scale up**

## HORIZONTAL SCALING
<img src="/Images/horizontal scaling.png" width=500> 

- Buying more machines is called horizontal scaling. 
- Scaling horizontally (out/in) means adding more nodes to (or removing nodes from) a system, such as adding a new computer to a distributed software application. 
-Horizontal scaling is costly  at the manufacturing but as the traffic increases horizontal scaling is cost effective. 

**For eg:-** If we have the software of convertor from  pdf file to word file.If we have 3 servers located in Asia,Australia,USA
If the ASIA server which will going to serve the request and is down due to power supply failure
still another USA server will do its task AND there will be no system failure this is the main advantage of Horizontal scaling. 

**ADVANTAGES**
- Fault tolerence is good.
- Due to the more machines if one node or server fails other nodes take charge so system failure is less.
- Scaling is good as users increase.
- Due to more machines load balancing is required.
- Low latency(time)i.e. latency means the time required for the rqst to process and come back.

**DISADVANTAGES**
- All the communication between the servers are through network so network calls(remote processor calls) are slow.
- Data  inconsistentcy(beacuse there is communication between the servers to satisfy the transactions so data can be inconsistent)

## VERTICAL SCALING
<img src="/Images/vertical scaling.png" width=500>

-Buying bigger machine is called Vertical scaling.
- Scaling vertically (up/down) means adding resources to (or removing resources from) a single node, 
typically involving the addition of CPUs, memory or storage to a single computer.
- As the traffic increases the cost of system also increases.

**For eg:-** If we have a software which has only one server located in USA.And if due to power supply failure server will get down and the whole system will down.

**ADVANTAGES**
- Load balancer is not required.
- Inter process communication hence fast.
- Data consistency.

**DISADVANTAGES**
- Single point of failure i.e. if the server fails entire system goes down.
- Hardware limit so scaling is bad.
- number of users handling is less.
- Fault tolerence is bad.
- High latency(time).
