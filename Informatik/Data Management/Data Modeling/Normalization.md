### Overview
+ reversible process of changing database schema for better quality and simplicity
+ step by step
	+ ![](Pasted%20image%2020220327154334.png)
+ 4,5,6th Normal Form also exists
+ Denormalization
	+ may improve performance for read-only DBs
		+ anomalies avoided due to read-only e.g. 

### 1st Normal Form
+ no multi-value attributes ==> all attributes are atomic
+ split relations with 1:N or M:N relationships

### 2nd Normal Form
+ must be in 1st Normal Form
+ every non-key attribute must be fully dependent on every key

### 3rd Normal Form
+ every non-key attribute is non-transitively dependent on every key
	+ no dependencies among non-key attributes

[[Database Design]]