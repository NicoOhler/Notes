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

### Physical Table Access Operator
+ seq scan
	+ sequential read of table
	+ reading tuples one by one
+ index scan
	+ first reads all indexes
	+ throwing all away which do not satisfy certain criteria
	+ reads remaining attributes afterwards
+ index only scan
	+ only reads indexes

### Physical Join Operators
+ nested loop join
	+ like two nested for loops
	+ for every tuple in table A iterate over every tuple in table B
	+ slow
+ hash/hash join
	+ only for equi joins
	+ smaller table A is read first
	+ create hashmap out of A
	+ if value in B equal to A ==> hash equal
	+ access via hashmap
	+ fast
+ sort/merge join
	+ no clue... VO#04 1:28
	+ efficient if one table is already sorted


### Physical Grouping Operators
+ hash aggregate
	+ groups into hash tables
	+ useful for additive/incremental aggregations
+ group aggregate
	+ sorting
	+ group by easy if sorted

### Analyzing/Explaining Queries
+ EXPLAIN command before SQL-query
+  returns query tree
	+  physical operators instead of SQL operators
+  EXPLAIN does not update regularly
	+  ANALYZE beforehand necessary
+  ![[Pasted image 20220406163536.png]]
+  Visual EXPLAIN
	+  ![[Pasted image 20220406163735.png]]

[[Relational Algebra]]