### Overview
+ Java Database Connectivity
+ [[Call Level Interfaces]] for accessing databases independent of DBMS from Java
+ most relational DBMS have JDBC implementations
+ driver types
	+ ![](Pasted%20image%2020220427121203.png)

### JDBC Components and Flow
+ driver manager establishes connection to execute (prepared/callable) statements which may return results
	+ ![](Pasted%20image%2020220427121722.png)
+ prepared statements
	+ avoid [[SQL Injection]] because inserted data need specific datatypes
		+ regular statements just execute query strings
	+ reusable ==> better performance
+ callable statements
	+ prepared statement which calls a stored 

### Example
+ ![](Pasted%20image%2020220427122129.png)
+ ![](Pasted%20image%2020220427122230.png)
+ ![](Pasted%20image%2020220427122514.png)
+ ![](Pasted%20image%2020220427122704.png)

### Transaction Handling
+ [[Transaction]] disabled by default
+ can be enabled
+ transactions can be fully committed or rolled back in case an error occurs
+ ![](Pasted%20image%2020220427124828.png)
+ batch inserts/fewer commits can increase performance
+ ![](Pasted%20image%2020220427125018.png)