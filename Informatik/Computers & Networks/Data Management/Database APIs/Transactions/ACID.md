### ACID Properties
+ atomic
	+ all or nothing
	+ either fully executed or not
	+ if TX fails ==> no changes are made - UNDO
+ consistent
	+ end of transaction has all constraints satisfied
+ isolation
	+ multiple concurrent transaction seem to execute sequentially
+ durability
	+ successful transactions survive permanently even if system fails
	+ system failure ==> db recoverable - REDO

### [[../../NoSQL/BASE]] Alternative
+ used in [[../../NoSQL/NoSQL]] systems instead of ACID