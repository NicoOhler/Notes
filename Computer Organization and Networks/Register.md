# Sequential Circuits
### Motivation
+ [[Combinational Circuits]] are not capable of storing data
	+ changes to input lead to change at output
+ storage by creating a feedback loop

### Set-Reset Latch - NOR Version
+ ![[Pasted image 20221014143700.png]]
+ set
	+ ![[Pasted image 20221031160611.png]]
+ release set input
	+ ![[Pasted image 20221031160640.png]]
+ reset
	+ ![[Pasted image 20221031160739.png]]
+ release reset
	+ ![[Pasted image 20221031160748.png]]
+ illegal action
	+ ![[Pasted image 20221031160822.png]]

### (A)synchronous circuits
+ synchronous circuits with global clock signal
	+ most commonly used
	+ no latches as storage
	+ instead uses flip-flops or registers
		+ sets output to data input on each rising clock edge
		+ ![[Pasted image 20221031161218.png]]
	+ 1-bit storage - flip-flop
	+ n-bit storage - register
+ asychronous circuits
	+ very rare

### Combination of Registers and [[Combinational Circuits]]
+ ![[Pasted image 20221031161649.png]]