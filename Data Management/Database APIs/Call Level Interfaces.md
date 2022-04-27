# Call Level Interfaces
### Overview
+ [[API]] of defined functions for dynamic [[SQL]]
+ allow database interaction using (C, Java, ...)
+ allows arbitrary sql queries
	+ checks if query is valid on db, not before
+ e.g. ODBC, JDBC, DB-API

### ODBC
+ Open Database Connectivity
+ API for accessing databases independent of DBMS and OS
+ all relational DBMS have ODBC implementations

### JDBC
+ API for accessing databases independent of DBMS from Java
+ most relational DBMS have JDBC implementations
+ driver types
	+ ![[Pasted image 20220427121203.png]]
+ driver manager establishes Ccnnection to execute (prepared/callable) statements which may return results
	+ ![[Pasted image 20220427121722.png]]
+ prepared statements
	+ avoid [[SQL Injection]] because inserted data need specific datatypes
	+ regular statements just execute query strings
+ example:
	+ ![[Pasted image 20220427122129.png]]
	+ ![[Pasted image 20220427122230.png]]
	+ ![[Pasted image 20220427122514.png]]
	+ ![[Pasted image 20220427122704.png]]