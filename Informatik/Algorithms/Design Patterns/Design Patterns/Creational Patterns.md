 >[!quote] Singleton
> > [!tip] Core idea
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
> > + implement interface for creation of individual parts and their use
> > + assembly in separate class
![](../../../../z_images/Pasted%20image%2020251226132043.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + combine parts in a very flexible manner
> > > + separate creation from assembly
> >
> >> [!failure] Bad
> >> + construction becomes trickier?
> >> + how to ensure a proper configuration?
### Factory Method
+ 
### Abstract Factory
+ 
### Prototype
+ 
