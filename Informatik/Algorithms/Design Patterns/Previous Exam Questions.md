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
+ Which pattern should be used if the creation of objects is very complicated and consists of many steps.
	+ builder
+ The "singleton" pattern ensures that only one instance of an object is present in the system. What mechanism prohibits developers from creating more instances?
	+ private constructor inaccessible from outside. Factory method creates object once during first call, stores reference and returns it on subsequent calls 
+ Which resources does the Flyweight pattern save?
	+ primarily memory
	+ potentially also computations, disk read/write, data bus-traffic
+ When I implement Netflix, which patterns are useful?
	+ broker for communication and distribution of movies and their metadata
	+ layers to separate high level logic, UI, networking, database, ...
	+ facade and message endpoint to provide simple public API
	+ messaging patterns such as messages, request-response, endpoint and router
	+ MVC/MVVM/MVP for UI
	+ memento to store settings and progress (which movies watched, where stopped, ...)
+ What are the differences between Mediator/Microkernel/Requestor + Request Handler/Observer?
	+ mediator handles communication between similar objects
	+ microkernel routes requests to responsible components by forwarding requests
	+ requestor is responsible for creating and forwarding messages to server, request handler is server side equivalent responsible for parsing request and dispatching responses
	+ observer register to subject, informed upon specific event, one-way 
+ The "message translator" pattern converts a message from one data format to another?
+ Which two sides of views does the bridge pattern "connect"?
	+ implementation and abstraction
	+ maybe use?
+ Which sub-patterns are direct participants of broker pattern?
	+ broker pattern follows a client-server strategy
	+ client and server use proxies instead of a direct communication
	+ proxies create messages (requests and responses) and send them to broker
	+ broker acts as middleman/bridge and potentially as a router/mediator/translator/...
	+ many more patterns can be used in a meaningful way depending on use case
+ Compare Template-Method, Strategy and Command. What are the differences? What are commonalities?
	+ template method defines methods and lets child classes define concrete behavior
	+ strategy utilizes template methods to dynamic swap concrete behaviors by swapping to another class
	+ command pattern packs the desired behavior (high level) and needed parameters into a command object, transmits it to some other object else and lets them execute the command. However, the concrete implementation of the desired behavior (detailed) is defined and handled by the executioner.
+ Compare Visitor, Iterator and Composite. What are the differences? What are commonalities?
	+ iterator loops over all elements of an arbitrary collection in a specific order
	+ visitor pattern allows execution of behavior on all elements of an aggregate,  custom behavior is explicitly defined for each object type, making it easy to create new arbitrary functionality
	+ composite allows for hierarchies of different objects which provide the same functionality. Concrete behavior is however fixed for each object type, making it costly to add new, rarely used functionality
+ Compare Active Object vs. Master Slave!
	+ master slave
		+ client gives master a large task
		+ master splits into smaller, more manageable subtasks
		+ delegates them to slaves, which operate on remote devices or in threads
		+ master combines partial results into final result
	+ active object
		+ client creates commands which specify what to do
		+ inserts them into command queue
		+ separate thread iterates through commands in an event loop
			+ usually a single thread e.g. Python, JavaScript async
+ What is the huge advantage of a Monitor compared to using locks?
	+ monitor provides safe easy to use synchronization and takes care of locking
	+ caller/client does not need to care about locks
+ What is the disadvantage of a Monitor compared to using locks?
	+ need for locks internally
	+ bottleneck due to wasteful and coarse locking of whole components instead of locking only the required resource
	+ prevents multiple simultaneous reads
	+ nested monitors may lead to deadlocks
+ Cache vs. Pool
	+ cache stores resources for later reuse
	+ pool provides exclusive access to a reusable resource
		+ usually multiple identical resources are available
		+ e.g. thread pool, address pool, ...