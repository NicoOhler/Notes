+ The "strategy" pattern allows for inserting or changing the behavior of a class at runtime.
+ The "observer" pattern can be used for informing other objects about changes
+ What would be a useful situation for the factory method pattern? Explain in a few words.
	+ when the concrete class of an object is not known at compile time
	+ e.g. unsure which OS, communication protocol, ...
+ Which pattern can be used to make a class compatible to a specific interface without changing the class source close? Explain how it works.
	+ class or object adapter
	+ create a sub class (inherits from adaptee) or wrapper class (contains adaptee) which provides the same functionality as the desired interface and handles the conversion internally
+ Which pattern can be used to encapsulate complex structure in a better interface? Explain how it works.
	+ Facade encapsulates everything needed and provides a simpler, easy to use interface that adheres to the desired programming paradigm and convention
+ Connect the pattern to its best fitting statement
	+ client-server
		+ processing requests on a central place
	+ broker
		+ connecting nodes together for communication
	+ master-slave
		+ distributing work amongst multiple nodes
	+ leader-follower
		+ taking turns in processing a task
+ Which pattern should be used if the creation of objects is very complicated and consists of many steps.
	+ builder
+ The "singleton" patterns ensures that only one instance of an object is present in the system. What mechanism prohibits developers from creating more instances?
	+ private constructor is not accessible from outside. Factory method creates object once during the first calls, stores re and returns referen 

