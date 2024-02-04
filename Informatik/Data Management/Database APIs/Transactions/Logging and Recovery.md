### Failure Types
+ transaction failures
	+ violated integrity constraints
	+ R1-Recovery: partial undo of uncommitted tx
+ system failures
	+ HW/OS system crash, power outage, ...
	+ kill all current TX
	+ does not lose persistent data
	+ R2-Recovery: partial redo of committed TX
	+ R3-Recovery: global undo of uncommitted TX
+ media failue
	+ hard disk errors (non-restorable)
	+ lose persistent data ==> need back up 
	+ R4-Recovery: global redo of all committed TX

### Database Transaction Log
+ ![](Pasted%20image%2020220519155234.png)

### Logging Types
+ ![](Pasted%20image%2020220520151204.png)

### Recovery on Storage Class Memory
+ ![](Pasted%20image%2020220520151515.png)
