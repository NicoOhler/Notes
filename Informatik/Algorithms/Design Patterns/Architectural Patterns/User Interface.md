 >[!quote] Model-View-Controller
> > [!tip] Core idea
> > + separate responsibilities of visualizing, processing and data management in GUI
> 
> > [!danger] Problem
> > + separate data from its representation
>
> > [!example] Forces
> > + view and data changes independently
> > + separation of concerns
> > + different update rates
>
> > [!success] Solution
> > + decouple data storage (model), visualization (view) and data manipulation (controller)
![](../../../../z_images/Pasted%20image%2020251229113409.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + code becomes reusable and separable (e.g. front and backend team)
> > > + decouples data and representation
> >
> >> [!failure] Bad
> >> + (unit testing) complexity increases
### Difference between MVC, MVP and MVVM
+ MVC
	+ controller handles user inputs by updating model
		+ model notifies view about changes (view observes model)
	+ view and model are aware of each other
	+ tight coupling of model and view
+ MVP
	+ addresses coupling issues via presenter
	+ presenter acts as connector between view and model
	+ view handles rendering and calls presenter method upon user inputs
		+ presenter then updates model and afterwards view if needed
+ MVVM
	+ synchronize model and view via data bindings in view model
	+ view is bound to properties of view model
		+ view/model updates itself when property changed by model/view
+ ![](../../../../z_images/Pasted%20image%2020251229114749.png)

 >[!quote] Presentation-Abstraction-Control
> > [!tip] Core idea
> > + decompose GUI generation into smaller agents
> > + each agent consists of presentation, abstraction and control part
>
> > [!success] Solution
![](../../../../z_images/Pasted%20image%2020251229120453.png)
