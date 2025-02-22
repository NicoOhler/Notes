### Segments, Pages and Blocks
+ segments
	+ storage unit of DB objects
	+ such as relations (heap) and indexes
+ page
	+ fixed-size memory region
	+ postgres 8KB by default
+ block
	+ smallest addressable unit on disk
+ ![](Pasted%20image%2020220505104430.png)

### Buffer & Storage Management
+ buffer management at granularity of pages
+ different table/page layouts possible
	+ NSM
	+ DSM
	+ PAX
	+ column
+ TID/RID concept
	+ tuple/row identifier
	+ stable ID, even if records reorganized in memory
	+ allows reorganizing data without altering address references
	+ ![](Pasted%20image%2020220505104735.png)
	+ page slot directory holds tuple offsets (byte position) within page
	+ ![](Pasted%20image%2020220505105122.png)

[[Database Compression Techniques]]