 >[!quote] Singleton
> > [!tip] Core idea/Context
> > + allow only one instance of an object
> 
> > [!danger] Problem
> > + how to prevent creation of multiple instances
>
> > [!example] Forces
> > + at most one instance
> > + accessible to all clients
> > + support subclassing
>
> > [!success] Solution
> > + hide class constructor and prohibit copy behavior
> > + instead provide public factory method which creates instance during first access
> > + return references to this instance on subsequent accesses
![](../../../../z_images/Pasted%20image%2020251226131431.png)
> 
> >[!quote] Consequences
> > > [!success] Good
> > > + controlled access to singular instance
> > > + enables refinement via subclassing
> > > + allows for a variable number of instances
> > > + more flexible and elegant compared to static class functions

 >[!quote] Builder
> > [!tip] Core idea
> > + split creation into multiple steps
> 
> > [!info] Context
> > + creation of complex objects
>
> > [!danger] Problem
> > + how to keep creation of complex objects simple?
>
> > [!example] Forces
> > + many different construction options
> > + creation independent of assembly
>
> > [!success] Solution
> > + implement interface for creation of individual parts
> > + handle assembly in separate class
![](../../../../z_images/Pasted%20image%2020251226132043.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + combine parts in a very flexible manner
> > > + separate creation from assembly
> >
> >> [!failure] Bad
> >> + construction is no longer as simple as writing "new"
> >> + need to ensure proper configuration

 >[!quote] Factory Method
> > [!tip] Core idea
> > + delegate object creation to someone else
> 
> > [!info] Context
> > + concrete class unknown at compile time
>
> > [!danger] Problem
> > + how to create object for which the class is not known
>
> > [!example] Forces
> > + object does not matter as long as it provides same functionality
> > + cannot anticipate class, delegate decision to someone else
>
> > [!success] Solution
> > + define interface of expected functionality and the creation
> > + subclass implements its own creation
![](../../../../z_images/Pasted%20image%2020251226132740.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + flexible creation during runtime
> > > + separates creation and usage
> > > + fewer dependencies
> >
> > > [!question] Open Questions
> > > + should the constructor be hidden
> > > + abstract or concrete creator (subclasses must/may override default implementation)
> >
> >> [!failure] Bad
> >> + additional abstraction

 >[!quote] Abstract Factory
> > [!tip] Core idea
> > + create families of related objects
> 
> > [!danger] Problem
> > + how to create only matching objects
>
> > [!example] Forces
> > + objects should fit together
> > + choose object family at runtime
> > + hide concrete implementation
>
> > [!success] Solution
> > + define interfaces for products and factories
> > + implement both
> > + select appropriate factory at runtime to create matching products
![](../../../../z_images/Pasted%20image%2020251226133832.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + easy swapping of product families
> > > + promotes consistency among products
> > > + separates concrete classes elegantly
> >
> > > [!question] Open Questions
> > > + how to select families?
> > > + how to prevent mixing of different factories? via a singleton?
> >
> >> [!failure] Bad
> >> + adding new products becomes more difficult

 >[!quote] Prototype
> > [!tip] Core idea
> > + create objects by cloning from templates
> 
> > [!info] Context
> > + creation of objects with class and properties unknown at compile time
>
> > [!danger] Problem
> > + dynamically instantiate and use object with unknown properties
>
> > [!example] Forces
> > + avoid long and complex instantiations
> > + avoid complex hierarchies and factories
>
> > [!success] Solution
> > + define and implement cloning interface
> > + add getter and setter to dynamically change properties if needed
![](../../../../z_images/Pasted%20image%2020251226134651.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + flexible and dynamic creation without complex class hierarchies
> > > + avoid repeated instantiations
> >
> >> [!failure] Bad
> >> + no type safety or compile time errors
