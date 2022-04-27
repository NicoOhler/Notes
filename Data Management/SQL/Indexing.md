# Indexing
+ creating secondary (nonclustered) index possible
	+ clustered ==> tuples sorted by index
	+ nonclustered ==> sorted attribute with tuple references?
+ ![[Pasted image 20220412150900.png]]
+ ![[Pasted image 20220412151005.png]]
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