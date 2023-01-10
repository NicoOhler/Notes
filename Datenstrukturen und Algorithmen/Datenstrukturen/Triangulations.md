### Triangel
+ simplest piece of surface
+ allow modelling surfaces
+ important for [[Computer Graphics]]

### Triangulation of Point Set $S$
+ [[Convex Hull]] partitioned into interior-disjoint triangels
+ no point of $S$ inside a segment or triangle
	+ ![[Pasted image 20221227213814.png]]
	+ ![[Pasted image 20221227213759.png]]
	+ ![[Pasted image 20221227213823.png]]

### Triangulation of Polygon $P$
+ polygon $P$ with vertex set S partitioned into interior-disjoint triangles
+ no point of $S$ inside a segment (or triangle)
	+ ![[Pasted image 20221227214116.png]]
	+ ![[Pasted image 20221227214158.png]]
	+ ![[Pasted image 20221227214205.png]]

### Maximal Plane Straight-Line Graphs
+ ![[Pasted image 20221227214404.png]]
+ ![[Pasted image 20221227214308.png]]
+ ![[Pasted image 20221227214331.png]]

### Elements of Triangulation
+ ![[Pasted image 20221227214541.png]]
+ number of edges and triangels depend on number of extreme points $h$ of $S$
	+ ![[Pasted image 20221227214632.png]]
	+ ![[Pasted image 20221227214746.png]]

### Applications
+ Graphics/GIS
	+ ![[Pasted image 20221227214956.png]]
+ FEM
	+ ![[Pasted image 20221227215056.png]]
+ geometric algorithms
	+ ![[Pasted image 20221227215152.png]]
+ [[Kombinatorik]]
	+ neighbours have different colors
	+ ![[Pasted image 20221227215302.png]]

### Canonical Triangulation
+ combine 3 most left points
+ add each point sequentially
	+ combine this point with each point to the left which it still "sees"
+ ![[Pasted image 20221227215943.png]]
+ ![[Pasted image 20221227220001.png]]

### Triangulation with Graham Scan
+ similar to creating [[Convex Hull]]
+ ![[Pasted image 20221227220301.png]]
+  ![[Pasted image 20221227220315.png]]
+ ![[Pasted image 20221227220418.png]]
	+ ![[Pasted image 20221227220431.png]]
+ ![[Pasted image 20221227220444.png]]
	+ ![[Pasted image 20221227220538.png]]
+ time complexity
	+ ![[Pasted image 20221227220651.png]]
+ space complexity
	+ ![[Pasted image 20221227220752.png]]
+ correctness
	+ ![[Pasted image 20221227220909.png]]

### Local Transformation
+ rebuild existing triangulation to different triangulation
+ edge flips
	+ ![[Pasted image 20221227221109.png]]
	+ ![[Pasted image 20221227221115.png]]
+ useful for optimization in heuristics

### Flip Distance Problem
+ ![[Pasted image 20221227221226.png]]

### Delaunay Triangulation
+ ![[Pasted image 20221227221439.png]]
+ ![[Pasted image 20221227221448.png]]