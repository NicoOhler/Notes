# Nicht Lineare Rekursion
### Binomial Lehrsatz für nicht lineare Rekursionen
+ ![[Pasted image 20220428152048.png]]

### Binärbaum
+ Binärbaum △ rekursiv definiert, wenn
	+ einzelner externer Knoten oder
	+ interner Knoten zusammen mit Binärbaum links und rechts 
		+ links $△_l$
		+ rechts $△_r$
+ interne Knoten heißen Wurzel
+ externe Knoten heißen Blätter
+ ![[Pasted image 20220428153058.png]]
+ Beispiele: 
	+ Anzahl der Menge von Binärbaume mit n Blättern
		+ ![[Pasted image 20220428153307.png]]
	+ Catalansche Zahl
		+ $\frac{1}{n}\binom{2n-2}{n-1}$
		+ ![[Pasted image 20220428163628.png]]

### Quicksort
+ Sortieralgorithmus
+ gegeben Array von unterschiedlichen Elementen
+ Divide and Conquer
	+ in zwei Subarrays aufteilen
	+ Teilarrays rekursiv sortieren
	+ sortierte Arrays zusammenfügen
+ Input
	+ Array a
	+ linke/kleinste Index l
	+ rechte/größte Index r
+ zwischen l und r wird sortiert
+ l=1 und r=n beim ersten Aufruf
+ Algorithmus
	+ p:=a\[r] ist Pivot-Element
	+ vergleiche a\[l] bis a\[r-1] mit p
	+ sortiere um, sodass
		+ a\[k]=p
		+ a\[i]\<p für i\<k
		+ a\[i]\>p für i\>k
	+ ruf Quicksort rekursiv erneut auf
		+ 


[[Lineare Rekursion]]