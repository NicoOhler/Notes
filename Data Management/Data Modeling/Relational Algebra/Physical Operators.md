# Physical Operators
### (Volcano) Iterator Model
+ everything implements ONC interface
	+ open
	+ next
	+ close
+ query exectution from root node
+ hierarchical and scalable
+ everything one by one
+ blocking operations may prevent this
	+ sorting/grouping/aggregation/hash joins
	+ require knowledge of all tuples not just one
+ e.g. 
	+ ![[Pasted image 20220406161042.png]]
	+ ![[Pasted image 20220406161145.png]]
