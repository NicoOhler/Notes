# JDBC
### Overview
+ Java Database Connectivity
+ [[Call Level Interfaces]] for accessing databases independent of DBMS from Java
+ most relational DBMS have JDBC implementations
+ driver types
	+ ![[Pasted image 20220427121203.png]]

### JDBC Components and Flow
+ driver manager establishes connection to execute (prepared/callable) statements which may return results
	+ ![[Pasted image 20220427121722.png]]
+ prepared statements
	+ avoid [[SQL Injection]] because inserted data need specific datatypes
		+ regular statements just execute query strings
	+ reusable ==> better performance
+ callable statements
	+ prepared statement which calls a stored 

### Example
+ ![[Pasted image 20220427122129.png]]
+ ![[Pasted image 20220427122230.png]]
+ ![[Pasted image 20220427122514.png]]
+ ![[Pasted image 20220427122704.png]]

### Transaction Handling
+ [[Transaction]] disabled by default
+ can be enabled
+ transactions can be fully committed or rolled back in case an error occurs
+ ![[Pasted image 20220427124828.png]]
+ batch inserts/fewer commits can increase performance
+ ![[Pasted image 20220427125018.png]]