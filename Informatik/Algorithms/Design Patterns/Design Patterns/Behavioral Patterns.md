 >[!quote] Command
> > [!tip] Core idea
> > + decouple invocation from execution via a request
> > + allow reversal of action
> 
> > [!info] Context
> > + invoke behavior of other object
>
> > [!danger] Problem
> > + invoke regardless of concrete implementation and context
>
> > [!example] Forces
> > + avoid coupling of invoker and request context
> > + unaware of concrete implementation
> > + undo requests
>
> > [!success] Solution
> > + define simple command interface
> > + implement behavior in concrete commands which may contain receiving object
> > + client calls command, passes parameters or initializes them before
![](../../../../z_images/Pasted%20image%2020251224130543.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + request does not depend on invoker, can be executed in isolation
> > > + undo/redo possible
> > > + switch receivers during runtime
> > > + reuse for multiple receivers
> >
> >> [!failure] Bad
> >> + more objects
> >> + need to store parameters or their references

### Chain of Responsibility
+ 
 >[!quote] Iterator
> > [!tip] Core idea
> > + uniform access to next element of arbitrary collections
> 
> > [!info] Context
> > + different data structures (lists, trees, maps, ...) 
> > + different orders (start to end, reverse, depth/breadth first, FIFO, ...)
>
> > [!danger] Problem
> > + how to simplify this
>
> > [!example] Forces
> > + simple, uniform access to different data structures and different orders
>
> > [!success] Solution
> > + define simple iterator interface
> > + implement concrete iterator for each collection and access order
![](../../../../z_images/Pasted%20image%2020251224132656.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + simple, uniform access
> > > + allow multiple simultaneous iterations
> > > + traversal may vary
> >
> >> [!failure] Bad
> >> + hides underlying structure
> >> + robustness wrt insertions and deletions not guaranteed
> >> + lower efficiency
### Interpreter
+ Abstract Syntax Tree?
### Mediator
+ 
### Memento
+ 
 >[!quote] Observer
> > [!tip] Core idea
> > + subject informs registered observers about changes
> > + e.g. onClick events or MQTT
> 
> > [!info] Context
> > + data distributed over multiple related objects
>
> > [!danger] Problem
> > + how to maintain consistency between them
>
> > [!example] Forces
> > + update others when object changes
> > + polling is costly
> > + other objects not know at compile-time
>
> > [!success] Solution
> > + subject maintains observer list and means to add or remove observers
> > + notify all observers on change by calling their update method
> > + observers react to change and optionally accesses subject data
![](../../../../z_images/Pasted%20image%2020251224124616.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + decouples subjects and observers
> > > + encourages reuse
> > > + supports m:n communication without polling
> >
> > > [!question] Mixed
> > > + synchronous vs. asynchronous
> >
> >> [!failure] Bad
> >> + potential for unexpected/cascading updates

 >[!quote] Strategy
> > [!tip] Core idea
> > + change complex behavior (dynamically) while keeping things relatively simple
> 
> > [!info] Context
> > + many related classes that differ in complex behavior but not data
>
> > [!danger] Problem
> > + how to handle different behaviors without making everything complicated
>
> > [!example] Forces
> > + different algorithm variants
> > + exchangeable at runtime
> > + split behavior from class
>
> > [!success] Solution
> > + provide interface for algorithms
> > + client uses interface without caring about details
> > + allow interchange of concrete algorithms
![](../../../../z_images/Pasted%20image%2020251224125516.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + split behavior from decision logic
> > > + avoids subclasses for different behavior
> > > + reuse behavior for multiple classes
> >
> > > [!question] Mixed
> > > + how to decide on strategy? 
> >
> >> [!failure] Bad
> >> + additional indirection, objects and communication
> >> + no access to private attributes

### Template Method
+ 
### Visitor
+ 
