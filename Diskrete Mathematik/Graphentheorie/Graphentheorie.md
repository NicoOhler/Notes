# Graphentheorie
### Grundbegriffe
+  Graph $G=(V,E)$
	+ Paar der Menge der Knoten V und Menge der Kanten E
	+ E⊆(V,2)
		+ Menge von 2-elementrigeTeilmengen von V
	+ z.B. ungerichtete Graph
		+ ![[Pasted image 20220508130402.png]]
+ gerichtete Graph (Digraph)
	+ ![[Pasted image 20220508130756.png]]
+ Knoten A ist Nachbar von B, wenn verbunden durch Kante
+ Knoten ist isoliert, wenn er keine Nachbarn hat
+ Schleife
	+ Knoten mit sich selbst verbunden
+ $G_1$ ist Teilgraph von $G_2$, wenn
	+ $G_1=(V_1,E_1)$ und $G_2=(V_2,E_2)$
	+ $V_1⊆V_2$und $E_1⊆E_2$
+ Teilgraph induziert(aufgespannt), wenn
	+ ![[Pasted image 20220508131411.png]]
	+ ![[Pasted image 20220508131641.png]]
	+ 
### Grad
+ falls Knoten auf Kante liegt
	+  V und E inzident
+ falls e aus zwei unterschiedlichen Knoten v und w besteht
	+ v und w sind adjazent/benachbart
+ Graph ist vollständig, wenn je zwei Knoten benachbart
	+ jeder Knoten ist mit jedem verbunden?
	+ ![[Pasted image 20220508144551.png]]
+ Teilmenge von V und E sind unabhängig
	+ wenn Elemente paarweise nicht benachbart sind
	+ ![[Pasted image 20220508145351.png]]
	+ ![[Pasted image 20220508145357.png]]
+ Grad von Knoten = Anzahl von Nachbarn
	+ $deg(V)=|N_G(V)|$
+ Gradarten
	+ ![[Pasted image 20220508145821.png]]
+ Summe aller Grade in Graph = doppelte Kantenanzahl
	+ ![[Pasted image 20220508150003.png]]
+ gerichteter Graph ==> Unterscheidung in Ausgangs- und Eingangsgrad
	+ ![[Pasted image 20220508150304.png]]
	+ Knoten mit Ausgangsgrad 0 heißt Senke
	+ Knoten mit Eingangsgrad 0 heißt Quelle

### Adjazenzmatrix
+ Adjazenzmatrix ist nxn Matrix mit
	+ $a_{ij}=1$, wenn $V_i$ und $V_j$ benachbart
	+ ansonsten 0
+ immer symmetrisch entlang der Diagonale
+ Beispiel
	+ ![[Pasted image 20220508150829.png]]
	+ Sanity Check - Probe
		+ ![[Pasted image 20220508151129.png]]

### Inzidenzmatrix
+ analog zur Adjazenzmatrix
	+ 1 wenn inzident
+ Beispiel:
	+ ![[Pasted image 20220508151314.png]]
	+ ![[Pasted image 20220508151256.png]]

### Diagonalmatrix/Gradmatrix
+ auf der Diagonale befindet sich Grad des jeweiligen Knoten
+ ![[Pasted image 20220508151638.png]]

### a
+ auf der Diagonale befindet sich Grad des jeweiligen Knoten
+ ansonsten -1 falls verbunden, sonst 0
+ ![[Pasted image 20220508151831.png]]
+ kann a

[[Diskrete Mathematik]] [[Graphs]] [[Matrix]]