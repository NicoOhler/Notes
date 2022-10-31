### Finite State Machines - Automaton

+ synchronous FSM clocked by clock signal and [[Clock Frequency]]
+ each clock period has defined current state
+ machine advances into next defined state after each rising edge

### State Diagram
+ defines sequence of states
+ initial state defined
+ circle with symbolic names for each state
+ arrows define sequence
	+ can be described in state transition table
	+ ![[Pasted image 20221031164002.png]]
+ may have inputs which influence next state
+ may also have outputs 
	+ written into state circles
	+ called Moore machines
+ ![[Pasted image 20221031164304.png]]
+ timing diagram
	+ ![[Pasted image 20221031164130.png]]

### Mapping State Diagram to Hardware
+ ![[Pasted image 20221031164948.png]]
+ state encoding
	+ ![[Pasted image 20221031165128.png]]
+ state transition table
	+ next state logic
		+ ![[Pasted image 20221031165355.png]]
		+ ![[Pasted image 20221031165437.png]]
	+ ![[Pasted image 20221031165242.png]]
+ output function
	+ 2, 3, 4 => 3 bit output
	+ ![[Pasted image 20221031165526.png]]
	+ ![[Pasted image 20221031165618.png]]
+ structural diagram of FSM
	+ ![[Pasted image 20221031165747.png]]
+ hardware implementation
	+ ![[Pasted image 20221031165853.png]]

### SystemVerilog Implementation
+ ![[Pasted image 20221031165957.png]]
+ 