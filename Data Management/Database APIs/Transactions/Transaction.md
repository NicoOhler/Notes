# Transaction TX
### Overview
+ series of steps viewed as atomic unit
	+ either fully executed or not
+ transactions can be fully committed or rolled back in case an error occurs
+ transforms database from consistent state into another consistent state
+ transaction satisfy ACID properties

### ACID
+ atomic
	+ all or nothing
	+ either fully executed or not
	+ if TX fails ==> no changes are made - UNDO
+ consistent
	+ end of transaction has all constrains satisfied
+ isolation
	+ multiple concurrent transaction seem to execute sequentially
+ durability
	+ succesful transactions survive permanently even if system fails
	+ system failure ==> db recoverable - REDO

### [[SQL]] Transaction Examples
+ ![[Pasted image 20220427124340.png]]
+ ![[Pasted image 20220519141009.png]]

### Transaction Anomalies
+ ![[Pasted image 20220519142025.png]]
+ ![[Pasted image 20220519142122.png]]
+ ![[Pasted image 20220519142248.png]]
+ ![[Pasted image 20220519142354.png]]

### Transaction Isolation Level
+ guarantees certain anomalies cannot happen
+ sacrifices performance
+ ![[Pasted image 20220427124439.png]]
+ ![[Pasted image 20220519142535.png]]
+ isolation level can be set by user or system
	+ ![[Pasted image 20220519142827.png]]

