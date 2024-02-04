+ [[Shortest Path Algorithms]] for all vertex pairs
+ distance matrix is calculated directly
+  [[Dynamische Programmierung]]
+ compute a sequence of distance matrices $w_1,...,w_n$
	+ initial weight matrix $w$ as input
		+ ![](../../../z_images/Pasted%20image%2020231003131602.png)
	+ ![](../../../z_images/Pasted%20image%2020231003131657.png)
+ ![](../../../z_images/Pasted%20image%2020231003131746.png)
+ proof by induction
	+ ![](../../../z_images/Pasted%20image%2020231003132338.png)
	+ $w_{k-1}$ may use $v_k$  as start or end point but not as intermediate
	+ ![](../../../z_images/Pasted%20image%2020231003132304.png)
	+ ![](../../../z_images/Pasted%20image%2020231003132940.png)
+ pseudo code
	+ ![](../../../z_images/Pasted%20image%2020231003133023.png)
+ ![](../../../z_images/Pasted%20image%2020231003133138.png)
+ ![](../../../z_images/Pasted%20image%2020231003133536.png)
