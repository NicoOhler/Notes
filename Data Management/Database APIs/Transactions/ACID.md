# ACID
### ACID Properties
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

### [[BASE]] Alternative
+ used in [[NoSQL]] systems instead of ACID