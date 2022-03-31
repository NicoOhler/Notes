# Spreading activation
### Basic Principle
+ node spreads to directly connected nodes
+ these nodes further spread to connected nodes
+ repeat

### Spreading Conditions
+ activation value (max 1, min 0)
	+ for each initially activated node (spreader)
+ activation threshold
	+ activation value above threshold ==> spread
+ decay value
	+  the further away from origin
	+  the more it decays/less likely to spread
+ termination criteria
	+ e.g. fixed number of cycles


[[Graphs]]