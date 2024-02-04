### Weird Questions
+ A new Thread object must be used each time a runnable code is to be started. 
	+ true
+ UDP message passing may imply space uncoupling. 
	+ false
+ Spatial uncoupling is a property which some indirect communication services provide.
	+ true
+ Consider a multi-threaded server which is answering to client requests. Describe 3 policies how incoming client requests can be assigned to server threads.
	+ thread per request/connection/service
+ Message queue systems may implement different queue models 
	+ true

### General
+ volatile
	+ JVM loads value always from memory instead of local cache
	+ reading from cache might cause problems with multiple threads accessing the same variable
+ defensive copies
	+ if mutable object should only be changed by the native class, the a defensive copy must be made any time it's passed into (constructor, setter) or out of (getter) the class.
	+ otherwise caller can break encapsulation, by changing the object
	+ prevents mutation from outside
		+ mutable object should only be changed within the native class
	+ security
		+ protects against ill-behaved clients and attacks
+ varargs
	+ method(int first_arg, int... remaining_args)
+ optionals
	+ alternative to `null`
	+ avoids `null` checking
	+ `Optional<Car> optCar = Optional.ofNullable(car);`
	+ `maxSpeed = optCar.map(Car::getMaxSpeed);`

### FX
+ basic elements
	+ stage - window
		+ first stage - initial window
	+ scene graph - tree representing UI elements
	+ scene - container
		+ may fill stage
		+ uses observable collections
+ classes
	+ Node - JF base class
	+ Pane - container base class
	+ Control - base class for interactive elements (buttons)
	+ Shape - base of vector shapes
+ observer 
	+ implements EventHandler\<ActionEvent>
	+ may be registered to observable object
	+ notified when object triggers an event
+ Properties 
	+ have value 
	+ observable
		+ method to register observers
		+ notifies on value change
+ Bindings
	+ property change affects other properties
	+ bidirectional 
		+ both directions possible
	+ unidirectional 
		+ one way, otherwise exception
+ MVP 
	+ Model 
		+ logic, data, methods, independent of GUI
	+ View 
		+ GUI creation and manipulation
	+ Presenter 
		+ flow control, handles UI interaction and manipulates model
+ FX threads
	+ application thread
		+ only thread able to access FX elements
			+ Platform.runLater()
		+ handles all events
		+ executes observer methods on event
	+ tasks
		+ thread executing single long running task
	+ service
		+ repeating tasks
		+ scheduled => schedule when to repeat tasks

### 8 golden rules
+ strive for consistency
+ enabled frequent users to use shortcuts
+ offer informative feedback
+ design dialog to yield closure.
+ offer simple error handling.
+ permit easy reversal of actions.
+ support internal locus of control.
+ reduce short-term memory load

### Threads
+ concurrency/parallelism
	+ true
		+ multiple CPUs/cores
	+ pseudo
		+ thread/process switching
	+ improves resource sharing, less idle time/busy wait
+ distributed system
	+ mutliple network components, coordinated via messages
	+ server uses threads for concurrent user requests
	+ e.g. remote method invocation, remote procedure call
	+ server
		+ states
			+ stateful 
				+ client tables
			+ soft state 
				+ for given time
			+ session state 
				+ for session
			+ stateless
		+ listen for/evaluate requests in dispatcher thread
		+ delegate to worker threads
			+ fixed number/dynamic - depends on creation/deletion costs
			+ reusage of threads
				+ thread pool
				+ list of non-active, waiting threads
				+ create all during server startup
			+ thread per request/connection/service-object (each  service with queue)
+ thread
	+ run once
		+ end if run ends
		+ object may still live
	+ methods to pause/end/react_to_end
		+ join
		+ isAlive
		+ resultListener with putResult()
		+ yield
	+ states
		+ new => ready
		+ ready => running
		+ running => blocked/waiting/timed_waiting , terminated
		+ blocked/waiting/timed_waiting => ready
	+ priority from 1 to 10
		+ high if interactive
		+ low if computationally intensive
	+ jvm has several background threads 
		+ garbage collection
		+ program start => new thread executing main
	
