+ use case
	+ query result instead of [[SQL]] table
	+ aggregation value instead of scalar value
+ subqueries can be stored as variable
	+ WITH VariableName AS (SELECT ...)
	+ ![](../../z_images/Pasted%20image%2020220412152501.png)
+ common use cases:
	+ ![](../../z_images/Pasted%20image%2020220412152541.png)

### Correlated and Uncorrelated Subqueries
+ correlated if queries depend on each other
	+ subquery exectuted for each tuple of outer query
		+ nested for loop 
	+ inefficient
	+ ![](../../z_images/Pasted%20image%2020220412152728.png)
+ uncorrelated if subquery executed once
	+ ![](../../z_images/Pasted%20image%2020220412152926.png)
+ correlated queries may be unnested (de-correlation)
	+ can also be improved by "only" executing subquery for each distinct value

### Recursive Queries
+ terminates when recursive query returns empty table
+ ![](../../z_images/Pasted%20image%2020220412153237.png)
+ ![](../../z_images/Pasted%20image%2020220412153249.png)
+ ![](../../z_images/Pasted%20image%2020220412153255.png)

[[Correlation]]
