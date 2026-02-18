### Table Scan vs Index Scan
+ for highly selective predicates
	+ index scan asymptotically way better than table scan
+ index scan higher per tuple overhead
	+ break even at ~5% output ratio
	+ index scan better if filter ratio below ~5%
+ multi-column predicates
	+ fetch/RID-list intersection
+ ![](Pasted%20image%2020220505110646.png)

### Use Cases for Indexes
![](Pasted%20image%2020220505111610.png)

### Create Index
+ create secondary (nonclustered) index on set of attributes
	+ clustered: tuples sorted by index
	+ nonclustered: sorted attribute with tuple references
+ ![](Pasted%20image%2020220505111741.png)
+ allows specifying uniqueness, order, indexing method
+ postgreSQL methods
	+ [[Binary Search and BTree]]
	+ hash
	+ gist
	+ gin

### Classification of Index Structures
![](Pasted%20image%2020220505112449.png)
![](Pasted%20image%2020220505112534.png)


