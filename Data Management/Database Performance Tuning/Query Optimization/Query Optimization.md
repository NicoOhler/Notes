# Query Optimization and Processing
### Overview Query Optimization
+ query execution consists of four steps
	+ parsing
	+ semantic analysis
		+ do all tables/tuples exist
		+ checks user permissions
	+ query tewriting
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
+ example:
	+ remove distinct
		+ primary key is always unique
		+ no need to check whether it already exists
	+ ![[Pasted image 20220512132200.png]]

### Standardization and Simplification
+ ![[Pasted image 20220512132402.png]]
+ 