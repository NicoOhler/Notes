# Query Optimization and Processing
### Overview
+ query execution consists of four steps
	+ parsing
	+ semantic analysis
		+ do all tables/tuples exist
		+ checks user permissions
	+ [[Query Rewriting]]
	+ [[Plan Optimization]]
+ query execution plan
	+ semantic analysis creates QEP
	+ plan optimization creates optimized QEP
	+ can be executed by runtime
+ runtime may store results in cache use again later
+ ![[Pasted image 20220512131924.png]]

### Overview Execution Strategies
+ different strategies with different pros and cons
+ (Volcano) iterator model
	+ see [[Physical Operators]]
+ materialized intermediates
	+ one column at a time
	+ uses binary association tables (BATs)
	+ ![[Pasted image 20220512153121.png]]
+ vectorized (batched) execution
	+ one vector at a time
	+ ![[Pasted image 20220512153159.png]]
+ query compilation
	+ no longer operator centric ==> data centric
	+ blurred boundaries between operators
	+ ![[Pasted image 20220512153320.png]]


