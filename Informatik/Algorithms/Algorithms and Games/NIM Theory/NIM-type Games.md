### Overview
+ all these games (and many more) can be reduced to NIM
+ NIM rules
	+  
+ ![[Pasted image 20231102153544.png]]

### Prime Game
+ ![[Pasted image 20231102124826.png]]
+ each integer with k prime factors corresponds to a coin pile with k coins
+ pile height = number of coins = number of prime factors

###  Poker NIM
+ ![[Pasted image 20231102125006.png]]
+ exactly the same as NIM with finite number of coins in the pool
+ placing coins from the pool just postpones the game end
	+ opponent just removes the coins you just placed

### Northcott’s Game
+ ![[Pasted image 20231102145821.png]]
+ asymmetric version of Poker NIM
+ each row corresponds to a pile
	+ number of spaces between the coins = pile height
	+ spaces behind a coin (inaccessible for the opponent) = number of coins in the pool

### Kayles
+ ![[Pasted image 20231102150228.png]]
+ Dawson’s Kayles
	+ always hit two neighbored pins
	+ remove single pins

### Monochromatic Triangle
+ ![[Pasted image 20231102150637.png]]
+ same as Dawson’s Kayles

### Triangulation Coloring Game
+ ![[Pasted image 20231102150717.png]]
+ dual structure
	+ voronoi diagram
	+ coloring an edge removes its triangle
		+ ![[Pasted image 20231102153357.png]]
	+ may optionally also split the pile
		+ ![[Pasted image 20231102153302.png]]
+ reduces to Kayles
