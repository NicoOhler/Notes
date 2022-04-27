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
+ consistent
	+ end of transaction has all constrains satisfied
+ isolation
	+ multiple concurrent transaction seem to execute sequentially
+ durability
	+ succesful transactions survive permanently even if system fails

### [[SQL]] Transaction Example
+ ![[Pasted image 20220427124340.png]]

### Transaction Isolation Level
+ guarantee certain things cannot happen
+ sacrifices performance
+ ![[Pasted image 20220427124439.png]]
