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
+ components
	+ DriverManager establishes Connection to execute Prepared/ 
	+ ![[Pasted image 20220427121722.png]]