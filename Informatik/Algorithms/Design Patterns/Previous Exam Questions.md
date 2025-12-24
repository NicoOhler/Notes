+ Broker in detail!!!
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
+ The "singleton" pattern ensures that only one instance of an object is present in the system. What mechanism prohibits developers from creating more instances?
	+ private constructor inaccessible from outside. Factory method creates object once during first call, stores reference and returns it on subsequent calls 
+ Which resources does the Flyweight pattern save?
	+ memory, performance, disk read/write, data bus-traffic
+ When I implement Netflix, which patterns are useful?
	+ broker for communication and distribution of movies and their metadata
	+ layers to separate high level logic, UI, networking, database, ...
	+ facade and message endpoint to provide simple public API
	+ messaging patterns such as messages, request-response, endpoint and router
	+ MVC/MVVM/MVP for UI
	+ memento to store settings and progress (which movies watched, where stopped, ...)
+ What are the differences between Mediator/Microkernel/Client-Dispatcher Server/Observer?
	+ mediator handles communication between similar objects
	+ microkernel connects different components by forwarding requests
	+ observer register to subject, informed upon specific event, one-way 
+ The "message translator" pattern converts a message from one data format to another?
+ Which two sides of views does the bridge pattern "connect"?
	+ implementation and abstraction
	+ maybe use?
+ Which sub-patterns are direct participants of broker pattern?
	+ message, bridge, proxy, iterator, factory, decorator
+ Compare Template-Method, Strategy and Command. What are the differences? What are commonalities?
	+ TODO
+ Compare Visitor, Iterator and Composite. What are the differences? What are commonalities?
	+ iterator loops over all elements in a collection
	+ visitor patterns allows performing the "same" action on all elements of an aggregate. however, action implementation may differ between objects due to implementation?
+ Compare Active Object vs. Master Slave!
	+ TODO
+ What is the huge advantage of a Monitor compared to using locks?
	+ monitor provides safe easy to use synchronization and takes care of locking
	+ caller/client does not need to care about locks
+ What is the disadvantage of a Monitor compared to using locks?
	+ need for locks internally
	+ wasteful and coarse locking of whole components instead of locking only the required resource
	+ block




