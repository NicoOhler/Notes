### Motivation
+ not all instructions need same amount of time when [[Pipelining]]
+ idea: mutiple different functional units
	+ take different numbers of cycles
	+ ![[Pasted image 20230117115624.png]]
	+ ![[Pasted image 20230117115926.png]]
+ Problem
	+ instructions might rely on results of previous instructions 
	+ "contract"
		+ ![[Pasted image 20230117120051.png]]

### Reorder Buffer (ROB)
+ ![[Pasted image 20230117120146.png]]
+ ![[Pasted image 20230117120320.png]]
+ ![[Pasted image 20230117120356.png]]
+ ![[Pasted image 20230117120300.png]]

 ### Pipeline with ROB
+ latency overhead
+ ![[Pasted image 20230117120532.png]]

### Efficient ROB Access
+ ![[Pasted image 20230117120659.png]]
+ ![[Pasted image 20230117120755.png]]

### Out-of-Order Dispatch Scheduler
+ in-order dispatch has dependencies on prior instructions
+ solution: fire instruction, when inputs are ready
+ ![[Pasted image 20230117121755.png]]
+ ![[Pasted image 20230117121859.png]]