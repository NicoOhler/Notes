### Motivation
+ Fließbandprinzip
	+ each component has own dedicated task
	+ invented by Henry Ford
+ pipeline the execution of multiple instructions
	+ assembly line of instructions
+ divide instruction processing into distinct stages
	+ different instruction executed each stage
	+ requires additional registers between each stage
	+ ![[Pasted image 20221112175053.png]]

### Example
+ four independent ADDs
	+ ![[Pasted image 20221112165103.png]]
+ laundry analogy
	+ compensate being slow on specific stage
	+ multiple instance of slow stage
	+ ![[Pasted image 20221112165413.png]]

### Ideal Pipelining
+ ![[Pasted image 20221112165539.png]]

### Control Signals
+ signals piped through and used when needed
+ ![[Pasted image 20221112181239.png]]

### RAW Dependence Handling
+ sometimes ressource needed by instruction only available later on
	+ e.g. 2nd instruction needs value from first
	+ ![[Pasted image 20221112181748.png]]