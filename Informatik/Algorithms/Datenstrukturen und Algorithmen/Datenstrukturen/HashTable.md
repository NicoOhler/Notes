### Motivation
+ Wörterbuchproblem lösen
+ Operationen
	+ insert
	+ search
	+ remove
+ Idee
	+ Inhalt nicht suchen
	+ Adresse berechnen in $O(1)$

### Definition
+ lineares Feld $T[0...m-1]$
+ Wert $w∈U$ wird in $T[h(w)]$ gespeichert
+ Hashfunktion $h:$ $U→\{0,1,...,m-1\}$
+ ![[../../../../z_images/Pasted image 20221113105055.png]]

### Kollisionsproblem
+ endlich große Tabelle
+ Menge der möglichen Schlüssel größer
+ Kollision
	+ unterschiedliche Schlüssel haben denselben Index
+ Belegungsfaktor $\alpha=\frac{m}{n}$

### Kollisionsbehandlung
+ Überläuferlisten (Chaining)
	+ Daten in verkettete Liste speichern bei Kollision
	+ ![[../../../../z_images/Pasted image 20221113111059.png]]
	+ Laufzeiten
		+ worst case $Θ(n)$ für Suchen, Löschen
			+ sehr unwahrscheinlich
			+ ![[../../../../z_images/Pasted image 20221113111441.png]]
		+ ![[../../../../z_images/Pasted image 20221113111156.png]]
+ Offene Adressierung
	+ Werte direkt in Tabelle speichern
		+ ![[../../../../z_images/Pasted image 20221113112247.png]]
	+ Bei Kollision wird neue Adresse berechnet bis freie gefunden
		+ ![[../../../../z_images/Pasted image 20221113112344.png]]
	+ Näherungen
		+ ![[../../../../z_images/Pasted image 20221113112524.png]]
	+ Löschproblem
		+ ![[../../../../z_images/Pasted image 20221113113048.png]]
		+ Lösung
			+ ![[../../../../z_images/Pasted image 20221113113114.png]]
	+ Operationen
		+ ![[../../../../z_images/Pasted image 20221113113151.png]]

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
	+ ![[../../../../z_images/Pasted image 20221113105721.png]]

### Arten von Hashfunktionen
+ Divisionsmethode
	+ ![[../../../../z_images/Pasted image 20221113105906.png]]
	+ schnell berechenbar
	+ nicht für alle m geeignet
		+ gutes m, wenn prim
		+ e.g. $m=2^k$
		+ $h(w)$ hängt von letzten $k-1$ Stellen ab
+ Multiplikationsmethode
	+ Nachkommastellen von Multiplikation mit Konstante $A$
	+ Multiplikation mit m abrunden
	+ ![[../../../../z_images/Pasted image 20221113110623.png]]
	+ unabhängig vom m

### Laufzeiten
+ ![[../../../../z_images/Pasted image 20221113113249.png]]