### Overview
+ all these games (and many more) can be reduced to NIM
+ NIM rules
	+  
+ ![](../../../z_images/Pasted%20image%2020231102153544.png)

### Prime Game
+ ![](../../../z_images/Pasted%20image%2020231102124826.png)
+ each integer with k prime factors corresponds to a coin pile with k coins
+ pile height = number of coins = number of prime factors

###  Poker NIM
+ ![](../../../z_images/Pasted%20image%2020231102125006.png)
+ exactly the same as NIM with finite number of coins in the pool
+ placing coins from the pool just postpones the game end
	+ opponent just removes the coins you just placed

### Northcott’s Game
+ ![](../../../z_images/Pasted%20image%2020231102145821.png)
+ asymmetric version of Poker NIM
+ each row corresponds to a pile
	+ number of spaces between the coins = pile height
	+ spaces behind a coin (inaccessible for the opponent) = number of coins in the pool

### Kayles
+ ![](../../../z_images/Pasted%20image%2020231102150228.png)
+ Dawson’s Kayles
	+ always hit two neighbored pins
	+ remove single pins

### Monochromatic Triangle
+ ![](../../../z_images/Pasted%20image%2020231102150637.png)
+ same as Dawson’s Kayles

### Triangulation Coloring Game
+ ![](../../../z_images/Pasted%20image%2020231102150717.png)
+ dual structure
	+ voronoi diagram
	+ coloring an edge removes its triangle
		+ ![](../../../z_images/Pasted%20image%2020231102153357.png)
	+ may optionally also split the pile
		+ ![](../../../z_images/Pasted%20image%2020231102153302.png)
+ reduces to Kayles

