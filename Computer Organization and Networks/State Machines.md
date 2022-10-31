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
+ 