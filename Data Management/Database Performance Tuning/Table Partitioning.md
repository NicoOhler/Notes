# Table Partitioning
### Partitioning Strategies
![[Pasted image 20220507104748.png]]

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
	+ ![[Pasted image 20220507105522.png]]

### Vertical Fragmentation
![[Pasted image 20220507105737.png]]

### Derived Horizontal Fragmentation
![[Pasted image 20220507105901.png]]