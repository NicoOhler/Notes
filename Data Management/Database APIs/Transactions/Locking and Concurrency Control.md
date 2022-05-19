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