 # Relational Terminology
+ Goal: Data Independence
+ value domain
	+ datatype
	+ set of all possible values?
	+ set of items
+ relation
	+ set of k attributes
	+ subset of cartesian product over all value domains
+ tuple
	+ row of elements of relation
+ cardinality
	+ number of tuples in the relation
+ rank
	+ number of attributes in the telation
+ database schema
	+ set of relation schemas and constraints
+ database
	+ set of actual relations including data
	+ database instance
+ NULL
	+ value for unknown/missing values
	+ ![](../../../z_images/Pasted%20image%2020220327145512.png)
	+ ![](../../../z_images/Pasted%20image%2020220327145606.png)	
+ primary key
	+ minimal set of attributes to uniquely identify tuples in relation
		+ unique
		+ not null
		+ minimal
+ foreign key
	+ reference to primary key in another relation
	+ may be NULL
	+ Referential Integrity
		+ may cause errors when deleting, because tuple may be referenced
		+ solutions
			+ ![](../../../z_images/Pasted%20image%2020220327151113.png)
+ domain/semantic constraints
	+ constraints of attribute value
	+ unique
	+ not null
	+ between x and y
	+ etc.

[[Database Design]]