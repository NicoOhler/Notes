### Plan Generation
+ selection of physical access path and [[Plan Operators]]
+ selection of execution order
+ convert logical query plan into optimal physical query plan
+ cost query optimization must be less than actual improvements

### Cost Models
+ ![](Pasted%20image%2020220512140034.png)
	+ do not consider skew and [[Correlation]]

### Query Types
+ nodes: tables
+ edges: join conditions
+ hardness depends on structure
+ types:
	+ chains
		+ few join orders
		+ ![](Pasted%20image%2020220512145212.png)
	+ stars
		+ central table
		+ outer tables add information
		+ almost no alternative join orders
		+ ![](Pasted%20image%2020220512145225.png)
	+ cliques
		+ lots of different join orders
		+ difficult to calculate
		+ ![](Pasted%20image%2020220512145315.png)

### Join Tree/Plan Types
+ data flow graph of tables and joins
+ edges data dependencies
+ types:
	+ ![](Pasted%20image%2020220512145654.png)

