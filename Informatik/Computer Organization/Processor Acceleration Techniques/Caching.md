### Speculative Execution
+ ![[../../../z_images/Pasted image 20230117122754.png]]
+ speculate outcome and which branch will be executed
	+ store results in ROB
	+ trash result if prediction incorrect
+ ![[../../../z_images/Pasted image 20230117122950.png]]
+ side effects
	+ ![[../../../z_images/Pasted image 20230117123027.png]]

### Memory Hierarchy
+ ideal memory
	+ ![[../../../z_images/Pasted image 20230117123313.png]]
	+ requirements contradict each other
		+ more capacity => slower
		+ higher bandwidth => more expensive
		+ lower latency => more expensive
+ ![[../../../z_images/Pasted image 20230117123711.png]]
+ create multiple levels of storage types
	+ storage with different properties
		+ register file
		+ cache
		+ DRAM
		+ hard disk
	+ use fast small as well as big slow memory
	+ ![[../../../z_images/Pasted image 20230117123800.png]]

### Locality
+ use past behaviour to predict near future
+ ![[../../../z_images/Pasted image 20230117124402.png]]
+ ![[../../../z_images/Pasted image 20230117124441.png]]

### Automatic Memory Management
+ ![[../../../z_images/Pasted image 20230117124507.png]]
+ ![[../../../z_images/Pasted image 20230117124557.png]]
+ automatically manage/move data across levels
	+ handled manually
		+ registers
		+ between DRAM and hard disk 
	+ modern memory hierarchy
		+ ![[../../../z_images/Pasted image 20230117124725.png]]

### Latency Analysis
+ ![[../../../z_images/Pasted image 20230117125154.png]]

### Cache
+ ![[../../../z_images/Pasted image 20230117125309.png]]
+ design decisions
	+ ![[../../../z_images/Pasted image 20230117125423.png]]
+ abstraction
	+ ![[../../../z_images/Pasted image 20230117125843.png]]
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
	+ ![[../../../z_images/Pasted image 20230117131811.png]]
