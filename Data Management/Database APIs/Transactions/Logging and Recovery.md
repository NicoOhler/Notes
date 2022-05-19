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
	+ R4-Recovery: global