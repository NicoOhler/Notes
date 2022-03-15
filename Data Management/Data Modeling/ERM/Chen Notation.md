# Chen Notation
### Entity
+ objects of the real world
+ entity type/set
	+ collection of entities
+ [[Weak Entity]]
	+ entities that are dependent on existing entity
+ ![[Pasted image 20220315114927.png]]

### Relationship Type
+ defines behaviour between entities
+ connected to concrete entities
+ special types:
	+ [[N-ary Relationships]]
+ ![[Pasted image 20220315114933.png]]

### Attribute
+ entities or relationshiips may have attribute value pairs
+ attributes describe entity/object
+ [[Attribute Types]]
	+ multi-value
	+ derived
	+ composite
	+ nullable
+ ![[Pasted image 20220315115146.png]]

### Keys
+ unique attribute to identify entity
	+ e.g. IDs
+ every entity needs key
+ ![[Pasted image 20220315115519.png]]

### Role
+ optional description of relationship
+ ![[Pasted image 20220315115531.png]]

### Cardinality
+ one-to-one 1:1
	+ ![[Pasted image 20220315120203.png]]
+ one-to-many 1:N
	+ ![[Pasted image 20220315120212.png]]
+ many-to-one N:1
	+ ![[Pasted image 20220315120222.png]]
+ many-to-many N:M
	+ ![[Pasted image 20220315120234.png]]

### Employee DB Example
+ without cardinalites
	+ ![[Pasted image 20220315115722.png]]
+ with cardinalities
	+ ![[Pasted image 20220315120548.png]]
+ with additional information
	+ ![[Pasted image 20220315120654.png]]


[[ER Diagram]]