### Problem
+ application use object-oriented approach
+ data stored in normalized flat tables
+ application is responsible for bridging
+ example
	+ ![](../../../z_images/Pasted%20image%2020220427130703.png)

### Object-Relational Mapping
+ ORM tools allow automatic 
	+ handling of object percistence lifecycle
	+ querying of underlying data stores
+ reduced development effort
+ improved testing and independence of DBMS
![](../../../z_images/Pasted%20image%2020220427130949.png)

### Pros and Cons
+ advantages
	+ simple CRUD operations
	+ simple queries
	+ application centric development
+ disadvantages
	+ unnecessary indirections and complexity
		+ mapping
		+ meta data
	+ performance harder to ensure
	+ no application centric development
		+ schema ownership
		+ already existing data
	+ dependent on framework APIs

[[Call Level Interfaces]]