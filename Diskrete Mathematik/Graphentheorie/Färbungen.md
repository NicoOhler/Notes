# Färbungen
### (Proper) Coloring
+ Färbung von $G(V,E)$ ist Funktion
	+ c: V --> F 
	+ mit Eigenschaft
		+ $\{x,y\}∈E$ ==> $c(x)≠c(y)$
		+ F ist diskrete Menge⊆ℕ
+ Chromatische Zahl $X(G)$ von $G$
	+ kleinste Zahl $k∈ℕ$, sodass ∃ Färbung mit k Farben
	+ $a(G)$ größte Zahl $k∈ℕ$, sodass ∃ unabhängige Knotenmenge in G
	+ ![[Pasted image 20220524140022.png]]
	+ Kreis mit 
		+ gerader Länge braucht 3
		+ ungerader Länge braucht 2
	+ ![[Pasted image 20220524140317.png]]

### Greedy-Algorithmus für Färbung
+ Input: $G=(A∪B,E)$ Graph
+ Output: Färbung mit "nicht zu vielen" Farben
+ Verfahren:
	+ ordne Knoten als $V_1,V_2,...,V_n$
	+ setze $C(V_1)=1$
	+ für $2≤i≤n$
		+ wähle als Farbe $C(V_i)$ die kleinste Zahl, welche nicht als (bisher gewählte) Nachbarfarbe von $V_i$ vorkommt
	+ setze m=1