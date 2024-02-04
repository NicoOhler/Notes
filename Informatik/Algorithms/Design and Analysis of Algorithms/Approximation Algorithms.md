### Overview
+ close to optimal solutions
+ provable guarantees on the solution quality
+ often a simple greedy algorithm
+ ![[../../../z_images/Pasted image 20231201214248.png]]
	+ ![[../../../z_images/Pasted image 20231201214340.png]]

### Minimum Vertex Cover
+ ![[../../../z_images/Pasted image 20231201214519.png]]
+ NP-complete
+ “vertex greedy” algorithm
	+ ![[../../../z_images/Pasted image 20231201215110.png]]
	+ ![[../../../z_images/Pasted image 20231201215357.png]]
+ “edge greedy” algorithm
	+ ApproximateVertexCover
	+ ![[../../../z_images/Pasted image 20231201215452.png]]
	+ better approximation guarantee than “greedy vertex”
	+ must not be always better
	+ 2-approximation
		+ ![[../../../z_images/Pasted image 20231202101902.png]]
		+ ![[../../../z_images/Pasted image 20231202102003.png]]

### Set Cover
+ ![[../../../z_images/Pasted image 20231202102258.png]]
+ NP-complete
+ greedy algorithm
	+ ![[../../../z_images/Pasted image 20231202102602.png]]
	+ add the set with a maximum number of not yet covered elements
	+ repeat until all elements are covered => correct
	+ approximation factor
		+ ![[../../../z_images/Pasted image 20231202103224.png]]
		+ ![[../../../z_images/Pasted image 20231202104110.png]]
			+ $1-x\le e^{-x}$   

### Partition Problem
+ ![[../../../z_images/Pasted image 20231202104434.png]]
	+ balance both partitions
+ NP-complete
+ ![[../../../z_images/Pasted image 20231202104450.png]]
+ Polynomial time approximation scheme
	+ ![[../../../z_images/Pasted image 20231202104842.png]]
	+ ![[../../../z_images/Pasted image 20231202105006.png]]
	+ ![[../../../z_images/Pasted image 20231202105032.png]]
	+ approximation factor
		+ ![[../../../z_images/Pasted image 20231202105317.png]]
		+ perfect balancing as lower bound
			+ ![[../../../z_images/Pasted image 20231202105421.png]]
		+ ![[../../../z_images/Pasted image 20231202105742.png]]
		+ ![[../../../z_images/Pasted image 20231202110428.png]]
			+ $s_k \le \frac{2L}{m}$ since all integers are positive
			+ last line of approximation works because of
				+ $m=\lceil \frac{1}{\epsilon}\rceil - 1$ 
		+ ![[../../../z_images/Pasted image 20231202110835.png]]