### Synchronization
+ synchronized method
	+ locks access to object
	+ or sleep and wait
+ semaphores
	+ limit number of threads accessing critical region simultaneously
	+ counter to limit parallel access
		+ block - `p()`/`down()`
		+ unblock - `v()`/`up()`
		+ can be applied to sets of semaphores
	+ execution sequences with semaphore array
	+ reader/writer problem
		+ exclusive write, shared read
		+ policies
			+ prioritize writers
				+ finish current reads
				+ execute write
			+ prioritize read
				+ execute reads until no more
				+ execute writes
		+ semaphore solution
			+ `read()/write()` execute `before/really/afterRead/Write()`
			+ `before/afterRead/Write` synchronized
+ possible problems and solutions
	+ ![[../z_images/Pasted image 20230124122803.png]]
	+ ![[../z_images/Pasted image 20230124122952.png]]
	+ ![[../z_images/Pasted image 20230124123015.png]]

### Data Stream Processing
+ create stream
	+ (e.g. from list)
+ process data
	+ filter
	+ map 
	+ sum
	+ etc
+ parallel processing
	+ executed in threads parallel for batches of the stream
	+ ![[../z_images/Pasted image 20230121182514.png]]

### [[Networking]]
+ network types
	+ (W)PAN 
		+ USB
		+ Bluetooth
	+ (W)LAN
		+ Ethernet
		+ WiFi
	+ (W)MAN
		+ DSL
	+ (W)WAN
		+ IP-Routing, LTE, 5G
+ topologies
	+ minimum spanning tree in practice
	+ ![[../z_images/Pasted image 20230121183200.png]]
+ TCP
	+ `Socket` and `ServerSocket`
		+ `getInput/OutputStream()`
		+ `accept()`
	+ connection oriented
		+ reliable
		+ handles order
		+ loss
		+ duplicates
		+ flow management
	+ bidirectional
	+ ![[../z_images/Pasted image 20230121183545.png]]
	+ abstract client/server
		+ ![[../z_images/Pasted image 20230121183617.png]]
+ UDP
	+ `DatagramPacket` and `DatagramSocket`
	+ connectionless
		+ unreliable, short message, use error connection codes
	+ unidirectional
	+ supports broad/multicasting 
		+ `MulticastSocket`
	+ abstract client/server
		+ ![[../z_images/Pasted image 20230121183637.png]]

### Communication
+ temporal uncoupling
	+ asynchronous
	+ sender and receiver must not be running/exist at the same time
+ space uncoupling
	+ identity of sender must not be known to other side
		+ e.g. broadcast, MQTT
	+ allow exchange, update or addition of recipients
+ transient communication
	+ receiver must be currently running
	+ request discarded if delivery not possible
	+ ![[../z_images/Pasted image 20230121193628.png]]
+ persistent communication
	+ receiver must not be currently runnning
	+ message stored on middleware 
		+ asynchronous
			+ near client
		+ synchronous
			+ near receiver
	+ ![[../z_images/Pasted image 20230121193648.png]]
+ pull notification
	+ receivers requests/polls information
+ push notification
	+ send notifications on event
	+ multicast

### Group Communication
+ requirements
	+ message integrity
	+ delivery guarantee
	+ receiving order
+ add/remove client, update list status
	+ ![[../z_images/Pasted image 20230121194902.png]]
+ JGroups
	+ protocol stack
		+ layered
		+ UDP (optional TCP)
		+ FRAG (fragmentation)
		+ MERGE
			+ ![[../z_images/Pasted image 20230121195130.png]]
		+ GMS (group membership protocol)
		+ CAUSAL (ordering of messages and answers)
	+ channel
		+ low level functionality for join/leave/send/receive
		+ ![[../z_images/Pasted image 20230121195323.png]]
	+ building blocks
		+ high level functionality
		+ ![[../z_images/Pasted image 20230121195453.png]]
	+ ![[../z_images/Pasted image 20230121195210.png]]
	+ CODE?
