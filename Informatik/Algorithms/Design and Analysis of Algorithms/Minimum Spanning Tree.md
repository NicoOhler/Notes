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
	+ ![](../../../z_images/Pasted%20image%2020231002215908.png)
+ crossing free (planar)
	+ otherwise using different edges would lead to a fewer length
+ example
	+ ![](../../../z_images/Pasted%20image%2020231002215945.png)

### Algorithm Idea
+ cut
	+ ![](../../../z_images/Pasted%20image%2020231002220647.png)
+ ![](../../../z_images/Pasted%20image%2020231002220800.png)
	+ proof
		+ ![](../../../z_images/Pasted%20image%2020231002220952.png)

### Prim’s Algorithm
+ greedy
+ also works with negative weights
+ ![](../../../z_images/Pasted%20image%2020231002221216.png)
+ pseudo code
	+ ![](../../../z_images/Pasted%20image%2020231002221245.png)
+ ![](../../../z_images/Pasted%20image%2020231002221621.png)
+ ![](../../../z_images/Pasted%20image%2020231002221629.png)
+ ![](../../../z_images/Pasted%20image%2020231002221854.png)

### Kruskal’s Algorithm
+ greedy
+ also works with negative weights
+ uses [[Union Find]] data structure
	+ ![](../../../z_images/Pasted%20image%2020231002222057.png)
	+ ![](../../../z_images/Pasted%20image%2020231002222251.png)
+ ![](../../../z_images/Pasted%20image%2020231002221954.png)
+ pseudo code
	+ ![](../../../z_images/Pasted%20image%2020231002222312.png)
+ ![](../../../z_images/Pasted%20image%2020231002222545.png)
+ ![](../../../z_images/Pasted%20image%2020231002222616.png)
+ 