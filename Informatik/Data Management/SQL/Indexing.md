+ creating secondary (nonclustered) index possible
	+ clustered ==> tuples sorted by index
	+ nonclustered ==> sorted attribute with tuple references?
+ ![](../../../z_images/Pasted%20image%2020220412150900.png)
+ ![](../../../z_images/Pasted%20image%2020220412151005.png)
+ can specify uniqueness, order and indexing method
	+ btree
	+ hash
	+ gist
	+ ...
+ increase read performance
+ slow down write performance 
+ primary keys (unique attributes) usually always create indexes
	+ verifying uniqueness would be inefficient otherwise


[[SQL]]