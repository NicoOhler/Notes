# Resilient Distributed Datasets
### RDD Abstraction
+ immutable, partitioned collection of [[Key-Value Pairs]]
+ fault tolerance via lineage-based re-computation

### Operations
+ coarse-grained deterministic operations
	+ transformations
	+ actions
+ ![[Pasted image 20220610114942.png]]

### Distributed Caching
+ fraction of worker memory used for caching
+ different storage levels
	+ ![[Pasted image 20220610115050.png]]

### RDD Lifecycle
+ ![[Pasted image 20220610115306.png]]