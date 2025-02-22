### Grundbegriffe
+  Graph $G=(V,E)$
	+ Paar der Menge der Knoten V und Menge der Kanten E
	+ E⊆(V,2)
		+ Menge von 2-elementrigeTeilmengen von V
	+ z.B. ungerichtete Graph
		+ ![](Pasted%20image%2020220508130402.png)
+ gerichtete Graph (Digraph)
	+ ![](Pasted%20image%2020220508130756.png)
+ Knoten A ist Nachbar von B, wenn verbunden durch Kante
+ Knoten ist isoliert, wenn er keine Nachbarn hat
+ Schleife
	+ Knoten mit sich selbst verbunden
+ $G_1$ ist Teilgraph von $G_2$, wenn
	+ $G_1=(V_1,E_1)$ und $G_2=(V_2,E_2)$
	+ $V_1⊆V_2$und $E_1⊆E_2$
+ Teilgraph induziert(aufgespannt), wenn
	+ ![](Pasted%20image%2020220508131411.png)
	+ ![](Pasted%20image%2020220508131641.png)
	+ 
### Grad
+ falls Knoten auf Kante liegt
	+  V und E inzident
+ falls e aus zwei unterschiedlichen Knoten v und w besteht
	+ v und w sind adjazent/benachbart
+ Graph ist vollständig, wenn je zwei Knoten benachbart
	+ jeder Knoten ist mit jedem verbunden?
	+ ![](Pasted%20image%2020220508144551.png)
+ Teilmenge von V und E sind unabhängig
	+ wenn Elemente paarweise nicht benachbart sind
	+ ![](Pasted%20image%2020220508145351.png)
	+ ![](Pasted%20image%2020220508145357.png)
+ Grad von Knoten = Anzahl von Nachbarn
	+ $deg(V)=|N_G(V)|$
+ Gradarten
	+ ![](Pasted%20image%2020220508145821.png)
+ Summe aller Grade in Graph = doppelte Kantenanzahl
	+ ![](Pasted%20image%2020220508150003.png)
+ gerichteter Graph ==> Unterscheidung in Ausgangs- und Eingangsgrad
	+ ![](Pasted%20image%2020220508150304.png)
	+ Knoten mit Ausgangsgrad 0 heißt Senke
	+ Knoten mit Eingangsgrad 0 heißt Quelle
	+ ![](Pasted%20image%2020220508153515.png)

[[Diskrete Mathematik]] [[Graphs KR]]