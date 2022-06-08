# ACID in NoSQL
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
+ cap theorem ==> at most 2 of the following attributes
	+ consistency - changes consistent among all nodes
	+ availablity - services must be always availabe
	+ partition tolerance - tolerance of temporarily unreachable noces
+ proof
+ 
