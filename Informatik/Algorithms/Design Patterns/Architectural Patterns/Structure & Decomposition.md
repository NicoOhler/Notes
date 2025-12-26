 >[!quote] Active Object
> > [!tip] Core idea
> > + encapsulate method invocation and execute asynchronously
> 
> > [!info] Context
> > + multiple clients access objects in different threads or contexts
>
> > [!success] Solution
> > + implement proxy which encapsulates method calls using commands
> > + clients use proxy to send requests to scheduler
> > + execute commands in separate thread(pool)
> > + clients wait or fetch results later (sync vs. async)
![](../../../../z_images/Pasted%20image%2020251226150417.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + simplifies synchronization, very convenient for client
> > > + command executed in separate thread
> >
> > > [!question] Mixed
> > > + order of execution and invocation may differ
> >
> >> [!failure] Bad
> >> + performance overhead
> >> + trickier debugging
### Blackboard
+ 
### Layers
+ 
### Pipes & Filters
+ 
### Microkernel
+ 

