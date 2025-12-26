 >[!quote] Broker
> > [!tip] Core idea
> > + manage dynamic communication between clients and servers in distributed systems
> 
> > [!info] Context
> > + distributed or heterogeneous systems with independent cooperating components
>
> > [!danger] Problem
> > + how to coordinate decoupled, interoperating components in complex systems
>
> > [!example] Forces
> > + support for remote method invocation
> > + dynamic addition, exchange or removal of services
> > + client should not be responsible for locating and selecting components
> > + hide details from other components
>
> > [!success] Solution
> > + specify broker API for clients and servers
> > + define object model for remote procedure calls, ...
> > + hide implementation details behind proxies
![](../../../../z_images/Pasted%20image%2020251226153540.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + broker handles locating and selecting components 
> > > + broker and proxies hide OS, networking and error handling details
> > > + interoperability between different broker
> > > + reuse, add, remove and exchange components dynamically
> > > + components may fail gracefully
> >
> >> [!failure] Bad
> >> + communication overhead
> >> + single point of failure
> >> + hard to test and debug due to many involved components
 
 >[!quote] Client-Server
> > [!tip] Core idea
> > + let clients send requests to server which answers with responses
> 
> > [!info] Context
> > + distributed application
>
> > [!danger] Problem
> > + how to provide services (resources, content, services) to multiple distributed clients
>
> > [!example] Forces
> > + availability of resources limited but needed by multiple clients
> > + service provided by single, centralized provider
> > + clients lack processing power or resources
> > + number of requests unknown
>
> > [!success] Solution
> > + define protocol for communication via requests and responses
> > + implement server with listener waiting for responses from multiple clients and answers with responses
> > + 
![](../../../../z_images/Pasted%20image%2020251226160125.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + 
> >
> > > [!question] Mixed
> > > + 
> >
> >> [!failure] Bad
> >> + 

 >[!quote] Master-Slace
> > [!tip] Core idea
> > + distribute work amongst helpers
> 
> > [!info] Context
> > + dividing work into identical subtasks
>
> > [!danger] Problem
> > + how to solve instances of same problem in different computing contexts
> > + how to separate their concerns?
>
> > [!example] Forces
> > + subtasks independent of partitioning work and recombining results
> > + coordination of subtasks needed
> > + solve many identical subproblems (potentially with different algorithms)
> > + multiple threads or even devices
>
> > [!success] Solution
> > + master distributes work into subtasks, delegates to slaves and combines results
> > + clients communicate only with coordinator (master)
> > + slave have uniform interface, handle work and communicate only with master
![](../../../../z_images/Pasted%20image%2020251226154932.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + separate concerns
> > > + exchange and extensible
> > > + fault tolerant
> > > + parallel and potentially even distributed computation
> >
> >> [!failure] Bad
> >> + not always feasible
> >> + partitioning and recombining can be difficult
