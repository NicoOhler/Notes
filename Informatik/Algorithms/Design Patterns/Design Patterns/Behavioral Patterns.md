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

 >[!quote] Chain of Responsibility
> > [!tip] Core idea
> > + forward a request until someone can handle it
>
> > [!danger] Problem
> > + how to resolve who is responsible for a specific task
>
> > [!example] Forces
> >  + multiple escalation levels that may dynamically change during runtime
> > + handling of different tasks by different objects
>
> > [!success] Solution
> > + implement a chain of handlers (specific early, general later)
> > + handle if capable of handling otherwise forward to successor
![](../../../../z_images/Pasted%20image%2020251226124039.png)

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
 
 >[!quote] Interpreter/Abstract Syntax Tree
> > [!tip] Core idea
> > + read expressions one after another and build a tree of expressions
> > + resolve/interpret leaves first and pass results up
>
> > [!success] Solution
![](../../../../z_images/Pasted%20image%2020251226125102.png)

 >[!quote] Mediator
> > [!tip] Core idea
> > + handle 1:n communication between multiple objects
>
> > [!success] Solution
![](../../../../z_images/Pasted%20image%2020251226124902.png)

 >[!quote] Memento
> > [!tip] Core idea
> > + store and load internal state of object
> 
> > [!danger] Problem
> > + how to persist an object?
>
> > [!example] Forces
> > + object state should be (re)storable
> > + do not break encapsulation (i.e. no external access)
>
> > [!success] Solution
> > + create memento class, data class for internal state
> > + implement getter and setter for memento
![](../../../../z_images/Pasted%20image%2020251226125453.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + persistence and restoration of state without exposure to outside
> > > + synergy with command pattern
> >
> >> [!failure] Bad
> >> + outside manipulation of memento $\Rightarrow$ checksum or signature

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

 >[!quote] Template Method
> > [!tip] Core idea
> > + define methods and let children define the behavior
> 
> > [!success] Solution
![](../../../../z_images/Pasted%20image%2020251226130128.png)
### Visitor
+ 
