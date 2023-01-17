### Basic Idea
+ add hardware to handle multiple instructions truly parallel
	+ fetch multiple instructions simulatenously
	+ schedule [[Multi-Cycle Execution]]
+ ![[Pasted image 20230117122218.png]]
	+ ![[Pasted image 20230117122241.png]]
+ superscalar pipeline for each CPU core
+ bottle neck
	+ slow memory access
	+ single memory access could take hundreds of CPU cycles

### Speculative Execution
+ ![[Pasted image 20230117122754.png]]
+ speculate outcome and which branch will be executed
	+ store results in ROB
	+ trash result if prediction incorrect
+ ![[Pasted image 20230117122950.png]]
+ side effects
	+ ![[Pasted image 20230117123027.png]]

### Memory Hierarchy
+ ideal memory
	+ ![[Pasted image 20230117123313.png]]
	+ requirements contradict each other
		+ more capacity => slower
		+ higher bandwidth => more expensive
		+ lower latency => more expensive
+ ![[Pasted image 20230117123711.png]]
+ create multiple levels of storage types
	+ different properties
	+ use fast small as well as big slow memory
	+ ![[Pasted image 20230117123800.png]]
	+ 
