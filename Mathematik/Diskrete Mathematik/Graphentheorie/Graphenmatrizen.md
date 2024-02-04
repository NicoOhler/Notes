### Adjazenzmatrix
+ Adjazenzmatrix ist nxn Matrix mit
	+ $a_{ij}=1$, wenn $V_i$ und $V_j$ benachbart
	+ sonst 0
+ immer symmetrisch entlang der Diagonale
+ $(A^k)_{ij}=$# Wege mit Länge k von $v_i$ nach $v_j$
	+ ![](Pasted%20image%2020220512162757.png)
+ Beispiel:
	+ ![](Pasted%20image%2020220508150829.png)
	+ Sanity Check - Probe
		+ ![](Pasted%20image%2020220508151129.png)

### Inzidenzmatrix
+ analog zur Adjazenzmatrix
	+ 1 wenn inzident
	+ sonst 0
+ Beispiel:
	+ ![](Pasted%20image%2020220508151314.png)
	+ ![](Pasted%20image%2020220508151256.png)

### Diagonalmatrix/Gradmatrix
+ auf der Diagonale befindet sich Grad des jeweiligen Knoten
+ ![](Pasted%20image%2020220508151638.png)

### Laplace Matrix
+ auf der Diagonale befindet sich Grad des jeweiligen Knoten
+ ansonsten -1 falls verbunden, sonst 0
+ ![](Pasted%20image%2020220508151831.png)
+ auch über Adjazenz- und Diagonalmatrix bestimmbar
	+ $L=D-A$
	+ ![](Pasted%20image%2020220508152102.png)

[[Graphentheorie]] [[Matrix]]