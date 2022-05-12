# Query Optimization and Processing
### Overview Query Optimization
+ query execution consists of four steps
	+ parsing
	+ semantic analysis
		+ do all tables/tuples exist
		+ checks user permissions
	+ [[Query Rewriting]]
	+ plan optimization
+ query execution plan
	+ semantic analysis creates QEP
	+ plan optimization creates optimized QEP
	+ can be executed by runtime
+ runtime may store results in cache use again later
+ ![[Pasted image 20220512131924.png]]

### Query Rewriting
+ rewrite query into semantically equivalent but more efficientl form
+ same query can be expressed differently
	+ avoid hand-tuning
+ complex queries may have redundancy
+ e.g. remove distinct
	+ primary key is always unique
	+ no need to check whether it already exists
	+ ![[Pasted image 20220512132200.png]]

### Standardization and Simplification
+ ![[Pasted image 20220512132402.png]]
+ ![[Pasted image 20220512132850.png]]

### Query Unnesting
+  type-A nesting
	+ unrelated inner query computes an aggregate
	+ no need to aggregate for each tuple
	+ instead aggregate once and insert result into outer query
	+ ![[Pasted image 20220512133206.png]]
+ type-N nesting
	+ unrelated inner query, which returns set of tuples
	+ join more efficient
	+ ![[Pasted image 20220512133412.png]]
+ type-J nesting
	+ unnesting of correlated subqueries w/o aggregation
	+ optimized via join constraint
	+ instead of constraint within subqery
	+ ![[Pasted image 20220512133612.png]]
+ type-JA nesting
	+ unnesting of correlated subqueries w/ aggregation
	+ all aggregates computed at once
	+ ![[Pasted image 20220512133924.png]]

### Selections and Projections
+ transformation rules
	+ selection grouping
		+ multiple groups combined to one
		+ ![[Pasted image 20220512134150.png]]
	+ projection grouping
		+ instead of filtering into stricter filtering
		+ only stricter filtering
		+ ![[Pasted image 20220512134240.png]]
	+ selection pushdown
		+ allows moving selection after join to before
		+ reduces size of join inputs
			+ may allow storing all data within RAM 
		+ ![[Pasted image 20220512134425.png]]
	+ projection pushdown
		+ if only some joined columns are required
		+ remove other columns before
		+ ![[Pasted image 20220512134620.png]]
+ restructuring algorith
	+ ![[Pasted image 20220512134906.png]]
	+ ![[Pasted image 20220512134924.png]]
+ example
	+ ![[Pasted image 20220512135309.png]]