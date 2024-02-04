### Motivation
+ basic key-value mapping
	+ simple API
	+ complex data models
+ reliability at massive scale
	+ cloud computing

### System Architecture
+ key-value pairs map different/flexible datatypes
+ API for CRUD Operations
+ scalablity via sharding
	+ horizontal partitioning
	+ ![](../../z_images/Pasted%20image%2020220608175445.png)
+ example systems
	+ ![](../../z_images/Pasted%20image%2020220608181257.png)

### Log-Structured Merge Tree
+ data structure used in
	+ ![](../../z_images/Pasted%20image%2020220608181458.png)
+ approach
	+ buffer writes in memory
	+ flushes data as sorted run
	+ compaction - merges sorted runs into larger runs of next level
+ ![](../../z_images/Pasted%20image%2020220608181817.png)
+ ![](../../z_images/Pasted%20image%2020220608182130.png)

[[Data Models]]
