### Triangel
+ simplest piece of surface
+ allow modelling surfaces
+ important for Computer Graphics

### Triangulation of Point Set $S$
+ [[Convex Hull]] partitioned into interior-disjoint triangels
+ no point of $S$ inside a segment or triangle
	+ ![](Pasted%20image%2020221227213814.png)
	+ ![](Pasted%20image%2020221227213759.png)
	+ ![](Pasted%20image%2020221227213823.png)

### Triangulation of Polygon $P$
+ polygon $P$ with vertex set S partitioned into interior-disjoint triangles
+ no point of $S$ inside a segment (or triangle)
	+ ![](Pasted%20image%2020221227214116.png)
	+ ![](Pasted%20image%2020221227214158.png)
	+ ![](Pasted%20image%2020221227214205.png)

### Maximal Plane Straight-Line Graphs
+ ![](Pasted%20image%2020221227214404.png)
+ ![](Pasted%20image%2020221227214308.png)
+ ![](Pasted%20image%2020221227214331.png)

### Elements of Triangulation
+ ![](Pasted%20image%2020221227214541.png)
+ number of edges and triangels depend on number of extreme points $h$ of $S$
	+ ![](Pasted%20image%2020221227214632.png)
	+ ![](Pasted%20image%2020221227214746.png)

### Applications
+ Graphics/GIS
	+ ![](Pasted%20image%2020221227214956.png)
+ FEM
	+ ![](Pasted%20image%2020221227215056.png)
+ geometric algorithms
	+ ![](Pasted%20image%2020221227215152.png)
+ [[Kombinatorik]]
	+ neighbours have different colors
	+ ![](Pasted%20image%2020221227215302.png)

### Canonical Triangulation
+ combine 3 leftmost points
+ add each point sequentially
	+ combine this point with each point to the left which it still "sees"
+ ![](Pasted%20image%2020221227215943.png)
+ ![](Pasted%20image%2020221227220001.png)

### Triangulation with Graham Scan
+ similar to creating [[Convex Hull]]
+ ![](Pasted%20image%2020221227220301.png)
+  ![](Pasted%20image%2020221227220315.png)
+ ![](Pasted%20image%2020221227220418.png)
	+ ![](Pasted%20image%2020221227220431.png)
+ ![](Pasted%20image%2020221227220444.png)
	+ ![](Pasted%20image%2020221227220538.png)
+ time complexity
	+ ![](Pasted%20image%2020221227220651.png)
+ space complexity
	+ ![](Pasted%20image%2020221227220752.png)
+ correctness
	+ ![](Pasted%20image%2020221227220909.png)

### Local Transformation
+ rebuild existing triangulation to different triangulation
+ edge flips
	+ ![](Pasted%20image%2020221227221109.png)
	+ ![](Pasted%20image%2020221227221115.png)
+ useful for optimization in heuristics

### Flip Distance Problem
+ ![](Pasted%20image%2020221227221226.png)

### Delaunay Triangulation
+ ![](Pasted%20image%2020221227221439.png)
+ ![](Pasted%20image%2020221227221448.png)