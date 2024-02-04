+ ### Terminology
+ lock
	+ logical synchronization of TXs
	+ blocks access to db objects
+ latch
	+ physical synchronization of access
	+ blocks access to shared data structures
+ pessimistic concurrency control
	+ assumes error will happen
	+ thus locks schemes
	+ lock-based database scheduler
	+ full serialization of TXs
+ optimistic concurrency control
	+ assumes error will not happen
	+ no locks but validation phase afterwards
		+ check of conflicts
	+ timestamp-based database schedulers
+ mixed concurrency control
	+ combines PCC and OCC
	+ might return synchronization errors (deadlocks)

### Serializability Therory
+ ![](../../../../z_images/Pasted%20image%2020220519150007.png)
+ ![](../../../../z_images/Pasted%20image%2020220519150029.png)
+ ![](../../../../z_images/Pasted%20image%2020220519150257.png)

### Locking Schemes
+ exclusive/write x-lock
	+ only current lock may write
+ shared/read s-lock
	+ current lock and other locks may read
+ multi-granularity-locking
	+ abuses hierarchy of db ojects
	+ intentional x/s-lock
	+ ![](../../../../z_images/Pasted%20image%2020220519150801.png)
+ lock compatibility
	+ ![](../../../../z_images/Pasted%20image%2020220519150717.png)

### Two-Phase Locking
+ concurrency protocol that guarantees serializable
+ pessimistic concurrency control
+ expanding phase
	+ aquires locks needed by TX
+ shrinking phase
	+ release locks aquired by TX
+ ![](../../../../z_images/Pasted%20image%2020220519151028.png)
+ potential problems fixed
	+ ![](../../../../z_images/Pasted%20image%2020220519151117.png)
	+ deadlock
		+ ![](../../../../z_images/Pasted%20image%2020220519151148.png)
		+ ![](../../../../z_images/Pasted%20image%2020220519151217.png)
		+ ![](../../../../z_images/Pasted%20image%2020220519151344.png)

### Timestamp Ordering
+ optimistic concurrency control
+ low overhead scheme if conflicts are rare
+ TXs get timestamp at BOT
+ each data object has read and write timestamp
+ timestamp comparison to validate access/abort
+ no locks but latches
+ ![](../../../../z_images/Pasted%20image%2020220519152033.png)

### Optimistic Concurrency Control
+ ![](../../../../z_images/Pasted%20image%2020220519152243.png)