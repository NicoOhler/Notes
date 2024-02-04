### Overview
+ close to optimal solutions
+ provable guarantees on the solution quality
+ often a simple greedy algorithm
+ ![](Pasted%20image%2020231201214248.png)
	+ ![](Pasted%20image%2020231201214340.png)

### Minimum Vertex Cover
+ ![](Pasted%20image%2020231201214519.png)
+ NP-complete
+ “vertex greedy” algorithm
	+ ![](Pasted%20image%2020231201215110.png)
	+ ![](Pasted%20image%2020231201215357.png)
+ “edge greedy” algorithm
	+ ApproximateVertexCover
	+ ![](Pasted%20image%2020231201215452.png)
	+ better approximation guarantee than “greedy vertex”
	+ must not be always better
	+ 2-approximation
		+ ![](Pasted%20image%2020231202101902.png)
		+ ![](Pasted%20image%2020231202102003.png)

### Set Cover
+ ![](Pasted%20image%2020231202102258.png)
+ NP-complete
+ greedy algorithm
	+ ![](Pasted%20image%2020231202102602.png)
	+ add the set with a maximum number of not yet covered elements
	+ repeat until all elements are covered => correct
	+ approximation factor
		+ ![](Pasted%20image%2020231202103224.png)
		+ ![](Pasted%20image%2020231202104110.png)
			+ $1-x\le e^{-x}$   

### Partition Problem
+ ![](Pasted%20image%2020231202104434.png)
	+ balance both partitions
+ NP-complete
+ ![](Pasted%20image%2020231202104450.png)
+ Polynomial time approximation scheme
	+ ![](Pasted%20image%2020231202104842.png)
	+ ![](Pasted%20image%2020231202105006.png)
	+ ![](Pasted%20image%2020231202105032.png)
	+ approximation factor
		+ ![](Pasted%20image%2020231202105317.png)
		+ perfect balancing as lower bound
			+ ![](Pasted%20image%2020231202105421.png)
		+ ![](Pasted%20image%2020231202105742.png)
		+ ![](Pasted%20image%2020231202110428.png)
			+ $s_k \le \frac{2L}{m}$ since all integers are positive
			+ last line of approximation works because of
				+ $m=\lceil \frac{1}{\epsilon}\rceil - 1$ 
		+ ![](Pasted%20image%2020231202110835.png)