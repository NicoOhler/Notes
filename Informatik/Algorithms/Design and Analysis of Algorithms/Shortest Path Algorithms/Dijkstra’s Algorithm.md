 + greedy [[Shortest Path Algorithms]] to find all destinations from one source
 + ![](../../../../z_images/Pasted%20image%2020231003124600.png)
+ ![](../../../../z_images/Pasted%20image%2020231003124609.png)
	+ Bellman Ford is an alternative for negative weights
+ ![](../../../../z_images/Pasted%20image%2020231003124705.png)
	+ similar to Prim’s algorithm [[Minimum Spanning Tree]]
		+ priority computation is different
	+ ![](../../../../z_images/Pasted%20image%2020231003124902.png)
+ pseudo code
	+ ![](../../../../z_images/Pasted%20image%2020231003125059.png)
+ ![](../../../../z_images/Pasted%20image%2020231003125219.png)
+ runtime may improve if Q is sorted
	+ ![](../../../../z_images/Pasted%20image%2020231003130719.png)
+ bad heuristics
	+ only considers distance from start to current vertex
	+ completely ignores distance from current vertex to goal
	+ therefore slow
	+ unlike [[A-Star Algorithm]]
