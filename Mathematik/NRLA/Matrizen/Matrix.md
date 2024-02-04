+ Rechteckige, tabellenähnliche Anordnung von Elementen (meist Zahlen)
+ Mehrere Matrizen können Zusammenhänge darstellen oder auch Rechenvorgänge erleichtern.
	+ z.B. Adjazenzmatrix, Lineare Gleichungsysteme
+ Auf diese lassen sich bestimmte Rechenregeln anwenden.
+ Matrix A: ℝ<sup>m×n</sup>  
	+ m = Zeilenanzahl = 3,  i = Zeilenindex
	+ n = Spaltenanzahl = 3,  j = Spaltenindex
	+ a<sub>ij</sub> = Element der i-ten Zeile und j-ten Spalte
	+ Hauptdiagonale: Diagonale von links oben nach rechts unten bzw. alle  a<sub>ij</sub> mit i=j
		+ a<sub>11</sub>, a<sub>22</sub>, a<sub>33</sub>
	<br>

	1 | 0 | 0 
	--- | --- | ---
	0 | 1 | 0 
	0 | 0 | 1 

### Arten von Matrizen
+ quadratische Matrix ==> m=n
+ symmetrische Matrix
	+ symmetrisch entlang der Hauptdiagonale
	+ jedes Element a<sub>ij</sub> = a<sub>ji</sub>
	+ 
	2 | 4 | 3 
	--- | --- | ---
	4 | 1 | 0 
	3 | 0| 1 
+ Einheitsmatrix/Identitätsmatrix I<sub>n</sub> ==> Elemente in der Hauptdiagonale (i=j) sind 1, ansonsten 0
	+ 
	1 | 0 | 0 
	--- | --- | ---
	0 | 1 | 0 
	0 | 0 | 1 
+ Diagonalmatrix ==> Nichtnullelemente in der Hauptdiagonale, ansonsten 0
	+ z.B. Einheitsmatrix
+ obere/untere Dreiecksmatrix ==> Nichtnullelemente nur in und ober/unterhalb der Hauptdiagonale
	+ z.B. Einheitsmatrix
+ Transponierte Matrix A<sup>T</sup> ==> gespiegelt an der Hauptdiagonale
	+ 1 | 0 
	--- | ---
	2| 3
	2| 3
	+ 1 | 2 | 2 
	--- | --- | ---
	0 | 3 | 3 
	
+ Inverse Matrix A<sup>-1</sup> ==> AxA<sup>-1</sup> = I<sub>n</sub>
	+ muss quadratisch sein
	+ Achtung: nicht jede quadratische Matrix ist invertierbar
	+ Matrizen sind regulär wenn invertierbar ansonsten singulär
	+ 2 | 1 
	--- | ---
	6| 4
	+ 2 | -0.5  
	--- | --- 
	-3 | 1 
	
### Rechenoperationen auf Matrizen
+ Addition von Matrix zu Skalar
	+ Skalar zu jedem Element der Matrix addieren
+  Addition von Matrix A (m×n) zu Matrix B (m×n)
	+ a<sub>ij</sub> + b<sub>ij</sub> für alle Elemente
+ Multiplikation von Matrix mit Skalar
	+ Skalar mit jedem Element der Matrix multiplizieren
+  Multiplikation von Matrix A (m×n) mit Matrix B (m×n)
	+  Spaltenanzahl der linken = Zeilenanzahl der rechten
	+ (AB)<sub>ij</sub>= Σ von k=0 bis i (a<sub>ik</sub>*b<sub>ki</sub>)
+ k-te Potenz von Matrix A
	+ A<sup>k</sup> = Π von i=1 bis k (A)
	+  A<sup>3</sup> = A\*A\*A


[[NRLA]]