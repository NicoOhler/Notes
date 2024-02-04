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
+ ![](Pasted%20image%2020220427124340.png)
+ ![](Pasted%20image%2020220519141009.png)


