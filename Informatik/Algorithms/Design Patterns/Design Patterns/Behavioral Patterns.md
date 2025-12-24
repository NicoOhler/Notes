### Command
+ 
### Chain of Responsibility
+ 
### Iterator
+ 
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
> > [!examples] Forces
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

### Strategy
+ 

 >[!quote] name
> > [!tip] Core idea
> > + 
> 
> > [!info] Context
> > + 
>
> > [!danger] Problem
> > + 
>
> > [!examples] Forces
> > + 
>
> > [!success] Solution
> > + 
UML
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
> 

### Template Method
+ 
### Visitor
+ 
