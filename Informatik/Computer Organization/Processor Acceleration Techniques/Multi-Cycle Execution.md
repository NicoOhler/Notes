### Motivation
+ not all instructions need same amount of time when [[Pipelining]]
+ idea: mutiple different functional units
	+ take different numbers of cycles
	+ ![](../../z_images/Pasted%20image%2020230117115624.png)
	+ ![](../../z_images/Pasted%20image%2020230117115926.png)
+ Problem
	+ instructions might rely on results of previous instructions 
	+ "contract"
		+ ![](../../z_images/Pasted%20image%2020230117120051.png)

### Reorder Buffer (ROB)
+ ![](../../z_images/Pasted%20image%2020230117120146.png)
+ ![](../../z_images/Pasted%20image%2020230117120320.png)
+ ![](../../z_images/Pasted%20image%2020230117120356.png)
+ ![](../../z_images/Pasted%20image%2020230117120300.png)

 ### Pipeline with ROB
+ latency overhead
+ ![](../../z_images/Pasted%20image%2020230117120532.png)

### Efficient ROB Access
+ ![](../../z_images/Pasted%20image%2020230117120659.png)
+ ![](../../z_images/Pasted%20image%2020230117120755.png)

### Out-of-Order Dispatch Scheduler
+ in-order dispatch has dependencies on prior instructions
+ solution: fire instruction, when inputs are ready
+ ![](../../z_images/Pasted%20image%2020230117121755.png)
+ ![](../../z_images/Pasted%20image%2020230117121859.png)