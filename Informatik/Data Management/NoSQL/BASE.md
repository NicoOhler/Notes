### BASE Properties
+ instead of ACID in [[NoSQL]] systems
+ basically available
	+ focus on availability
	+ potentially outdated dta
	+ no guarantee on consistent data
+ soft state
	+ data might change later on
	+ due to async updates/nodes becoming available again
+ eventual consistency
	+ after enough time data distributed on all nodes become consistent
	+ ![](../../../z_images/Pasted%20image%2020220608174250.png)

### Two-Phase Commit Protocol
+ distributed TX processing
	+ n nodes with related but distributed data (vertical partitiong)
	+ ensures consistent view
		+ atomicity
		+ durability
+ two-phase commit (via 2n msgs)
	+ prepare - check for success, log 
	+ commit - release locks and other cleanups
	+ each node was successful ==> release locks
		+ otherwise each node revert/prevent local changes
	+ scaling problem
		+ one node temporarily down ==> failure

### Cap Theorem
+ at most 2 of the following attributes
	+ consistency - changes consistent among all nodes
	+ availablity - services must be always availabe
	+ partition tolerance - tolerance of temporarily unreachable noces
+ possible combinations
	+ ![](../../../z_images/Pasted%20image%2020220608173739.png)

