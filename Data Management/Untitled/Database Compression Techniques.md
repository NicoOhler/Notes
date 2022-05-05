# DB Compression Techniques
### DB Compression Overview
+ fit larger datasets in memory
+ less I/O
+ better cache uitilization
+ some DBs allow query processing directly on compressed data
	+ ![[Pasted image 20220505105419.png]]

### Lightweight Database Compression Schemes
+ null suppresion
	+ compress integers with leading zeros
	+ ![[Pasted image 20220505105637.png]]
+ run-length encoding
	+ compress sequences of equal values by "runs"
	+ each run consists of
		+ value
		+ start
		+ length
	+ ![[Pasted image 20220505105752.png]]
+ dictionary encoding
	+ compress column with few distinct values 
	+ create dictionary with all values
	+ store pos in dictionary instead of actual value
	+ ![[Pasted image 20220505110042.png]]
		+ compression would be more effective if values were strings instead
+ delta encoding
	+ compress sequence with small changes
	+ store delta/change to previous value
	+ ![[Pasted image 20220505110250.png]]
+ frame of reve



[[Physical Design]]
