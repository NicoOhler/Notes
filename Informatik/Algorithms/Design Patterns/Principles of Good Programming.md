### SOLID
+ Single Responsibility
	+ class should have exactly one reason to change
		+ class should have one job
		+ Curly's law: "Do one thing and stick to that!" 
	+ avoid god classes
	+ aim for small classes with single responsibility
+ Open/Closed
	+ objects should be open for extension but closed for modification
	+ extend class behavior without modification of base class
	+ e.g. inheritance, adapter, strategy
+ Liskov Substitution
	+ derived classes must be substitutable for their base classes
+ Interface Segregation
	+ client should not be forced to implement interface which is not needed
	+ aim for fine grained, client specific interfaces that do one thing
	+ avoid general purpose interfaces, otherwise clients might need to implement undesired behavior
+ Dependency Inversion
	+ high level objects should depend on abstractions instead of concrete low level implementations
### Principles of Good Programming
+ Decomposition
	+ makes a large problem more manageable
	+ decomposition into smaller subproblems (single responsibility)
	+ divide and conquer
	+ separate concerns
+ Abstraction
	+ wrap another layer around a problem (Liskov Substitution)
	+ hide implementation details
+ Decoupling
	+ reduce dependencies
	+ minimize coupling and maximize cohesion
	+ separation of concerns
	+ late binding, shift binding time to later
	+ prioritize composition over inheritance
		+ inheritance is hard to understand
		+ however, not everything in same class 
			+ Open/Closed principle
	+ inversion of control?
		+ Hollywood principle: "Don't call us, we call you!"
		+ high level uses low level, not the other way aroun
+ Usability and Simplicity
	+ keep everything simple
		+ single responsibility
		+ avoid premature optimization
	+ easy to use right, hard to use wrong
	+ adhere to expectations, intuitive usage
		+ Principle of least astonishment
		+ Don’t make me think
		+ Code for the Maintainer
	+ common schemes
		+ YAGNI – You ain’t gonna need it!
		+ DRY – Don’t repeat yourself!
		+ KISS – Keep it simple, stupid!
		+ Ockham’s razor - Do the simplest thing possible 
