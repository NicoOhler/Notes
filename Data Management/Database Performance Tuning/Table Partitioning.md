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
	+ 