# Matrix
+ Rechteckige, tabellenähnliche Anordnung von Elementen (meist Zahlen)
+ Mehrere Matrizen können Zusammenhänge darstellen oder auch Rechenvorgänge erleichtern.
	+ z.B. Adjazenzmatrix, Lineare Gleichungsysteme
+ Auf diese lassen sich bestimmte Rechenregeln anwenden.
+ Matrix A: ℝ<sup>mxn</sup>  
	+ m = Zeilen = 3,  i = Zeilenindex
	+ n = Spalten = 3,  j = Spaltenindex
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
	+ 2 | 1 
	--- | ---
	6| 4
	+ 2 | -0.5  
	--- | --- 
	-3 | 1 
	
### Rechenoperationen auf Matrizen
+ Addition von Matrix zu Skalar
	+ Skalar zu jedem Element der Matrix addieren
+  Addition von Matrix zu Matrix
	+ jedes M zu jedem Element der Matrix addieren
