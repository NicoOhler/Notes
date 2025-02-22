### Eigenschaften
+ [[Divide & Conquer]] Algorithmus
+ in-place
+ Verfahren
	+ zerlege Feld in zwei Felder
		+ linke Feld mit Elementen ≤ Elementen in rechtem Feld
	+ Feld weiterzerlegen
		+ QuickSort rekursiv aufrufen
	+ ![](Pasted%20image%2020221028153656.png)

### Partitioning
+ Pivot-Element p
+ sortiere Feld, sodass
	+ links Zahlen ≤ p
	+ rechts Zahlen > p
	+ Feld wird von beiden Seiten durchlaufen
		+ Elemente vertauschen, wenn Bedingung nicht erfüllt 
	+ treffen sich beide Indizes in der Mitte 
		+ fertig
	+ ![](Pasted%20image%2020221028153947.png)
+ ![](Pasted%20image%2020221028154444.png)

### Laufzeit
+ ![](Pasted%20image%2020221028154719.png)
+ Vorteil gegenüber [[MergeSort]]
	+ weniger Kopieren => schneller trotz schlechterer T(n)
	+ besseres S(n)

### Varianten
+ Randomisierte Pivotauswahl
	+ ![](Pasted%20image%2020221028155120.png)
+ Iterative Variante
	+ ![](Pasted%20image%2020221028155111.png)