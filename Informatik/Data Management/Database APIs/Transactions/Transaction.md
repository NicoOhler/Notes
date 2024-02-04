### Overview
+ series of steps viewed as atomic unit
	+ either fully executed or not
+ transactions can be fully committed or rolled back in case an error occurs
	+ includes [[Logging and Recovery]]
+ transforms database from consistent state into another consistent state
	+ via [[Locking and Concurrency Control]]
+ transaction satisfy [[ACID]] properties
	+ dependent on [[Transaction Isolation Level]]

### [[SQL]] Transaction Examples
+ ![[../../../../z_images/Pasted image 20220427124340.png]]
+ ![[../../../../z_images/Pasted image 20220519141009.png]]


