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
+ if two segments intersect → $x$-intervals overlap
	+ inverse not always true
+ scan from left to right through all $x$-value with vertical $L$
	+ at every point 
		+ consider segments hit by $L$
		+ check for intersection
	+ intersections must be neighboured on $L$ 
		+ at some point
+ ![[Pasted image 20230113211847.png]]
+ events
	+ ![[Pasted image 20230113211908.png]]

### Implementation
+ used data structures
	+ X
		+ contains $x$-coordintates of known, future events
			+ incoming start and endpoints
		+ operations
			+ insert
			+ remove $x$-minimum
				+ [[Queue]], [[Heap]]
	+ search tree Y
		+ contains $y$-ordered set of semgents intersecting $L$
		+ operations
			+ insert (startpoints)
			+ remove (endpoints)
			+ switch neighbours (intersection)
			+ dictionary, [[(2-4)-Bäume]]
+ pseudocode
	+ ![[Pasted image 20230113213608.png]]
+ details
	+ $y$-order depends on actual $y$-coordinates at this $x$-coordinate
		+ ![[Pasted image 20230113214133.png]]
	+ at most two new neighbours
		+ above and below new minimum $x$
		+ easier to find if linked
			+ maybe link leaves of [[(2-4)-Bäume]] with pointers

### Analysis
+ ![[Pasted image 20230113214400.png]]