### Adapter
+ context
	+ multiple different frameworks or libraries
+ problem
	+ incompatible classes should work together
+ forces
	+ class interfaces do not match
	+ reuse functionality without rewriting class
	+ source code for class might not be available
	+ inheritance prevented due to sealed class
+ solution
	+ create wrapper class around adaptee (used class)
		+ supports the desired interface
	+ two variants
		+ class adapter inherits from adaptee
		+ object adapter contains adaptee as member
+ class adapter
>[!quote] consequences
> > [!success] Pros
> > + convenient without additional indirection
> > + only change
>
> >[!question] Pros
> >+ convenient without additional indirection
> >+ only change
>
> >[!failure] Cons
> >+ would have to adapt subclasses as well

 >[!quote] name
> > [!info] context
> > + multiple different frameworks or libraries
>
> > [!danger] problem
> > + incompatible classes should work together
>
> > [!example] forces
> > +  class interfaces do not match
> > + reuse functionality without rewriting class
> > + source code for class might not be available
> > + inheritance prevented due to sealed class
>
> > [!success] solution
> > + create wrapper class around adaptee (used class)
> > + supports the desired interface
	+ two variants
		+ class adapter inherits from adaptee
		+ object adapter contains adaptee as member
>
> >[!quote] consequences
> > > [!success] Pros
> > > + 
> >
> > > [!question] ?
> > > + 
> >
> >> [!failure] Cons
> >> + 


### Bridge
+ 
### Composite 
+ 
### Decorator
+ 
### Facade
+ 
### Flyweight
+ 
### Proxy
+ 
