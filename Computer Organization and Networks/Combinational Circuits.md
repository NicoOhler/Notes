# Circuits
### Definition
+ Combination of [[Logic Gates]] with a specific layout on a chip

### Circuit Description Options
+ boolean functions using [[Boolean Algebra]]
+ truth tables
+ circuit netlist
	+ connected logic gates
+ hardware description language
	+ code that describes physical hardware
	+ default
	+ e.g. SystemVerilog
+ examples
	+ ![[Pasted image 20221014100827.png]]
	+ ![[Pasted image 20221014100914.png]]


### Application Specific Integrated Circuit ASIC
+ chip that physically realizes a given circuit
+ ![[Pasted image 20221014101730.png]]

### Field Programmable Gate Arrays FPGA
+ existing hardware configured to correspond to a given circuit
+ tradeoff between hardware and software
	+ more efficient but more expensive than software
	+ less efficient but less expensive than hardware
+ ![[Pasted image 20221014101850.png]]

### Logic Synthesis
+ process of mapping abstract circuit description to circuit netlist
+ ![[Pasted image 20221014102444.png]]

### Addition of [[Binary Numbers]]
+ adder (sum of two bits)
	+ three inputs
		+ two digits to add
		+ carry over
	+ two outputs
		+ digit of sum
		+ carry over
+ n-bit addition
	+ cascading these adders
	+ ![[Pasted image 20221014141349.png]]

