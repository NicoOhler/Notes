### Triangel
+ simplest piece of surface
+ allow modelling surfaces
+ important for Computer Graphics

### Triangulation of Point Set $S$
+ [[Convex Hull]] partitioned into interior-disjoint triangels
+ no point of $S$ inside a segment or triangle
	+ ![](../../../../z_images/Pasted%20image%2020221227213814.png)
	+ ![](../../../../z_images/Pasted%20image%2020221227213759.png)
	+ ![](../../../../z_images/Pasted%20image%2020221227213823.png)

### Triangulation of Polygon $P$
+ polygon $P$ with vertex set S partitioned into interior-disjoint triangles
+ no point of $S$ inside a segment (or triangle)
	+ ![](../../../../z_images/Pasted%20image%2020221227214116.png)
	+ ![](../../../../z_images/Pasted%20image%2020221227214158.png)
	+ ![](../../../../z_images/Pasted%20image%2020221227214205.png)

### Maximal Plane Straight-Line Graphs
+ ![](../../../../z_images/Pasted%20image%2020221227214404.png)
+ ![](../../../../z_images/Pasted%20image%2020221227214308.png)
+ ![](../../../../z_images/Pasted%20image%2020221227214331.png)

### Elements of Triangulation
+ ![](../../../../z_images/Pasted%20image%2020221227214541.png)
+ number of edges and triangels depend on number of extreme points $h$ of $S$
	+ ![](../../../../z_images/Pasted%20image%2020221227214632.png)
	+ ![](../../../../z_images/Pasted%20image%2020221227214746.png)

### Applications
+ Graphics/GIS
	+ ![](../../../../z_images/Pasted%20image%2020221227214956.png)
+ FEM
	+ ![](../../../../z_images/Pasted%20image%2020221227215056.png)
+ geometric algorithms
	+ ![](../../../../z_images/Pasted%20image%2020221227215152.png)
+ [[Kombinatorik]]
	+ neighbours have different colors
	+ ![](../../../../z_images/Pasted%20image%2020221227215302.png)

### Canonical Triangulation
+ combine 3 leftmost points
+ add each point sequentially
	+ combine this point with each point to the left which it still "sees"
+ ![](../../../../z_images/Pasted%20image%2020221227215943.png)
+ ![](../../../../z_images/Pasted%20image%2020221227220001.png)

### Triangulation with Graham Scan
+ similar to creating [[Convex Hull]]
+ ![](../../../../z_images/Pasted%20image%2020221227220301.png)
+  ![](../../../../z_images/Pasted%20image%2020221227220315.png)
+ ![](../../../../z_images/Pasted%20image%2020221227220418.png)
	+ ![](../../../../z_images/Pasted%20image%2020221227220431.png)
+ ![](../../../../z_images/Pasted%20image%2020221227220444.png)
	+ ![](../../../../z_images/Pasted%20image%2020221227220538.png)
+ time complexity
	+ ![](../../../../z_images/Pasted%20image%2020221227220651.png)
+ space complexity
	+ ![](../../../../z_images/Pasted%20image%2020221227220752.png)
+ correctness
	+ ![](../../../../z_images/Pasted%20image%2020221227220909.png)

### Local Transformation
+ rebuild existing triangulation to different triangulation
+ edge flips
	+ ![](../../../../z_images/Pasted%20image%2020221227221109.png)
	+ ![](../../../../z_images/Pasted%20image%2020221227221115.png)
+ useful for optimization in heuristics

### Flip Distance Problem
+ ![](../../../../z_images/Pasted%20image%2020221227221226.png)

### Delaunay Triangulation
+ ![](../../../../z_images/Pasted%20image%2020221227221439.png)
+ ![](../../../../z_images/Pasted%20image%2020221227221448.png)