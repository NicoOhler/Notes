### Sprague-Grundy-Theory
+ First/Second-Player Win depends on number of coins
	+ for a single pile
	+ ![[Pasted image 20231102154334.png]]
+ Nimbers
	+ ![[Pasted image 20231102154538.png]]
	+ ![[Pasted image 20231102155002.png]]
	+ nimber depends on height
		+ ![[Pasted image 20231102163555.png]]

### NIM Rules
+ ![[Pasted image 20231102155453.png]]
+ ![[Pasted image 20231102163158.png]]
	+ ![[Pasted image 20231102164346.png]]

### Optimal Strategy
+ compute each pile’s nimber
+ XOR to find out if a winning move exists
	+ even odd?
	+ not zero?
+ compute for each pile if there is a winning move for this pile
+ execute a optimal move
+ repeat after opponent’s move
+ ![[Pasted image 20231102172055.png]]

### Variations
+ take a limited number of coins each turn
	+ ![[Pasted image 20231102172856.png]]
+ take 1 coin or split a pile into two (non-empty) piles
	+ ![[Pasted image 20231103222956.png]]
+ Laskers NIM
	+ NIM or split a pile into two (non-empty) piles
	+ ![[Pasted image 20231103223843.png]]
	+ ![[Pasted image 20231103224538.png]]
+ Kayles and Dawson’s Kayles
	+ no repeating nimber patterns

[[Algorithms and Games]]