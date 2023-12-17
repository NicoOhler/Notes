# Logging and Recovery
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
+ ![[Pasted image 20220519155234.png]]

### Logging Types
+ ![[Pasted image 20220520151204.png]]

### Recovery on Storage Class Memory
+ ![[Pasted image 20220520151515.png]]
