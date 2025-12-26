 >[!quote] Active Object
> > [!tip] Core idea
> > + encapsulate method invocation and execute asynchronously
> 
> > [!info] Context
> > + multiple clients access objects in different threads or contexts
>
> > [!danger] Problem
> > + how to execute commands in different context
>
> > [!example] Forces
> > + clients invoke remote operation and fetch results later
> > + synchronized access to worker threads
>
> > [!success] Solution
> > + implement proxy which encapsulates method calls using commands
> > + proxy sends requests to scheduler
> > + execute commands in separate thread(pool)
> > + clients wait or 
![](../../../../z_images/Pasted%20image%2020251226150417.png)
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
### Blackboard
+ 
### Layers
+ 
### Pipes & Filters
+ 
### Microkernel
+ 

