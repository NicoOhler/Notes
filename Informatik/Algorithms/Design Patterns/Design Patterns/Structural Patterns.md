 >[!quote] Adapter
> > [!info] Context
> > + multiple different frameworks or libraries
>
> > [!danger] Problem
> > + incompatible classes should work together
>
> > [!hint] Forces
> > +  class interfaces do not match
> > + reuse functionality without rewriting class
> > + source code for class might not be available
> > + inheritance prevented due to sealed class
>
> > [!success] Solution
> > + create wrapper class around adaptee (used class)
> > 	+ implements desired interface and handles conversion 
> > 	+ hides complexity
> > + two variants
> > 	+ class adapter inherits from adaptee
> > 	+ object adapter contains adaptee as member
![](../../../../z_images/Pasted%20image%2020251223212158.png)
>
> >[!quote] Consequences of class adapter
> > > [!success] Good
> > > + use override
> > > + access to protected members
> > > + simple inheritance without additional indirection
> >
> > > [!question] Mixed
> > > + everything is inherited, only changes have to be implemented
> >
> >> [!failure] Bad
> >> + need to also implement subclasses
> 
> >[!quote] Consequences of object adapter
> > > [!success] Good
> > > + supports subclasses and Liskov substitution
> > > + hides underlying adaptee
> >
> > > [!question] Mixed
> > > + no methods automatically inherited
> >
> >> [!failure] Bad
> >> + additional indirection

 >[!quote] Bridge
> > [!info] Context
> > + application with abstraction and implementation hierarchies
>
> > [!danger] Problem
> > + decouple abstraction from implementation
>
> > [!examples] Forces
> > + avoid binding between abstraction and implementation
> > + both should support subclasses
> > + change contained to one side
> > + hide implementation details
>
> > [!success] Solution
> > + create abstraction and implementation interface and implement via subclasses
> > + abstraction uses implementation interface instead of concrete implementation
![](../../../../z_images/Pasted%20image%2020251224115629.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + separates implementation and abstraction
> > > + both are extensive and grow independently 
> > > + implementation can be decided/swapped during runtime
> > > + hide implementation details
> > > + encourages layering
> >
> >> [!failure] Bad
> >> + higher complexity with more classes and interfaces
> 

 >[!quote] Decorator
> > [!info] Context
> > + extend functionality of objects
>
> > [!danger] Problem
> > + how to add or extend functionality without changing object
>
> > [!tip] Forces
> > + add/remove functionality/responsibility dynamically without affecting other objects
> > + reuse functionality
> > + extensions subclasses would be impractical
> > 	+ many subclasses/extensions/combinations
> > 	+ less dynamic
>
> > [!success] Solution
> > + create subclass which forwards requests (function calls) to its object
> > + perform additional operations before or after request
![](../../../../z_images/Pasted%20image%2020251223211942.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + flexible and dynamic addition and removal of responsibilities during runtime
> > > + easy to add property twice??
> > > + avoids feature laden classes and class explosion issue
> >
> >> [!failure] Bad
> >> + decorator and component not identical??
> >> + hard to learn and debug
> >> + many little objects which only differ in their interconnection??

 >[!quote] Facade
> > [!info] Context
> > + working with complex code
> > + potentially with different programming paradigms
>
> > [!danger] Problem
> > + make use of complex code easy and intuitive
>
> > [!tip] Forces
> > + different platforms, paradigms, environments and conventions
> > + heterogeneous code is difficult to maintain
> > + change of underlying code is costly or impossible
> > + details should be hidden
>
> > [!success] Solution
> > + implement a simple high level wrapper 
> > + hides complexities and implementation details
> > + provide easy to use OO interface
![](../../../../z_images/Pasted%20image%2020251223212122.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + concise, cohesive and robust high level
> > > + code becomes robust and easy to learn/understand/maintain
> >
> >> [!failure] Bad
> >> + reduced functionality
> >> + lose benefits of underlying paradigm
> >> + additional abstraction with potential performance loss

 >[!quote] Proxy
> > [!info] Context
> > + need for versatile references to objects
>
> > [!danger] Problem
> > + how to control the access to objects
>
> > [!tip] Forces
> > + objects in different address spaces
> > + delay expensive object creation to when it is needed
> > + restrict access e.g. via rights
> > + perform additional action upon access to object 
>
> > [!success] Solution
> > + proxy class provides interface identical to subject
> > + maintain reference to subject and control access to it
> > + similar to decorator but with different intent: access control vs. extension
![](../../../../z_images/Pasted%20image%2020251224122850.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + separates original functionality from housekeeping
> > > + potential for hidden optimizations (delay creation, caching) and access control
> >
> >> [!failure] Bad
> >> + performance and complexity overhead due to indirection

 >[!quote] Composite
> > [!tip] Core idea
> > + treat object hierarchies identically
> > + composite may be leaves, chains or object trees (e.g. HTML DOM)
> > + action on composite forwarded to children
> 
> > [!info] Context
> > + object hierarchies with different granularities
>
> > [!danger] Problem
> > + how to handle different granularities of objects identically in hierarchies
>
> > [!examples] Forces
> > + need to represent arbitrary hierarchies but also treat them identical
> > + each object should has its own behavior (implementation)
> > + apply method call on all objects
>
> > [!success] Solution
> > + define interface for all granularities with needed methods
> > + composites forward the call while children execute them
![](../../../../z_images/Pasted%20image%2020251224123221.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + provides flexible and extensible hierarchy of primitives and composites
> > > + simple hierarchy handling
> >
> > > [!question] Mixed
> > > + changing roles 
> > > 	+ leaf turns into composite or vice versa
> > > + references to parent
> >
> >> [!failure] Bad
> >> + client unaware of call complexity and potential side effects
> 

 >[!quote] Flyweight
> > [!tip] Core idea
> > + share global state and vary differences only when needed
> 
![](../../../../z_images/Pasted%20image%2020251224124420.png)

