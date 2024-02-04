### Motivation
+ [[Combinational Circuits]] are not capable of storing data
	+ changes to input lead to change at output
+ storage by creating a feedback loop

### Set-Reset Latch - NOR Version
+ ![](Pasted%20image%2020221014143700.png)
+ set
	+ ![](Pasted%20image%2020221031160611.png)
+ release set input
	+ ![](Pasted%20image%2020221031160640.png)
+ reset
	+ ![](Pasted%20image%2020221031160739.png)
+ release reset
	+ ![](Pasted%20image%2020221031160748.png)
+ illegal action
	+ ![](Pasted%20image%2020221031160822.png)

### (A)synchronous circuits
+ synchronous circuits with global clock signal
	+ most commonly used
	+ no latches as storage
	+ instead uses flip-flops or registers
		+ sets output to data input on each rising clock edge
		+ ![](Pasted%20image%2020221031161218.png)
	+ 1-bit storage - flip-flop
	+ n-bit storage - register
+ asychronous circuits
	+ very rare

### Combination of Registers and [[Combinational Circuits]]
+ ![](Pasted%20image%2020221031161649.png)