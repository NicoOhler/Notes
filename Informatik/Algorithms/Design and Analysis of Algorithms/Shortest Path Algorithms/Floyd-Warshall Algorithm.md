+ [[Shortest Path Algorithms]] for all vertex pairs
+ distance matrix is calculated directly
+  [[Dynamische Programmierung]]
+ compute a sequence of distance matrices $w_1,...,w_n$
	+ initial weight matrix $w$ as input
		+ ![](Pasted%20image%2020231003131602.png)
	+ ![](Pasted%20image%2020231003131657.png)
+ ![](Pasted%20image%2020231003131746.png)
+ proof by induction
	+ ![](Pasted%20image%2020231003132338.png)
	+ $w_{k-1}$ may use $v_k$  as start or end point but not as intermediate
	+ ![](Pasted%20image%2020231003132304.png)
	+ ![](Pasted%20image%2020231003132940.png)
+ pseudo code
	+ ![](Pasted%20image%2020231003133023.png)
+ ![](Pasted%20image%2020231003133138.png)
+ ![](Pasted%20image%2020231003133536.png)
