### SOLID
+ Single Responsibility
	+ class should have exactly one reason to change??
	+ small classes with single responsibility
	+ Curly's law: "Do one thing and stick to that!" 
	+ avoid god classes
+ Open Closed
	+ extend class behavior without modification
	+ e.g. inheritance, adapter, strategy
+ Liskov Substitution
	+ derived classes must be substitutable for their base classes
+ Interface Segregation
	+ fine grained, client specific interfaces??
+ Dependency Inversion
	+ depend on abstraction instead of concrete implementations

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
	+ late binding
	+ shift binding time to later
	+ prioritize composition over inheritance
	+ Hollywood principle: "Don't call us, we call you!"
+ Usability and Simplicity
	+ easy to use right, hard to use wrong
	+ adhere to expectations, intuitive usage
	+ YAGNI: you ain't gonna need it
	+ 