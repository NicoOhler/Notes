### Overview
+ written as A* Algorithm
+ [[Shortest Path Algorithms]] to find a single destination
+ based on [[Breadth-First Search]] and [[Dijkstra’s Algorithm]]
+ informed
	+ does not search uniformly
	+ uses heuristics
	+ prioritizes towards the direction of the goal

### Heuristics
+ ![[Pasted image 20231003144622.png]]
+ perfect heuristic
	+ border line impossible
	+ requires perfect knowledge lol
+ overestimate
	+ fast
	+ not admissible
	+ might not find path even if one exists

### A* Heuristics
+ $g(v)$
	+ distance from start to current vertex
+ $h(u)$
	+ distance from current vertex to end
		+ "Luftlinie" - as the crow flies
	+ ignores obstacles which may block the path
	+ underestimates the future cost
		+ good characteristic
+ therefore pretty efficient

### Comparison between A* and Dijkstra’s
+ A*
	+ ![[Pasted image 20231003140500.png]]
+ Dijkstra’s
	+ ![[Pasted image 20231003140512.png]]

### Algorithm
+ ![[Pasted image 20231003140811.png]]
+ ![[Pasted image 20231003141556.png]]
	+ red parts differ from [[Dijkstra’s Algorithm]]

### Properties
+ nodes may expand more than once
	+ $g(v)$ heuristic value can change
	+ always terminates if a path exists
+ optimal if a path exists
	+ ![[Pasted image 20231003143638.png]]
	+ ![[Pasted image 20231003143841.png]]
	+ ![[Pasted image 20231003144431.png]]
+ optimally efficient
	+ with regards to the number of vertices expanded
+ space as bottle neck
	+ ![[Pasted image 20231003145200.png]]
	+ ![[Pasted image 20231003145208.png]]
	+ motivation for memory bounded heuristic search
		+ Iterative deepening A*
