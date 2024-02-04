### Overview
+ alternative to [[MapReduce]]
	+ many shared concepts
+ executors with in-memory storage
	+ lazy evaluation
	+ fault tolerance via [[RDD]] lineage
+ high performance
	+ in-memory storage
	+ fast job scheduling
+ rich, functional high-level [[API]]
	+ general computation DAGs
	+ unified platform

### Architecture
![[../../../../z_images/Pasted image 20220610114627.png]]

### Spark Partitions
+ logical key-value collections split into physical partitions 128MB
+ partitiions are granularity of tasks, I/O, shuffling, evictions
+ ![[../../../../z_images/Pasted image 20220610115447.png]]
+ partitioning preserving
	+ operations which keep keys unchanged do no change partitions
	+ ![[../../../../z_images/Pasted image 20220610115654.png]]

### Lazy Evaluation, Caching and Lineage 
+ ![[../../../../z_images/Pasted image 20220610120256.png]]
+ example: k-means clustering
	+ ![[../../../../z_images/Pasted image 20220610120357.png]]
	+ ![[../../../../z_images/Pasted image 20220610120727.png]]

### Spark DataFrames and DataSets
+ ![[../../../../z_images/Pasted image 20220610120811.png]]
+ example
	+ ![[../../../../z_images/Pasted image 20220610120833.png]]

### Dask
![[../../../../z_images/Pasted image 20220610121102.png]]


