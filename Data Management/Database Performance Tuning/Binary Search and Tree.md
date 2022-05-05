# Binary Search and Tree
### Binary Search
+ pos = binarySearch(data,key=23)
+ find key position within sorted data
+ ![[Pasted image 20220505112030.png]]
+ optimizations
	+ k-ary search for SIMD data-parallelism
		+ ?
	+ interpolation search: probe  expexted pos in key range
		+ e.g. search for "Bastian" in telephone book, dont start in the middle but rather at the beginning

### Binary Tree
+ self balancing tree
+ individual nodes stored as pages
	+ [[Background Storage System]]
+ each node contains data or reference to data
	+ values sorted within node
	
![[Pasted image 20220505112930.png]]
+ pointer left/right of value points to leaf with smaller/bigger values

![[Pasted image 20220505113409.png]]
![[Pasted image 20220505113600.png]]


