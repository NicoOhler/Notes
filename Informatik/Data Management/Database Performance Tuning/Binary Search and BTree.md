### Binary Search
+ pos = binarySearch(data,key=23)
+ find key position within sorted data
+ ![](Pasted%20image%2020220505112030.png)
+ optimizations
	+ k-ary search for SIMD data-parallelism
		+ ?
	+ interpolation search: probe  expexted pos in key range
		+ e.g. search for "Bastian" in telephone book, dont start in the middle but rather at the beginning

### BTree
+ self balancing tree
+ individual nodes stored as pages
	+ [[Background Storage System]]
+ each node contains data or reference to data
	+ values sorted within node
	
![](Pasted%20image%2020220505112930.png)
+ pointer left/right of value points to leaf with smaller/bigger values

![](Pasted%20image%2020220505113409.png)
![](Pasted%20image%2020220505113600.png)

### B-Tree Insert
+ always insert into leaf nodes
+ if node overflows (exceeds 2k entries) ==> node splitting
+ node splitting
	+ split into two leaf nodes
	+ left node with first k entries
	+ right node with last k entries
	+ (k+1)th entry inserted into parent node
		+ may cause recursive splitting
+ self-balancing
+ ![](Pasted%20image%2020220506175849.png)
+ Example
	+ ![](Pasted%20image%2020220507102636.png)

### B-Tree Delete
+ deletion might cause underflow (<k entries)
	+ underflow on inner node
		+ ==> move entry from fullest successor (node below) into inner node
	+ underflow on leaf node
		+ ==>  merge with sibling
+ example
	+ ![](Pasted%20image%2020220507103205.png)

### B-Tree Insert and Delete Example  
![](Pasted%20image%2020220507103541.png)

### Prefix Tree
![](Pasted%20image%2020220507103927.png) 

### Learned Index Structures
![](Pasted%20image%2020220507104055.png)