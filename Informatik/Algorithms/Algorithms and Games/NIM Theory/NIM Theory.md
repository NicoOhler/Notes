### Sprague-Grundy-Theory
+ First/Second-Player Win depends on number of coins
	+ for a single pile
	+ ![](../../../../z_images/Pasted%20image%2020231102154334.png)
+ Nimbers
	+ ![](../../../../z_images/Pasted%20image%2020231102154538.png)
	+ ![](../../../../z_images/Pasted%20image%2020231102155002.png)
	+ nimber depends on height
		+ ![](../../../../z_images/Pasted%20image%2020231102163555.png)

### NIM Rules
+ ![](../../../../z_images/Pasted%20image%2020231102155453.png)
+ ![](../../../../z_images/Pasted%20image%2020231102163158.png)
	+ ![](../../../../z_images/Pasted%20image%2020231102164346.png)

### Optimal Strategy
+ compute each pile’s nimber
+ XOR to find out if a winning move exists
	+ zero $\Rightarrow$ no winning move
+ compute for each pile if there is a winning move for this pile
+ execute a optimal move
+ repeat after opponent’s move
+ ![](../../../../z_images/Pasted%20image%2020231102172055.png)

### Variations of [[NIM-type Games]]
+ take a limited number of coins each turn
	+ ![](../../../../z_images/Pasted%20image%2020231102172856.png)
+ take 1 coin or split a pile into two (non-empty) piles
	+ ![](../../../../z_images/Pasted%20image%2020231103222956.png)
+ Laskers NIM
	+ NIM or split a pile into two (non-empty) piles
	+ ![](../../../../z_images/Pasted%20image%2020231103223843.png)
	+ ![](../../../../z_images/Pasted%20image%2020231103224538.png)
+ Kayles and Dawson’s Kayles
	+ no repeating nimber patterns

[[Algorithms and Games]]
