 >[!quote] Layers
> > [!tip] Core idea
> > + split system into layers based on abstraction level
> 
> > [!info] Context
> > + large systems that require decompositions
>
> > [!danger] Problem
> > + hard to understand system
> > + many dependencies, functions and responsibilities
>
> > [!example] Forces
> > + change should apply to 
>
> > [!success] Solution
> > + 
![](../../../../z_images/Pasted%20image%2020251226151722.png)
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
pipes

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

 >[!quote] Blackboard
> > [!tip] Core idea
> > + collaborate on common data to get best solution
>
> > [!success] Solution
![](../../../../z_images/Pasted%20image%2020251226151509.png)

 >[!quote] Microkernel
> > [!tip] Core idea
> > + route requests to responsible components
>
> > [!success] Solution
![](../../../../z_images/Pasted%20image%2020251226151543.png)
