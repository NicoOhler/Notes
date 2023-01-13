### Definition
+ given $n$ line segments in the plane, find all intersections

### Intersection Check
+ other segment's endpoints must be on different sides
+ for both segments
+ check 4 triple-orientations 
	+ ![[Pasted image 20230113210908.png]]
	+ $counterclockwise=left$

### Observations
+ intersection check takes constant time
+ up to $\Theta(n^2)$ intersections
	+ worst case takes $\Omega(n^2)$
	+ output-sensitive algorithm needed

### Plane Sweep Idea
+ if two seg

