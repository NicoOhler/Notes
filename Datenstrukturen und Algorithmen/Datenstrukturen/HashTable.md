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

### Kollisionen
+ Problem
	+ endlich große Tabelle
	+ Menge der möglichen Schlüssel größer
	+ Kollision
		+ unterschiedliche Schlüssel haben denselben Index

### Hashfunktion
+ Ziel: Werte gleich auf Feld zu verteilen
	+ Verteilung der Werte meist unbekannt
+ heuristische Wahl der Funktion
	+ möglichst effizient
	+ gleichwahrscheinliche Indizes
	+ ähnliche Werte getrennt
		+ unabhängig von Mustern in den Daten
+ theoretische ideale Hashfunktion
	+ jeder Index ist gleich wahrscheinlich
	+ ![[Pasted image 20221113105721.png]]

### Arten von Hashfunktionen
+ Divisionsmethode
	+ ![[Pasted image 20221113105906.png]]
	+ schnell berechenbar
	+ nicht für alle m geeignet
		+ e.g. $m=2^k$ →hängt nur von letzten $k-1$ Stellen ab
	+ 
+ 
