### Definition
+ given $n$ line segments in the plane, find all intersections

### Intersection Check
+ other segment's endpoints must be on different sides
+ for both segments
+ check 4 triple-orientations 
	+ ![](Pasted%20image%2020230113210908.png)
	+ $counterclockwise=left$

### Observations
+ intersection check takes constant time
+ up to $\Theta(n^2)$ intersections
	+ worst case takes $\Omega(n^2)$
	+ output-sensitive algorithm needed

### Plane Sweep Idea
+ if two segments intersect → $x$-intervals overlap
	+ inverse not always true
+ scan from left to right through all $x$-values with vertical $L$
	+ at every point 
		+ consider segments hit by $L$
		+ check for intersection
	+ intersections must be neighboured on $L$ 
		+ at some point
+ ![](Pasted%20image%2020230113211847.png)
+ events
	+ ![](Pasted%20image%2020230113211908.png)

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
		+ contains $y$-ordered set of segments intersecting $L$
		+ operations
			+ insert (startpoints)
			+ remove (endpoints)
			+ switch neighbours (intersection)
			+ dictionary, [[(2-4)-Bäume]]
+ pseudocode
	+ ![](Pasted%20image%2020230113213608.png)
+ $y$-order depends on actual $y$-coordinates at this $x$-coordinate
	+ ![](Pasted%20image%2020230113214133.png)
+ at most two new neighbours
	+ above and below new minimum $x$
	+ easier to find if linked
		+ maybe link leaves of [[(2-4)-Bäume]] with pointers

### Analysis
+ ![](Pasted%20image%2020230113214527.png)
+ detecting same intersection twice possible
	+ must be prevented with check
	 + does not affect time complexity
+ ![](Pasted%20image%2020230113214944.png)
+ can be further reduced to
	+ $O(n\ log n + k)$
+ stop at first intersection possible
	+ ![](Pasted%20image%2020230113215052.png)
