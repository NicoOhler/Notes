### Overview
+ solve a problem using multiple distributed devices
	+ data might not fit onto a single device
		+ disk cluster
	+ maybe All-to-all communication
		+ no locality restrictions
		+ bandwidth restrictions
+ output may be just a part of the solution
+  time complexity wrt communication rounds instead of computation time
	+ efficient = $poly log(n) << n$
	+ $log^{*}n$
		+ ![[Pasted image 20231201200005.png]]

### Vertex Coloring
+ symmetry breaking
	+ mutual exclusive access to shared resource
	+ colors = time slots => resource scheduling
+ ![[Pasted image 20231201194921.png]]
+ color local minima vertices first
	+ minima if no neighbor has a higher IP
	+ extremely slow
	+ linear time
+ random coloring
	+ ![[Pasted image 20231201204548.png]]
	+ ![[Pasted image 20231201204739.png]]

### Linial’s Algorithm
+ theorems
	+ ![[Pasted image 20231201200321.png]]
	+ ![[Pasted image 20231201200306.png]]
		+ $\Delta=$ highest degree
	+ Linial’s color reduction
		+ ![[Pasted image 20231201200827.png]]
		+ ![[Pasted image 20231201201111.png]]
			+ ![[Pasted image 20231201201312.png]]
			+ ![[Pasted image 20231201201830.png]]
			+ small intersection set
				+ ![[Pasted image 20231201202049.png]]
			+ ![[Pasted image 20231201202233.png]]
+ ![[Pasted image 20231201202254.png]]

### Maximal Independent Set
+ ![[Pasted image 20231201202450.png]]
+ at the end each node knows whether is in the independent set
+ different from the maximum independent set problem
	+ independent set need not be of maximum size
+ naive centralized greedy algorithm
	+ ![[Pasted image 20231201203123.png]]
+ distributed version
	+ ![[Pasted image 20231201203355.png]]
	+ executed by each node $v$ in parallel/synchronous
	+ ![[Pasted image 20231201203425.png]]
	+ coloring acts as scheduler
	+ notifying/asking neighbors
		+  implementation dependent
		+ may take 2 additional rounds
		+ does not change time complexity
	+ ![[Pasted image 20231201203834.png]]
+ ![[Pasted image 20231201204110.png]]
	+ ![[Pasted image 20231201204056.png]]
	+ ![[Pasted image 20231201204144.png]]
	+ ![[Pasted image 20231201204201.png]]
	+ ![[Pasted image 20231201204306.png]]