+ message queues
	+ middleware for persistent message storage
		+ potentially SSL, transactional, data transformation
	+ decoupling of space and time
	+ ![[../z_images/Pasted image 20230121195715.png]]
+ publish subscribe model
	+ publishers create topics and publishes to them
	+ subscribers subscribe to topics and are notified/receive 
	+ participants independent
		+ do not know each other
	+ broker
		+ ![[../z_images/Pasted image 20230121200201.png]]
		+ ![[../z_images/Pasted image 20230121200304.png]]
	+ subscription models
		+ channel (topics given by channel)
		+ topic (event attribute)
		+ content (event attributes)
		+ type (topics of object type)
+ distributed shared memory = DRAM
	+ ![[../z_images/Pasted image 20230121200458.png]]
	+ ![[../z_images/Pasted image 20230122142621.png]]
+ Tuple Space
	+ Distributed Associative Memory
	+ content-addressable memory
	+ asynchronous publish-subscribe system
	+ ![[../z_images/Pasted image 20230122142757.png]]
	+ implementation
		+ ![[../z_images/Pasted image 20230122143051.png]]
	+ ![[../z_images/Pasted image 20230122143255.png]]

### Reactive Software
+ goals
	+ reponsive
	+ resilient
		+ responsive despite failure
	+ elastic
		+ reponsive under varying workload
	+ message-driven
		+ asynchronous message passing
		+ boundary between components
+ high-level asynchronous Java APIs
	+ `Future`
		+ provides reference to result once completed
		+ blocked when accessing result before completion
			+ `isDone()` before `get()`
			+ `get(1, TimeUnit.SECONDS)` throws `TimeoutException`
		+ `CompletableFuture`
			+ combines several depending futures
			+ wait for completion of all tasks/the fastest
			+ completion notifications - callbacks
	+ `Callable`
		+ hosts asynchronous code to execute
	+ `ExecutorService`
		+ accepts, schedules and runs `Runnable/Callable` objects in threads
		+ interface to submits tasks and obtain results later
		+ returns future on submit
		+ `newFixed/CachedThreadPool()`
		+ blocking threads reduce throughput
		+ needs to be shutdown
	+ code snippets
		+ ![[../z_images/Pasted image 20230124111020.png]]
		+ ![[../z_images/Pasted image 20230124111959.png]]
		+ future-style
			+ ![[../z_images/Pasted image 20230124112226.png]]
		+ callback-style
			+ ![[../z_images/Pasted image 20230124112315.png]]
		+ `CompletableFuture`
			+ ![[../z_images/Pasted image 20230124112600.png]]
		+ `parallelStream`
			+ ![[../z_images/Pasted image 20230124112836.png]]

### [[Transaction]] Concepts
+ set of operations executed atomically
+ provides [[ACID]]
	+ ![[../z_images/Pasted image 20230122151611.png]]
+  serial equivalence 
	+ interleaving of transactions/operations is serially equivalent if the combined effect is the same as if performed sequentially
+ potential problems
	+ lost update
		+ ![[../z_images/Pasted image 20230122151950.png]]
		+ ![[../z_images/Pasted image 20230122180115.png]]
	+ inconsistent retreival
		+ ![[../z_images/Pasted image 20230122175621.png]]
		+ ![[../z_images/Pasted image 20230122180402.png]]
	+ dirty reads
		+ ![[../z_images/Pasted image 20230122175820.png]]
+ compatibility
	+ ![[../z_images/Pasted image 20230122180457.png]]
	+ ![[../z_images/Pasted image 20230122180548.png]]
+ locking
	+ ![[../z_images/Pasted image 20230122180633.png]]
+ ![[../z_images/Pasted image 20230122180718.png]]
+ ![[../z_images/Pasted image 20230122180854.png]]
+ two-phase locking
	+ ![[../z_images/Pasted image 20230122180945.png]]
+ deadlock detection
	+ ![[../z_images/Pasted image 20230122181144.png]]
+ ![[../z_images/Pasted image 20230122181219.png]]