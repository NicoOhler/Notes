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
![](Pasted%20image%2020220610114627.png)

### Spark Partitions
+ logical key-value collections split into physical partitions 128MB
+ partitiions are granularity of tasks, I/O, shuffling, evictions
+ ![](Pasted%20image%2020220610115447.png)
+ partitioning preserving
	+ operations which keep keys unchanged do no change partitions
	+ ![](Pasted%20image%2020220610115654.png)

### Lazy Evaluation, Caching and Lineage 
+ ![](Pasted%20image%2020220610120256.png)
+ example: k-means clustering
	+ ![](Pasted%20image%2020220610120357.png)
	+ ![](Pasted%20image%2020220610120727.png)

### Spark DataFrames and DataSets
+ ![](Pasted%20image%2020220610120811.png)
+ example
	+ ![](Pasted%20image%2020220610120833.png)

### Dask
![](Pasted%20image%2020220610121102.png)


