# Derived Operators
### Intersection
+ R∩S
+ each tuple within R and S
+ set intersection derived from difference
+ bag intersection with element multiplicity min(R,S)
+ require compatible schema

### Division
+ R÷S
+ counterpart to cartesian product
+ ![[Pasted image 20220406145109.png]]

### (Inner) Join
+ R⋈S
+ selection of tuples and attributes from R×S
	+ equivalent in set/bag
+ NULL never matches
+ Theta Join
	+ join by arbitrary condition
+ Natural Join
	+ equi join - join by equivalence
	+ shared attributes only appearing once

### Outer Join
+ same as inner join but NULL matches
+ left outer join
	+ full left side, NULL for non-existing right side
+ right outer join
	+ full right side, NULL for non-existing right side
+ full outer join
	+ full left and right side, NULL for non-existing side
+ ![[Pasted image 20220406145729.png]]
	+ symbols different

### Semi Join and Anti Join
+ left semi join
	+ join based on condition without left side
+ right semi join
	+ join based on condition without right  side
+ right/left anti join
	+ returns tuples that do not appear within other side

### Deduplication, Sorting, Renaming
+ deduplication 
	+ converts a bag into a set by removing duplicates
	+ ALL/DISTINCT
		+ indicate w/ or w/o duplicate elimination
+ sorting
	+ converts a bag into a sorted list of tuples
	+ order lost if used in other ops
	+ ASC/DESC
		+ as/descending order
+ Rename
	+ defines new schema (new attribute/schema names)
	+ tuples keep unchanged

### Grouping and Aggregation
+ grouping γ(R)
	+ group input tuples R according to unique values in A
+ aggregation
	+ compute aggregate per group of tuples (created by grouping)
	+ aggregation w/o grouping possible
	+ ![[Pasted image 20220406154703.png]]
+ 


[[Relational Algebra]]














[[Relational Algebra]]