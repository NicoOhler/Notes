# Basic Operators

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

### Projection
+ $π(R)$
+ set: selection of attributes with duplicate elimination
+ bag: selection of attribute
+ extended projection
	+ arithmetic expressions
		+ new columns based on computation
	+ duplicate occurences
	
### Selection (restriction)
+ $σ(R)$
+ selection of tuples satisfying condition
	+ equivalent in set/bag

### Composition of Complex Queries
+ relational algebra expressions can be represented as data flow graph tree
	+ leaf...tables
	+ root/top...result
+ ![[Pasted image 20220406144328.png]]


[[Relational Algebra]]