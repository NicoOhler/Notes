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
	+ ![](Pasted%20image%2020221031164002.png)
+ may have inputs which influence next state
+ may also have outputs 
	+ written into state circles
	+ called Moore machines
+ ![](Pasted%20image%2020221031164304.png)
+ timing diagram
	+ ![](Pasted%20image%2020221031164130.png)

### Mapping State Diagram to Hardware
+ ![](Pasted%20image%2020221031164948.png)
+ state encoding
	+ ![](Pasted%20image%2020221031165128.png)
+ state transition table
	+ next state logic
		+ ![](Pasted%20image%2020221031165355.png)
		+ ![](Pasted%20image%2020221031165437.png)
	+ ![](Pasted%20image%2020221031165242.png)
+ output function
	+ 2, 3, 4 => 3 bit output
	+ ![](Pasted%20image%2020221031165526.png)
	+ ![](Pasted%20image%2020221031165618.png)
+ structural diagram of FSM
	+ ![](Pasted%20image%2020221031165747.png)
+ hardware implementation
	+ ![](Pasted%20image%2020221031165853.png)

### SystemVerilog Implementation
+ ![](Pasted%20image%2020221031165957.png)
