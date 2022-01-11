# NRLA Stoff
### 
+ Lineare Abbildungen
	+ Linearität bzgl. Addition, Skalarmultiplikation und Kombination
	+  Kern(F):=$\{\overrightarrow{v}∈V:\overrightarrow{v}$-->$\overrightarrow{0}\}$
		+ Kern von F = Menge aller Elemente, welche Null abbilden
	+ Bild(F):=$\{F(\overrightarrow{v}):\overrightarrow{v}∈V\}$
		+ Bild von F = Menge aller Elemente in V erreichbar durch Abbildung F
	+ Isomorph <==> bijektiv und linear
	+  injektiv ==> jedes Element in Zielmenge wird höchstens 1x abgebildet
		+ injektiv, wenn Kern(F)={0}
	+ surjektiv ==> jedes Element in Zielmenge wird mindestens 1x abgebildet
		+ surjektiv, wenn Bild(F)=Zielmenge
	+ bijektiv ==> jedes Element in Zielmenge wird genau 1x abgebildet
		+ invers möglich
		+ F' auch linear
	+ Verknüpfungen linearer Abbildungen?
	+ lineare Abbildungen konstruieren?
	+ Koordinaten-Abbildung?
	+ Basiswechsel - Koordinatentransformation TODO
	+ lineare Abbildung = Matrixmultiplikation TODO
+ Unitäre Räume
	+ Norm/Länge
		+ Norm/Betrag/Länge
			+ $||x||=\sqrt{x_1^2+...+x_n^2}$
			+ induzierte Norm  $||x||=\sqrt{<x ,x>}$
			+ Abstand $d(v,w);=||v-w||$ 
		+ inneres Produkt  $<x,y>=x_1 y_1+...+x_n y_n$ bestimmt Winkel
			+ orthogonal, wenn $<x,y>=0$ 
	+ Orthonormierungsverfahren nach Gram-Schmidt
	+ QR Zerlegung
		+ A=QR
		+ Q durch Gram-Schmidt
		+ $R = Q^TA$
+ Eigenwerte und Eigenvektoren
	+ Eigenwerte bestimmen
		+ Lösen der charakteristischen Gleichung $det(A-λI)=0$
			+ lambda² + spur + det?
		+ Polynom als Lösung
		+ dessen Nullstellen/Eigenwerte und Vielfachheiten bestimmen
+ Eigenvektoren bestimmen
	+ Gleichung $(A-λI)v=0$ für alle Eigenwerte lösen
		+ ∞ Lösungen
	+ Eigenraum/span/Dimensionen bestimmen
		+ $Eigen(λ_*,A)=Span({v_1,...,v_n})$
		+ geometrische Vielfachheit = $dim Eigen(λ_*,A)$
	+ 1 ≤ geom V(λ) ≤ alg V(λ)
+ Diagonalisierung
	+ diagonalisierbar, wenn A n l. u. EV besitzt
	+ diagonalisierbar, wenn $D=S^{-1}AS$
	+ ONB aus EV bilden
+ Methode der kleinsten Quadrate
	+ yes