### Overview
+ rewrite query into semantically equivalent but more efficientl form
+ same query can be expressed differently
	+ avoid hand-tuning
+ complex queries may have redundancy
+ e.g. remove distinct
	+ primary key is always unique
	+ no need to check whether it already exists
	+ ![[../../../../z_images/Pasted image 20220512132200.png]]

### Standardization and Simplification
+ ![[../../../../z_images/Pasted image 20220512132402.png]]
+ ![[../../../../z_images/Pasted image 20220512132850.png]]

### Query Unnesting
+  type-A nesting
	+ unrelated inner query computes an aggregate
	+ no need to aggregate for each tuple
	+ instead aggregate once and insert result into outer query
	+ ![[../../../../z_images/Pasted image 20220512133206.png]]
+ type-N nesting
	+ unrelated inner query, which returns set of tuples
	+ join more efficient
	+ ![[../../../../z_images/Pasted image 20220512133412.png]]
+ type-J nesting
	+ unnesting of correlated subqueries w/o aggregation
	+ optimized via join constraint
	+ instead of constraint within subqery
	+ ![[../../../../z_images/Pasted image 20220512133612.png]]
+ type-JA nesting
	+ unnesting of correlated subqueries w/ aggregation
	+ all aggregates computed at once
	+ ![[../../../../z_images/Pasted image 20220512133924.png]]

### Selections and Projections
+ transformation rules
	+ selection grouping
		+ multiple groups combined to one
		+ ![[../../../../z_images/Pasted image 20220512134150.png]]
	+ projection grouping
		+ instead of filtering into stricter filtering
		+ only stricter filtering
		+ ![[../../../../z_images/Pasted image 20220512134240.png]]
	+ selection pushdown
		+ allows moving selection after join to before
		+ reduces size of join inputs
			+ may allow storing all data within RAM 
		+ ![[../../../../z_images/Pasted image 20220512134425.png]]
	+ projection pushdown
		+ if only some joined columns are required
		+ remove other columns before
		+ ![[../../../../z_images/Pasted image 20220512134620.png]]
+ restructuring algorith
	+ ![[../../../../z_images/Pasted image 20220512134906.png]]
	+ ![[../../../../z_images/Pasted image 20220512134924.png]]
+ examples
	+ ![[../../../../z_images/Pasted image 20220512135309.png]]
	+ ![[../../../../z_images/Pasted image 20220512151834.png]]
	+ ![[../../../../z_images/Pasted image 20220512152310.png]]