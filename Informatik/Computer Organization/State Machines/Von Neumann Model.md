### Limitations of [[Finite State Machines]]
+ previous state machines designed for specific application
+ application changes require new state machine, new hardware
+ general-purpose machine wanted

### Von Neumann Model
+ architecture with following components
	+ ![[Pasted image 20221101163042.png]]
+ CPU connected via bus system to memory and I/O
	+ ![[Pasted image 20221101163214.png]]
+ Hardvard Architecture Variation
	+ Memory split into Data and Instruction Memory

### Arithmetic Logic Unit
+ ALUs are [[Combinational Circuits]] performing calculation operations
+ basic properties
	+ ![[Pasted image 20221101163430.png]]

### Register File
+ contatins m n-bit registers
+ write one n-bit value per clock cycle
	+ register selected via $R_W$
	+ does not write if low
+ read two registers per clock cycle
	+ provided at outputs A and B
	+ registers selected via $R_A$ and $R_B$
+ basically memory with
	+ one write port
	+ two read ports
+ ![[Pasted image 20221101163955.png]]
+ register file with 32 registers
	+ ![[Pasted image 20221101164143.png]]

### Processing Unit
+ combines ALU and register file
	+ ![[Pasted image 20221101183415.png]]
+ instruction register
	+ stores instruction to execute and parameters
	+ mapped to control signals by instruction encoder
	+ ![[Pasted image 20221101164537.png]]

