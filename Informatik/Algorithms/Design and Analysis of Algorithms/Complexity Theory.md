### Relations between Problems
+ some problems can be solved using an algorithm for another problem
+ reduction
	+ e.g. problem B can be efficiently solved if there is an efficient algorithm for problem A
	+ B cannot be fundamentally harder than A $\iff$ A cannot be fundamentally easier than B
	+ $B ≤_x A$
		+ B can be reduced to A
		+ solving B with the help of A 

### Reducing City Tour to Dinner Party
+ similarity
	+ view both problems as graphs
	+ “differently reachable from …” $\iff$ “liked by …”
+ difference
	+ cycle must be closed for the dinner party
+ conclusions
	+ if there is a tour $\Rightarrow$ there is a possible seating order
	+ if there is a seating $\Rightarrow$ finding a tour path is easy
		+ no tour $\Rightarrow$ no seating
	+ ![[Pasted image 20231003170559.png]]
+ the dinner party problem can be also reduced to the city tour problem

### Complexity Classes
+ P
	+ decision problems solvable in polynomial time
+ NP
	+ decision problems solvable in nondeterministic polynomial time 
	+ solution is verifiable in polynomial time given a certificate (e.g. a solution)
+ PSPACE
	+ decision problems solvable using a polynomial amount of memory
	+ disregards time complexity
+ EXPTIME
	+ decision problems solvable in exponential time
+ Undecidable
	+ problems which cannot be solved no matter how much time or space is allowed
	+ must be proven that no such algorithm exists
+ ![[Pasted image 20231003172704.png]]

### Types of Polynomial Time Reductions
+ ![[Pasted image 20231003173203.png]]
+ ![[Pasted image 20231003173301.png]]
	+ special case of Cook reductions
+ ![[Pasted image 20231003173516.png]]

### NP-completeness
+ Problem B is NP-complete if
	+ B ∈ NP
	+ B is NP-hard
		+ ![[Pasted image 20231003173825.png]]
+ ![[Pasted image 20231003175028.png]]
+ ways to show that B is NP-complete
	+ ![[Pasted image 20231003174119.png]]
		+ possibility 2 works because 
			+ ![[Pasted image 20231115155357.png]]
				+ all problems in NP can be reduced to C
					+ since C is NP-complete
				+ C can be reduced to B
				+ ![[Pasted image 20231003174042.png]]
	+ must also show that B ∈ NP
		+ otherwise B might be NP-hard but B ∉ NP
+ ways to show that B is NP-hard
	+ reduce a NP-hard problem to B
