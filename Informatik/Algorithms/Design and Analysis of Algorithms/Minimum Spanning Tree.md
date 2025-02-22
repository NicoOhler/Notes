### Motivation
+ many algorithms can be applied to unweighted trees
	+ [[Spannbaumalgorithmen]]
	+ [[Breadth-First Search]]
	+ [[Depth-First Search]]
	+ …
+ does not work for weighted graphs
+ useful if direct connections from A to B not possible
	+ road networks
	+ electrical circuits
	+ …

### Definition
+ tree which connects all points which minimizes the total length of all edges
	+ ![](Pasted%20image%2020231002215908.png)
+ crossing free (planar)
	+ otherwise using different edges would lead to a fewer length
+ example
	+ ![](Pasted%20image%2020231002215945.png)

### Algorithm Idea
+ cut
	+ ![](Pasted%20image%2020231002220647.png)
+ ![](Pasted%20image%2020231002220800.png)
	+ proof
		+ ![](Pasted%20image%2020231002220952.png)

### Prim’s Algorithm
+ greedy
+ also works with negative weights
+ ![](Pasted%20image%2020231002221216.png)
+ pseudo code
	+ ![](Pasted%20image%2020231002221245.png)
+ ![](Pasted%20image%2020231002221621.png)
+ ![](Pasted%20image%2020231002221629.png)
+ ![](Pasted%20image%2020231002221854.png)

### Kruskal’s Algorithm
+ greedy
+ also works with negative weights
+ uses [[Union Find]] data structure
	+ ![](Pasted%20image%2020231002222057.png)
	+ ![](Pasted%20image%2020231002222251.png)
+ ![](Pasted%20image%2020231002221954.png)
+ pseudo code
	+ ![](Pasted%20image%2020231002222312.png)
+ ![](Pasted%20image%2020231002222545.png)
+ ![](Pasted%20image%2020231002222616.png)
+ 