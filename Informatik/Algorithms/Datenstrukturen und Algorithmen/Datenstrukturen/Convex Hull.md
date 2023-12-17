### Motivation
+ ![[Pasted image 20221227134456.png]]
+ ![[Pasted image 20221227134509.png]]

### Convex Set
+ ![[Pasted image 20221227134917.png]]
+ intersection of convex sets also convex
+ sets can be approximated with convex set
	+ small convex set containing original set
		+ ![[Pasted image 20221227135132.png]]
+ convex hull 
	+ smallest convex set
		+ ![[Pasted image 20221227135150.png]]
	+ ![[Pasted image 20221227135220.png]]
	+ contains boundary and interior

### Motivation
+ important geometric [[Datenstrukturen]]
+ applications
	+ ![[Pasted image 20221227135319.png]]
	+ ![[Pasted image 20221227135351.png]]
	+ ![[Pasted image 20221227135433.png]]
	+ etc

### Planar Convex Hull
+ convex polygon
	+ convex hull of point set
+ convex hull of vertex set
	+ convex hull of polygon
+ basic creation algorithms
	+ ![[Pasted image 20221227135648.png]]
	+ ![[Pasted image 20221227140210.png]]

### Jarvis' Wrap
+ edge of convex hull if all other points on one side
	+ ![[Pasted image 20221227140340.png]]
	+ ![[Pasted image 20221227140500.png]]
	+ Repeat until $q_1$ is reached again
+ ![[Pasted image 20221227140712.png]]
+ ![[Pasted image 20221227140824.png]]
+ pseudo code
	+ preparation
		+ ![[Pasted image 20221227140805.png]]
	+ ![[Pasted image 20221227140857.png]]
+ time complexity
	+ ![[Pasted image 20221227140955.png]]
+ space complexity
	+ ![[Pasted image 20221227141158.png]]
+ correctness
	+ ![[Pasted image 20221227141218.png]]
+ ![[Pasted image 20221227141448.png]]

### Orientation Test
+ ![[Pasted image 20221227141600.png]]

### Graham Scan
+ ![[Pasted image 20221227141857.png]]
+ ![[Pasted image 20221227142002.png]]
	+ ![[Pasted image 20221227142112.png]]
+ ![[Pasted image 20221227142153.png]]
	+ ![[Pasted image 20221227142217.png]]
+ time complexity
	+ ![[Pasted image 20221227142420.png]]
+ space complexity
	+ ![[Pasted image 20221227142437.png]]
+ correctness
	+ ![[Pasted image 20221227142500.png]]

### Lower Bound
+ ![[Pasted image 20221227163924.png]]
+ ![[Pasted image 20221227163941.png]]

