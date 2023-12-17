 + greedy [[Shortest Path Algorithms]] to find all destinations from one source
 + ![[Pasted image 20231003124600.png]]
+ ![[Pasted image 20231003124609.png]]
	+ Bellman Ford is an alternative for negative weights
+ ![[Pasted image 20231003124705.png]]
	+ similar to Prim’s algorithm [[Minimum Spanning Tree]]
		+ priority computation is different
	+ ![[Pasted image 20231003124902.png]]
+ pseudo code
	+ ![[Pasted image 20231003125059.png]]
+ ![[Pasted image 20231003125219.png]]
+ runtime may improve if Q is sorted
	+ ![[Pasted image 20231003130719.png]]
+ bad heuristics
	+ only considers distance from start to current vertex
	+ completely ignores distance from current vertex to goal
	+ therefore slow
	+ unlike [[A-Star Algorithm]]
