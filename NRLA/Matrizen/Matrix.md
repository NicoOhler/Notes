# Matrix
+ Rechteckige, tabellenähnliche Anordnung von Elementen (meist Zahlen)
+ Mehrere Matrizen können Zusammenhänge darstellen oder auch Rechenvorgänge erleichtern.
	+ z.B. Adjazenzmatrix, Lineare Gleichungsysteme
+ Auf diese lassen sich bestimmte Rechenregeln anwenden.
+ Matrix A: ℝ<sup>mxn</sup>  
	+ m = Zeilen = 3,  i = Zeilenindex
	+ n = Spalten = 3,  j = Spaltenindex
	+ a<sub>ij</sub> = Element der i-ten Zeile und j-ten Spalte
	<br>

	1 | 0 | 0 
	--- | --- | ---
	0 | 1 | 0 
	0 | 0 | 1 

### Arten von Matrizen
+ quadratische Matrix ==> m=n
+ Einheitsmatrix I<sub>n</sub> ==> Nichtnullelemente nur in der Hauptdiagonale (i=j)
+ obere/untere Dreiecksmatrix ==> Nichtnullelemente nur in und ober/unterhalb der Hauptdiagonale
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
+  Addition von Matrix A (mxn) zu Matrix B (mxn)
	+ a<sub>ij</sub> + b<sub>ij</sub> für alle Elemente
+ Multiplikation von Matrix mit Skalar
	+ Skalar mit jedem Element der Matrix multiplizieren
+  Multiplikation von Matrix A (mxn) mit Matrix B (mxn)
	+  Spaltenanzahl der linken = Zeilenanzahl der rechten
	+ (AB)<sub>ij</sub>= Σ von k=0 bis i (a<sub>ik</sub>*b<sub>ki</sub>)
+ k-te Potenz von Matrix A
	+ A<sup>k</sup> = Π von 

[[NRLA]]