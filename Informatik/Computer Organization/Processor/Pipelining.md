### Motivation
+ Fließbandprinzip
	+ each component has own dedicated task
	+ invented by Henry Ford
+ pipeline the execution of multiple instructions
	+ assembly line of instructions
+ divide instruction processing into distinct stages
	+ different instruction executed each stage
	+ requires additional registers between each stage
	+ ![](../../z_images/Pasted%20image%2020221112175053.png)

### Example
+ four independent ADDs
	+ ![](../../z_images/Pasted%20image%2020221112165103.png)
+ laundry analogy
	+ compensate being slow on specific stage
	+ multiple instance of slow stage
	+ ![](../../z_images/Pasted%20image%2020221112165413.png)

### Ideal Pipelining
+ ![](../../z_images/Pasted%20image%2020221112165539.png)

### Control Signals
+ signals piped through and used when needed
+ ![](../../z_images/Pasted%20image%2020221112181239.png)

### RAW Dependence Handling
+ RAW - read after write
+ sometimes result needed by instruction not calculated yet
	+ e.g. 2nd instruction needs value from first
	+ which has not finished yet
	+ ![](../../z_images/Pasted%20image%2020221112181748.png)
+ stall
	+ wait until data value available
	+ ![](../../z_images/Pasted%20image%2020221112181908.png)
+ dependence detection
	+ scoreboarding
		+ each registers has valid bit
		+ instruction writing to register resets valid bit
		+ instruction in decode stage needs to check if all source registers are valid
	+ data forwarding/bypassing
		+ forward result to dependent instruction as soon as available
		+ hazard unit detects dependencis between instructions
		+ ![](../../z_images/Pasted%20image%2020221113104357.png)