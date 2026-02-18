### Partitioning Strategies
![](Pasted%20image%2020220507104748.png)

### Correctness Properties
+ relation R partitioned into n fragments
+ completeness
	+ each item from R must be included in at least one fragment
+ reconstruction
	+ exact reconstruction of fragments must be possible
+ disjointness
	+ no item must be in more than one fragment
	+ $R_i∩R_j=∅$

### Horizontal Partitioning
+ row partitioning into n fragments
	+ complete, disjoint and reconstructable
	+ schema of fragments is equivalent to schema of base relation
+ partitioning
	+ split table by n selection predicates on attributes
		+ e.g. split by last name
	+ beware of attribute domain and skew	
+ reconstruction
	+ union of all fragments
	+ bag semantics but no duplicates across partitions
	+ ![](Pasted%20image%2020220507105522.png)

### Vertical Fragmentation
![](Pasted%20image%2020220507105737.png)

### Derived Horizontal Fragmentation
![](Pasted%20image%2020220507105901.png)

### Exploiting Partitioning in Postgre
![](Pasted%20image%2020220507112231.png)
![](Pasted%20image%2020220507112555.png)

### Database Cracking
+ database layout adapts to requested queries and their range predicates
	+ creates [[Index Structures]] to identify qualifying partitions
	+ inside partition its elements are unordered
+ workload creates hybrid between partitioning and indexing
+ ![](Pasted%20image%2020220507112812.png)

[[Background Storage System]] [[Database Performance Tuning]]