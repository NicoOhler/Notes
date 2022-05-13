# Spannbaumalgorithmen
### Prüfer-Code
+ Bijektion f: $T_n$-->$S_{n-2}, T$-->$f(T)=s$
	+ $S_{n-2}=\{s=(s_1s2....s_{n-2}),s_i∈[n]\}$
	+ sukzessiv definiert
		+ $T_0=T$
		+ $T_i$
			+ nehme kleinste Blatt $l_i$ in $T_i-1$
			+ entferne $l_i$  und inzidente Kante von $T_i-1$
			+ definiere i-te Folgenglied $s_i$ als Nachbar von $l_i$
+ Verfahren retourniert Folge $S_T$
+ ![[Pasted image 20220513135223.png]]

###  Bread-First-Search
+ branching progress
+ ![[Pasted image 20220513135916.png]]
+ Input: zusammenhängender Graph G
+ Output: Spannbaum T
+ Verfahren:
	+ wähle Knoten $x_0$ als Wurzel
		+ Liste $L=(x_0)$
	+ Loop bis T alle Knoten enthält $V(T)=V(G)$
		+ gegeben Liste $L=(x_0,x_1,...)$ und Baum T
		+ nimm ersten Knoten x von L
		+ falls x keine Nachbarn hat, welche noch nicht im Baum sind
			+ $N(x)/V(T)=∅$
			+ entfern x aus L
		+ sonst
			+ füg einen Nachbarn y aus $N(x)/V(T)$ zu T und L hinzu
			+ ![[Pasted image 20220513143532.png]]
	+ return T
+ Beispiel
	+ ![[Pasted image 20220513144115.png]]
	+ ![[Pasted image 20220513144220.png]]

### Depth-First-Search
+ findet langen Pfad
+ ![[Pasted image 20220513135946.png]]
+ Input: zusammenhängender Graph G
+ Output: Spannbaum T
+ Verfahren fast ident zu BFS
	+ jedoch wird y am Anfang von L hinzugefügt
		+ ![[Pasted image 20220513143908.png]]

### Algorithmus von Kruskal
+ Input: 
	+ zus. Graph G mit n Knoten und m Kanten
	+ Gewichtsfunktion w
		+ E-->ℝ
		+ e-->w(e)
+ Output:
	+ Spannbaum T von G mit minimalem Gewicht
	+ Summe aller Kantengewichte ist minimal
	+ ![[Pasted image 20220513145234.png]]
+ Verfahren
	+ sortiere (nummeriere) Kanten aufsteigend nach Gewicht
		+ ![[Pasted image 20220513145554.png]]
	+ setze E(T)=∅
	+ Loop bis $|E(T)|=n-1$
		+ nimm die kleinste Kante $e_n$
		+ füge $e_n$ zu T hinzu, wenn das keinen Kreis erzeugt
			+ sonst wird $e_n$ aus der Liste entfernt
	+ return T

### Matching
+ Matching in G ist Menge M⊆E, sodass jeder Knoten höchstens eine Kante von M berührt
+ ![[Pasted image 20220513211821.png]]
+ ![[Pasted image 20220513211946.png]]
+ Matching ist perfekt, wenn jeder Knoten gematcht ist
	+ $|M|=\frac{|V|}{2}$
	+ größtmögliches Matching

### Satz von Hall
+ bipartite Graph G
	+ ![[Pasted image 20220513212219.png]]
+ G hat Matching, wenn $N(S)≥|S|$ für $∀S⊆A$
	+ ![[Pasted image 20220513212531.png]]
+ Pfad $P=(x_0,e_1,x_1,e_2,x_2,...,e_n,x_n)$ alternierend bzgl. M, wenn
	+ $x_0$ ungematcht:
		+ $e_i∈M$ für gerade i
		+ $e_i∉M$ für ungerade i
+ P ist augmentierend, wenn alternierend und 

[[Bäume & Spannbäume]]