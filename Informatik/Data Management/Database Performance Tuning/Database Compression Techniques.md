### DB Compression Overview
+ fit larger datasets in memory
+ less I/O
+ better cache uitilization
+ some DBs allow query processing directly on compressed data
	+ ![](../../z_images/Pasted%20image%2020220505105419.png)

### Lightweight Database Compression Schemes
+ null suppresion
	+ compress integers with leading zeros
	+ ![](../../z_images/Pasted%20image%2020220505105637.png)
+ run-length encoding
	+ compress sequences of equal values by "runs"
	+ each run consists of
		+ value
		+ start
		+ length
	+ ![](../../z_images/Pasted%20image%2020220505105752.png)
+ dictionary encoding
	+ compress column with few distinct values 
	+ create dictionary with all values
	+ store pos in dictionary instead of actual value
	+ ![](../../z_images/Pasted%20image%2020220505110042.png)
		+ compression would be more effective if values were strings instead
+ delta encoding
	+ compress sequence with small changes
	+ store delta/change to previous value
	+ ![](../../z_images/Pasted%20image%2020220505110250.png)
+ frame-of-reference encoding
	+ compress values by storing delta to reference value
	+ outlier handling
	+ ![](../../z_images/Pasted%20image%2020220505110426.png)



[[Physical Design]]
