# Index Structures
### Table Scan vs Index Scan
+ for highly selective predicates
	+ index scan asymptotically way better than table scan
+ index scan higher per tuple overhead
	+ break even at ~5% output ratio
	+ index scan better if filter ratio below ~5%
+ multi-column predicates
	+ fetch/RID-list intersection
+ ![[Pasted image 20220505110646.png]]

### Use Cases for Indexes
![[Pasted image 20220505111610.png]]

### Create Index
+ create secondary (nonclustered) index on set of attributes
	+ clustered: tuples sorted by index
	+ nonclustered: sorted attribute with tuple references
+ ![[Pasted image 20220505111741.png]]
+ allows specifying uniqueness, order, indexing method
+ postgreSQL methods
	+ btree
	+ hash
	+ gist
	+ gin

### Binary Search
+ pos = binarySearch(data,key=23)
+ find key position within sorted data
+ ![[Pasted image 20220505112030.png]]
+ optimizations
	+ k-ary search for SIMD data-parallelism
		+ ?
	+ interpolation search: probe  expexted pos in key range
		+ e.g. search for David in teleph
	+ ![[Pasted image 20220505112218.png]]