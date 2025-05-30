### Definition
+ ![](Pasted%20image%2020231124175136.png)
+ a flow is a function which returns the throughput as real number for each edge
	+ capacity constraints
		+ flow $f(u,v)$< capacity $c(u,v)$
	+ skew symmetry
		+ $f(u,v)=-f(v,u)$
		+ ![](Pasted%20image%2020231124175526.png)
	+ conservation of flow
		+ incoming flow = outcoming flow
		+ except for source and sink

### Ford-Fulkerson-Method
+ ![](Pasted%20image%2020231124180106.png)
+ residual capacity:
	+ $c_f(u,v)=c(u,v)-f(u,v)$
+ residual network
	+ ![](Pasted%20image%2020231124180409.png)
+ augmenting path
	+ path from s to t in $G_f$
	+ $c_f(p)=$ minimal residual capacity
+ augmenting a flow f along a path p
	+ for each flow along the path
		+ add/subtract min residual capacity
		+ ![](Pasted%20image%2020231124181857.png)
		+  $f+f_p$
+ pseudocode
	+ ![](Pasted%20image%2020231124182403.png)
+ correctness
	+ augmented version is a flow
		+ ![](Pasted%20image%2020231124182629.png)
	+ min-cut = maximum flow

### Max-Flow = Min-Cut Theorem
+ ![](Pasted%20image%2020231124183036.png)
+ ![](Pasted%20image%2020231124183418.png)
+ ![](Pasted%20image%2020231124183849.png)
	+ ![](Pasted%20image%2020231124183907.png)
	+ ![](Pasted%20image%2020231124184143.png)
	+ ![](Pasted%20image%2020231124184320.png)
	+ ![](Pasted%20image%2020231124184424.png)
+ ![](Pasted%20image%2020231124184715.png)
	+ does not hold for real-valued capacities 
+ finding a min-cut
	+ ![](Pasted%20image%2020231125102514.png)

### Edmonds-Karp-Algorithm
+ faster version of the Ford-Fulkerson-Method
	+ FF can be very slow even for small networks
	+ runtime depends on min capacity	
 + pseudo-code
	+ ![](Pasted%20image%2020231125102805.png)
+ ![](Pasted%20image%2020231125102812.png)
	+ ![](Pasted%20image%2020231125103101.png)
	+ ![](Pasted%20image%2020231125103612.png)
	+ ![](Pasted%20image%2020231125103900.png)
	+ ![](Pasted%20image%2020231125104033.png)

### Application
+ ![](Pasted%20image%2020231125104233.png)
+ ![](Pasted%20image%2020231125104349.png)