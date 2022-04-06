# Relational Algebra
+ operands
	+ relations
	+ variables for computing new values
+ operators
	+ traditional set operations
	+ specific relational operations
		+ sorting
		+ deduplification
	+ e.g.
		+ ![[Pasted image 20220406142243.png]]
	+ ![[Pasted image 20220406142441.png]]


### Cartesian Product
+ R×S
+ set of all pairs of inputs
+ each from r combined with each from 2 

### Union
+ R∪S
+ set union with duplicate elimination
+ bag union (commutative but not idempotent)
+ require compatible schema between R and S

### Difference
+ R-S, R\\S
+ each from R, which is not in S
+ set difference
+ bag: element multiplicity of R minus multiplicity min(R,S)
+ 
