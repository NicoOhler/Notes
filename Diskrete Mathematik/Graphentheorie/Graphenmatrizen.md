# Graphenmatrizen
### Adjazenzmatrix
+ Adjazenzmatrix ist nxn Matrix mit
	+ $a_{ij}=1$, wenn $V_i$ und $V_j$ benachbart
	+ ansonsten 0
+ immer symmetrisch entlang der Diagonale
+ $(A^k)_{ij}=$# Wege mit Länge k von $v_i$ nach $v_j$
	+ ![[Pasted image 20220512162757.png]]
+ Beispiel:
	+ ![[Pasted image 20220508150829.png]]
	+ Sanity Check - Probe
		+ ![[Pasted image 20220508151129.png]]

### Inzidenzmatrix
+ analog zur Adjazenzmatrix
	+ 1 wenn inzident
	+ ansonsten
+ Beispiel:
	+ ![[Pasted image 20220508151314.png]]
	+ ![[Pasted image 20220508151256.png]]

### Diagonalmatrix/Gradmatrix
+ auf der Diagonale befindet sich Grad des jeweiligen Knoten
+ ![[Pasted image 20220508151638.png]]

### Laplace Matrix
+ auf der Diagonale befindet sich Grad des jeweiligen Knoten
+ ansonsten -1 falls verbunden, sonst 0
+ ![[Pasted image 20220508151831.png]]
+ auch über Adjazenz- und Diagonalmatrix bestimmbar
	+ $L=D-A$
	+ ![[Pasted image 20220508152102.png]]

[[Graphentheorie]] [[Matrix]]