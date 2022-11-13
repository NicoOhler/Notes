### Motivation
+ Wörterbuchproblem lösen
+ Operationen
	+ insert
	+ search
	+ remove
+ Idee
	+ nicht Inhalt suchen
	+ Adresse berechnen in $O(1)$

### Definition
+ lineares Feld $T[0...m-1]$
+ Wert $w∈U$ wird in $T[h(w)]$ gespeichert
+ Hashfunktion $h:$ $U→\{0,1,...,m-1\}$
+ ![[Pasted image 20221113105055.png]]

### Hashfunktion



### Kollisionen
+ Problem
	+ endlich große Tabelle
	+ Menge der möglichen Schlüssel größer
	+ Kollision
		+ unterschiedliche Schlüssel haben denselben Index