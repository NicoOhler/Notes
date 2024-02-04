### Definition
+ Heap wird auch Halde genannt
+ ![[../../../../z_images/Pasted image 20221029175134.png]]
+ ![[../../../../z_images/Pasted image 20221029175226.png]]
+ nicht automatisch absteigend sortiert
+ Darstellung als Graph/Binärbaum
	+ siehe [[Bäume & Spannbäume]]
	+ ![[../../../../z_images/Pasted image 20221029175629.png]]
+ Eigenschaften
	+ $A[0]$ ist Maximum (Wurzel) 
	+ vollständiger Baum
		+ letzte Ebene evtl. nicht komplett
	+ jeder Teilbaum wieder Halde
	+ $h=\lfloor log_2(n)\rfloor$

### Heapify
+ Verhalde-Prozedur
	+ ![[../../../../z_images/Pasted image 20221029181517.png]]
	+ ![[../../../../z_images/Pasted image 20221029181546.png]]
+ Aufbau einer Halde mittel Heapify
	+ gegeben lineares Feld in beliebiger Reihenfolge
	+ Blätter (einzelnes Element) sind triviale Halden
	+ Verhalde auf Eltern der Blätter (vorletzte Schicht) anwenden
	+ Wiederholen für alle Knoten bis zur Wurzel
	+ ![[../../../../z_images/Pasted image 20221029182046.png]]
	+ Laufzeit
		+ ![[../../../../z_images/Pasted image 20221029182332.png]]
		+ ![[../../../../z_images/Pasted image 20221029182846.png]]