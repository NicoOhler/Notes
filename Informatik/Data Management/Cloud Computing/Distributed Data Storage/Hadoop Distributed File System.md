### HDFS Overview
+ distributed file system for large clusters and datasets
+ splits files in 128 MB blocks, 3x replicated and distributed
+ ![](Pasted%20image%2020220610105424.png)

### HDFS NameNode
![](Pasted%20image%2020220610105957.png)

### HDFS DataNode
![](Pasted%20image%2020220610110021.png)

### CRUD Operations
![](Pasted%20image%2020220610110411.png)

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
+ ![](Pasted%20image%2020220610110821.png)

### Architecture
![](Pasted%20image%2020220610111131.png)

### Excursus: Amazon Redshift
![](Pasted%20image%2020220610110942.png)

[[Distributed Data Storage]]
