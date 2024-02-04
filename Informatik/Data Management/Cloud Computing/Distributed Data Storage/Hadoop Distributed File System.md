### HDFS Overview
+ distributed file system for large clusters and datasets
+ splits files in 128 MB blocks, 3x replicated and distributed
+ ![[../../../../z_images/Pasted image 20220610105424.png]]

### HDFS NameNode
![[../../../../z_images/Pasted image 20220610105957.png]]

### HDFS DataNode
![[../../../../z_images/Pasted image 20220610110021.png]]

### CRUD Operations
![[../../../../z_images/Pasted image 20220610110411.png]]

### Data Locality
+ HDFS is rack-aware
+ schedule reads form closes DN
+ replica placement 3x
	+ local DN
	+ other-rack DN
	+ same-rack DN

### HDFS Federation
+ eliminates NN als namespace scalability bottleneck
+ multiple independent NNs for name spaces
+ each is responsible for subtrees of file system
+ ![[../../../../z_images/Pasted image 20220610110821.png]]

### Architecture
![[../../../../z_images/Pasted image 20220610111131.png]]

### Excursus: Amazon Redshift
![[../../../../z_images/Pasted image 20220610110942.png]]

[[Distributed Data Storage]]
