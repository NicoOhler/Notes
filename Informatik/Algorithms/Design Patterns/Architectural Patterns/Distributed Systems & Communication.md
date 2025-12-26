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
### Client-Server
+ 
### Master-Slave
+ 
