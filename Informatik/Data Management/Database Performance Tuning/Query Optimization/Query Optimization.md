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
+ ![](../../../z_images/Pasted%20image%2020220512131924.png)

### Overview Execution Strategies
+ different strategies with different pros and cons
+ (Volcano) iterator model
	+ see [[Physical Operators]]
+ materialized intermediates
	+ one column at a time
	+ uses binary association tables (BATs)
	+ ![](../../../z_images/Pasted%20image%2020220512153121.png)
+ vectorized (batched) execution
	+ one vector at a time
	+ ![](../../../z_images/Pasted%20image%2020220512153159.png)
+ query compilation
	+ no longer operator centric ==> data centric
	+ blurred boundaries between operators
	+ ![](../../../z_images/Pasted%20image%2020220512153320.png)


