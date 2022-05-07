# Materialized Views
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
	+ ![[Pasted image 20220507113629.png]]
+ deferred maintenance
	+ reader pays
	+ update view on explicit user request
	+ potentially inconsistent base tables and views
+ lazy maintenance
	+ asynd/reader pays
	+ same guarantess as eager maintenance
	+ defer maintenance until free cycles or view required
	+ ![[Pasted image 20220507113852.png]]

### How View Maintenance is done
+ incremental maintenance
	+ track changesin and update view according to these changes