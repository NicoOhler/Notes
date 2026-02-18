### Types of [[Finite State Machines]]
+ ![](Pasted%20image%2020221031173538.png)
+ mealy machines have different outputs for the same state
	+ output written outside of state circle
	+ next to state transition
	+ value of input affect timing diagram
	+ ![](Pasted%20image%2020221031173749.png)
	+ ![](Pasted%20image%2020221031173711.png)
+ machine combinations
	+ multiple moore machines cause no problems
		+ ![](Pasted%20image%2020221031174731.png)
	+ moore with mealy machine cause no problems
	+ two mealy machine may cause problems
		+ one needs to avoid combinational loops
		+ ![](Pasted%20image%2020221031174837.png)