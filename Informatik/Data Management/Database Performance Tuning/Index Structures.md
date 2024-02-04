### Table Scan vs Index Scan
+ for highly selective predicates
	+ index scan asymptotically way better than table scan
+ index scan higher per tuple overhead
	+ break even at ~5% output ratio
	+ index scan better if filter ratio below ~5%
+ multi-column predicates
	+ fetch/RID-list intersection
+ ![[../../../z_images/Pasted image 20220505110646.png]]

### Use Cases for Indexes
![[../../../z_images/Pasted image 20220505111610.png]]

### Create Index
+ create secondary (nonclustered) index on set of attributes
	+ clustered: tuples sorted by index
	+ nonclustered: sorted attribute with tuple references
+ ![[../../../z_images/Pasted image 20220505111741.png]]
+ allows specifying uniqueness, order, indexing method
+ postgreSQL methods
	+ [[Binary Search and BTree]]
	+ hash
	+ gist
	+ gin

### Classification of Index Structures
![[../../../z_images/Pasted image 20220505112449.png]]
![[../../../z_images/Pasted image 20220505112534.png]]


