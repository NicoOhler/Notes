### Join Ordering Problem
+ given a join query graph, find the optimal join ordering
+ usually NP-hard
	+ polynomical algorithms exist for special cases
+ search space sizes
	+ ![](../../../z_images/Pasted%20image%2020220512145848.png)

### Join Order Seach Strategies
+ tradeoff between optimal plan and compile time
+ ![](../../../z_images/Pasted%20image%2020220512150207.png)
+ naive full enumeration
	+ infeasible for large queries
+ exact dynamic programming
	+ guarantees optimal plan
	+ often too expensive (beyond 20 relations)
	+ bottom-up/top-down approach
+ greedy/heuristic algorithms
	+ tests out some
	+ ignore worst
	+ further optimization on best
		+ e.g. random mutations (as with genetics)
+ approximate algorithms
+ ![](../../../z_images/Pasted%20image%2020220512150247.png)

### Greedy Join Ordering
+ does not always return optimal join ordering
+ algorithm:
	+ calculate cost of each two table join combination
	+ calculate costs of previous join with next table
	+ repeat until every table is used
+ example
	+ ![](../../../z_images/Pasted%20image%2020220512150833.png)

### Dynamic Programming Join Ordering
+ exact enumeration via dynamic programming
	+ tries to find optimal substructures first
	+ overlapping subproblems allow for memoization
		+ reuse already retrieved data
+ e.g. DPSize
	+ bottom-up
	+ split into independent subproblems
	+ solve subproblems
	+ combine solutions
	+ ![](../../../z_images/Pasted%20image%2020220512151517.png)

[[Plan Optimization]]