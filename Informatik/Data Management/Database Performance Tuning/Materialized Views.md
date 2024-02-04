### Overview
+ precompute often used queries, store and reuse them multiple times
+ frequently re-occuring queries (views) need to be identified

### Lifecycle
+ select view
	+ NP-hard
	+ heuristic, greedy and approximate algorithms exist
+ use view within other queries
	+ use some parts of the view and use more operators on top of it
+ maintain view whenever data is added/removed

### View Maintenance
+ eager maintenance
	+ writer pays
	+ update view whenever underlying data is changed
	+ ![](../../../z_images/Pasted%20image%2020220507113629.png)
+ deferred maintenance
	+ reader pays
	+ update view on explicit user request
	+ potentially inconsistent base tables and views
+ lazy maintenance
	+ asynd/reader pays
	+ same guarantess as eager maintenance
	+ defer maintenance until free cycles or view required
	+ ![](../../../z_images/Pasted%20image%2020220507113852.png)

### How View Maintenance is done
+ incremental maintenance
	+ track changes in separate table - propagate
	+ apply collected changes to view - apply
	+ ![](../../../z_images/Pasted%20image%2020220507114310.png)
	+ ![](../../../z_images/Pasted%20image%2020220507114318.png)

### Materialized Views in PostgreSQL
+ ![](../../../z_images/Pasted%20image%2020220507114449.png)

[[Database Performance Tuning]]