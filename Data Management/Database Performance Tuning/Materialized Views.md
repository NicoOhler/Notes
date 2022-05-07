# Materialized Views
### Overview
+ precompute often used queries, store and reuse them multiple times
+ frequently re-occuring queries (views) need to be identified
+ lifecycle
	+ select view
	+ use view within other queries
	+ maintain view whenever data is added/removed