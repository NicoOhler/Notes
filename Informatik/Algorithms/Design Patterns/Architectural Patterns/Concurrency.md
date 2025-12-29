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
> >> [!failure] Bad
> >> + order of execution and invocation may differ
> >> + performance overhead
> >> + trickier debugging

 >[!quote] Future
> > [!tip] Core idea
> > + provide a placeholder for future results
>
> > [!success] Solution
![](../../../../z_images/Pasted%20image%2020251229104636.png)

>[!quote] Locks
> > [!tip] Core idea
> > + ensure mutual exclusive resource access via locking/reservation mechanism
> > + e.g. mutex, semaphore, read/write lock, condition variable, ...
>
> > [!success] Solution
![](../../../../z_images/Pasted%20image%2020251229105200.png)
>
> > >[!quote] Consequences
> > > [!success] Good
> > > + mutual exclusive access enforces consistency
> > > + parallel access to shared resources
> >
> >> [!failure] Bad
> >> + added complexity
> >> + overhead and waiting time
> >> + lock-less alternative might be better suited
> >> + race conditions and deadlocks

>[!quote] Monitor
> > [!tip] Core idea
> > + synchronize method calls to an object
>
> > [!success] Solution
![](../../../../z_images/Pasted%20image%2020251229105645.png)
>
> > >[!quote] Consequences
> > > [!success] Good
> > > + simplifies synchronization and scheduling
> >
> >> [!failure] Bad
> >> + wasteful and coarse locking of whole components leads to bottleneck
> >> + no simultaneous reads
> >> + nested monitors may lead to deadlocks

>[!quote] Thread-Specific Storage
> > [!tip] Core idea
> > + store separate data instances for each thread
>
> > [!success] Solution
![](../../../../z_images/Pasted%20image%2020251229104801.png)

>[!quote] Async-Await
> > [!tip] Core idea
> > + execute functions cooperatively in an event loop
>
> > [!success] Solution
![](../../../../z_images/Pasted%20image%2020251229105045.png)