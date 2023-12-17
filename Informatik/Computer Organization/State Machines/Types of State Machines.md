### Types of [[Finite State Machines]]
+ ![[Pasted image 20221031173538.png]]
+ mealy machines have different outputs for the same state
	+ output written outside of state circle
	+ next to state transition
	+ value of input affect timing diagram
	+ ![[Pasted image 20221031173749.png]]
	+ ![[Pasted image 20221031173711.png]]
+ machine combinations
	+ multiple moore machines cause no problems
		+ ![[Pasted image 20221031174731.png]]
	+ moore with mealy machine cause no problems
	+ two mealy machine may cause problems
		+ one needs to avoid combinational loops
		+ ![[Pasted image 20221031174837.png]]