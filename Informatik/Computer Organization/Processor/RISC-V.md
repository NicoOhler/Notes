### RISC-V 
+ [[Instruction Set Architecture]]
+ properties
	+ ![](Pasted%20image%2020221101170500.png)
+ Instruction Set
	+ ![](Pasted%20image%2020221101170610.png)
+ ALU and register file are 32-bit
+ register files consists of 32 registers
	+ register x0 always stores zero
	+ allows transformation of operations 
		+ add(destination,a,b) => add(dest, a, 0) = move(a, dest)

### Instruction Encoding
+ stores operation to execute and parameters
+ terminology
	+ ![](Pasted%20image%2020221101171520.png)
+ instruction types
	+ R-Type
		+ perform arithmetic and logic operations based on two input registers
		+ ![](Pasted%20image%2020221101171954.png)
		+ ![](Pasted%20image%2020221101172026.png)
	+ I-Type
	+ S-Type
	+ U-Type
