### Design Flow
+ ![[Pasted image 20221112162719.png]]

### Single Cycle Datapath
+ overview
	+ ![[Pasted image 20221112163652.png]]
+ each instruction takes one cycle to execute
	+ maximum clock frequency defined by slowest instruction

### Performance
+ goal to maximise instruction executions per time
+ determined by
	+ clock cycles per instruction CPI
	+ [[Clock Frequency]], cycles per second
+ program with N instruction takes $N*CPI*(1/f)$

### Multicycle Architecture
+ operations needed for one instruction
	+ split up into more fine granular operations
+ 