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