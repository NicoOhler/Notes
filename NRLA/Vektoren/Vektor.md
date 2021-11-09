# Vektor
+ $\overrightarrow{a}$ = (a<sub>x</sub>, a<sub>y</sub>, a<sub>z</sub>) - 3D
+ Strecken mit bestimmter Länge und Richtung OHNE Ausgangspunkt
+ mehrdimensional
+ eine Komponenten für jede Dimension
+ Länge des Vektors = Betrag des Vektors
	+ $|\overrightarrow{a}| = \sqrt[2]{a_x^2 + a_y^2}$ - 2D
	+ $|\overrightarrow{a}| = \sqrt[2]{a_x^2 + a_y^2 + a_z^2}$ - 3D

### Beispiele
+ Ortsvektor 0 = (0, 0, 0)
+ Identische Vektoren ==> ident in allen Komponenten
	+ können jedoch unterschiedliche Ausgangspunkte vorweisen
	+ können somit parallel verschoben sein
+ Gegenvektor von $\overrightarrow{a}$ ist -$\overrightarrow{a}$
	+ komplett ident, jedoch mit umgekehrter Richtung
+ Nullvektor  $\overrightarrow{0}$ ==> Betrag 0

### Grundrechnungsarten
+ Addition
	+ Vektor a an b durch passende Verschiebung anhängen
		+ Anfang von b = Ende von a
		+ Anfang von a bis Ende von b =  $\overrightarrow{a + b}$
	+ Summenvektor erhält man durch Aufsummieren der Komponenten
		+ $\overrightarrow{a + b} = \overrightarrow{a} + \overrightarrow{b} = (a_x + b_x, a_y + b_y, a_z + b_z)$ 
+ Subtraktion
	+ gleich der Addition, jedoch wird der Gegenvektor addiert
	+ Differenzvektor  erhält man durch Subtrahieren der Komponenten
		+ $\overrightarrow{a - b} = \overrightarrow{a} + (- \overrightarrow{b}) = (a_x - b_x, a_y - b_y, a_z - b_z)$
+ Multiplikation mit Skalar
	+  $\overrightarrow{a} * λ =$ Vektor mit gleicher Richtung, jedoch mit λ-fachen Betrag
	+  jede Komponente wird mit λ multipliziert
+  Skalarprodukt <a, b>
	+  Produkt der Beträge multipliziert mit Cosinus des Winkels α dazwischen $|\overrightarrow{a}| * |\overrightarrow{b}| * cos(α)$
	+  Vektoren senkrecht zueinander ==> cos(90°) = 0 ==> Skalarprodukt = 0
+  Kreuzprodukt/Vektorprodukt
	+  nur in $ℝ^3$
	+  Kreuzprodukt zweier Vektoren a und b = a×b
		+  liefert dritten Vektor c
		+  c steht senkrecht zu a und b
		+  Länge von c = |a×b| = Fläche des von a und b aufgespannten Parallelogramm
		+  ![[Pasted image 20211109131952.png]]
	+  Rechte-Hand-Regel
	+ $|a×b| = |\overrightarrow{a}| * |\overrightarrow{b}| * sin(α)$
	+ Rechenregeln
		+ a×b = -b×a
		+ a×(b×c) = a×b + a×c
		+ 0×a = a×0 = 0
		+ a×b = 0 ==> kolinear ==> α = 0
+  Spatprodukt
