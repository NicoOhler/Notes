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
> 
> > > [!example] Examples
> > + 

 >[!quote] Bridge
> > [!info] Context
> > + 
>
> > [!danger] Problem
> > + 
>
> > [!tip] Forces
> > + 
>
> > [!success] Solution
> > + 
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
> > [!example] Examples
> > + a

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
> 
> > [!example] Examples
> > + 

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
> 
> > [!example] Examples
> > + 

 >[!quote] Proxy
> > [!info] Context
> > + 
>
> > [!danger] Problem
> > + 
>
> > [!tip] Forces
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
> > [!example] Examples
> > + 
### Composite 

### Flyweight
+ 
