### Motivation
+ ![](Pasted%20image%2020221227134456.png)
+ ![](Pasted%20image%2020221227134509.png)

### Convex Set
+ ![](Pasted%20image%2020221227134917.png)
+ intersection of convex sets also convex
+ sets can be approximated with convex set
	+ small convex set containing original set
		+ ![](Pasted%20image%2020221227135132.png)
+ convex hull 
	+ smallest convex set
		+ ![](Pasted%20image%2020221227135150.png)
	+ ![](Pasted%20image%2020221227135220.png)
	+ contains boundary and interior

### Motivation
+ important geometric [[Datenstrukturen]]
+ applications
	+ ![](Pasted%20image%2020221227135319.png)
	+ ![](Pasted%20image%2020221227135351.png)
	+ ![](Pasted%20image%2020221227135433.png)
	+ etc

### Planar Convex Hull
+ convex polygon
	+ convex hull of point set
+ convex hull of vertex set
	+ convex hull of polygon
+ basic creation algorithms
	+ ![](Pasted%20image%2020221227135648.png)
	+ ![](Pasted%20image%2020221227140210.png)

### Jarvis' Wrap
+ edge of convex hull if all other points on one side
	+ ![](Pasted%20image%2020221227140340.png)
	+ ![](Pasted%20image%2020221227140500.png)
	+ Repeat until $q_1$ is reached again
+ ![](Pasted%20image%2020221227140712.png)
+ ![](Pasted%20image%2020221227140824.png)
+ pseudo code
	+ preparation
		+ ![](Pasted%20image%2020221227140805.png)
	+ ![](Pasted%20image%2020221227140857.png)
+ time complexity
	+ ![](Pasted%20image%2020221227140955.png)
+ space complexity
	+ ![](Pasted%20image%2020221227141158.png)
+ correctness
	+ ![](Pasted%20image%2020221227141218.png)
+ ![](Pasted%20image%2020221227141448.png)

### Orientation Test
+ ![](Pasted%20image%2020221227141600.png)

### Graham Scan
+ ![](Pasted%20image%2020221227141857.png)
+ ![](Pasted%20image%2020221227142002.png)
	+ ![](Pasted%20image%2020221227142112.png)
+ ![](Pasted%20image%2020221227142153.png)
	+ ![](Pasted%20image%2020221227142217.png)
+ time complexity
	+ ![](Pasted%20image%2020221227142420.png)
+ space complexity
	+ ![](Pasted%20image%2020221227142437.png)
+ correctness
	+ ![](Pasted%20image%2020221227142500.png)

### Lower Bound
+ ![](Pasted%20image%2020221227163924.png)
+ ![](Pasted%20image%2020221227163941.png)

