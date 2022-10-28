### Eigenschaften
+ [[Divide & Conquer]] Algorithmus
+ Verfahren
	+ zerlege Feld in zwei Felder
		+ linke Feld mit Elementen ≤ Elementen in rechtem Feld
	+ Feld weiterzerlegen
		+ QuickSort rekursiv aufrufen
	+ ![[Pasted image 20221028153656.png]]

### Partitioning
+ gegeben Zahl p
+ sortiere Feld, sodass
	+ links Zahlen ≤ p
	+ rechts Zahlen > p
	+ Feld wird von beiden Seiten durchlaufen
		+ Elemente vertauschen, wenn Bedingung nicht erfüllt
	+ treffen sich beide Indizes in der Mitte 
		+ fertig
	+ 
	+ ![[Pasted image 20221028153947.png]]