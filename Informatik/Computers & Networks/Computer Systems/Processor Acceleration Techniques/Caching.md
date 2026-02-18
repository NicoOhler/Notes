### Speculative Execution
+ ![](Pasted%20image%2020230117122754.png)
+ speculate outcome and which branch will be executed
	+ store results in ROB
	+ trash result if prediction incorrect
+ ![](Pasted%20image%2020230117122950.png)
+ side effects
	+ ![](Pasted%20image%2020230117123027.png)

### Memory Hierarchy
+ ideal memory
	+ ![](Pasted%20image%2020230117123313.png)
	+ requirements contradict each other
		+ more capacity => slower
		+ higher bandwidth => more expensive
		+ lower latency => more expensive
+ ![](Pasted%20image%2020230117123711.png)
+ create multiple levels of storage types
	+ storage with different properties
		+ register file
		+ cache
		+ DRAM
		+ hard disk
	+ use fast small as well as big slow memory
	+ ![](Pasted%20image%2020230117123800.png)

### Locality
+ use past behaviour to predict near future
+ ![](Pasted%20image%2020230117124402.png)
+ ![](Pasted%20image%2020230117124441.png)

### Automatic Memory Management
+ ![](Pasted%20image%2020230117124507.png)
+ ![](Pasted%20image%2020230117124557.png)
+ automatically manage/move data across levels
	+ handled manually
		+ registers
		+ between DRAM and hard disk 
	+ modern memory hierarchy
		+ ![](Pasted%20image%2020230117124725.png)

### Latency Analysis
+ ![](Pasted%20image%2020230117125154.png)

### Cache
+ ![](Pasted%20image%2020230117125309.png)
+ design decisions
	+ ![](Pasted%20image%2020230117125423.png)
+ abstraction
	+ ![](Pasted%20image%2020230117125843.png)
+ implementation
	+ divide RAM into $2^n$ subsets
		+ store one subset in cache
		+ each subset can be identified with n-bit tag
			+ first $n$-bits of RAM address equal to tag
		+ repeated between cache layers
			+ L1 cache
			+ L2 cache
			+ ...
	+ actually multiple subset in mutliple cache locations
		+ map first k subsets to first cache location
			+ repeated for following subsets
	+ address converted to
		+ tag
		+ index
		+ offset
	+ actual workflow for data access
		+  use cache location with index
			+ check if its tag equal to address tag
			+ if yes, use offset to access data
+ example
	+ ![](Pasted%20image%2020230117131811.png)
