### Basic Principle
+ node spreads to directly connected nodes
+ these nodes further spread to connected nodes
+ repeat

### Spreading Conditions
+ activation value AV (max 1, min 0)
	+ for each initially activated node
	+ AV(i,t1) - AV of index i at time t1
+ activation threshold
	+ if AV above threshold 
	+ spread to adjacent nodes
	+ those spread even further if AV above threshold again
+ decay value D
	+  the further away from origin
	+  the more it decays/less likely to spread
+ termination criteria
	+ e.g. fixed number of cycles
+ activation value of newly activated nodes
	+ $AV(j,t2)=AV(j,t1) + AV(i,t1)*A(i,j)*D$


[[Graphs KR]]