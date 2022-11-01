### RISC-V 
+ [[Instruction Set Architecture]]
+ properties
	+ ![[Pasted image 20221101170500.png]]
+ Instruction Set
	+ ![[Pasted image 20221101170610.png]]
+ ALU and register file are 32-bit
+ register files consists of 32 registers
	+ register x0 always stores zero
	+ allows transformation of operations 
		+ add(destination,a,b) => add(dest, a, 0) = move(a, dest)

### Instruction Encoding
+ stores operation to execute and parameters
+ terminology
	+ ![[Pasted image 20221101171520.png]]
+ instruction types
	+ R-Type
		+ perform arithmetic and logic operations based on two input registers
		+ ![[Pasted image 20221101171954.png]]
		+ ![[Pasted image 20221101172026.png]]
	+ 
	+ S-Type
	+ U-Type
