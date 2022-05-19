# Locking and Concurrency Control
+ ### Terminology
+ lock
	+ logical synchronization of TXs
	+ blocks access to db objects
+ latch
	+ physical synchronization of access
	+ blocks access to shared data structures
+ Pessimistic Concurrency Control
	+ assumes error will happen
	+ thus locks schemes
	+ lock-based database scheduler
	+ full serialization of TXs
+ Optimistic Concurrency Control
	+ assumes error will not happen
	+ no locks but validation phase afterwards
		+ check of conflicts
	+ timestamp-based database schedulers
+ Mixed Concurrency Control
	+ combines PCC and OCC
	+ might return synchronization errors (deadlocks)

### Serializability Therory
+ ![[Pasted image 20220519150007.png]]
+ ![[Pasted image 20220519150029.png]]
+ ![[Pasted image 20220519150257.png]]

### Locking Schemes
+ exclusive/write x-lock
	+ only current lock may write
+ shared/read s-lock
	+ current lock and other locks may read
+ multi-granularity-locking
	+ abuses hierarchy of db ojects
	+ intentional x/s-lock
	+ ![[Pasted image 20220519150801.png]]
+ lock compatibility
	+ ![[Pasted image 20220519150717.png]]

### Two-Phase Locking
+ concurrency protocol that guarantees serializable
+ expanding phase
	+ aquires locks needed by TX
+ shrinking phase
	+ release locks aquired by TX
+ ![[Pasted image 20220519151028.png]]
+ 
