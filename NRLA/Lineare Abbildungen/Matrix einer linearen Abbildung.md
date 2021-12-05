# Matrix einer linearen Abbildung
+ jeder endlich-dimensionale VR V ist gleichwertig zu $ℝ^n,ℂ^n$
+ V --> W lineare Abbildung
	+ lineare Transformation
	+ Transformationsmatrix
		+ Spaltenvektoren der die lineare Abbildung F darstellenden Matrix M sind die Koordinatenvektoren der Bilder des Basisvektoren
			+ $C_B(F(v_1)),...,C_B(F(v_n))$
		+ Beispiel
			+ ![[Pasted image 20211204184201.png]]

### Komposition von linearen Abbildungen
+ Komposition wird wird durch das Produkt der darstellenden Transformationsmatrizen beschrieben

### Inverse eines Isomorphismus
+ Transformationsmatrix muss regulär sein bei isomorpher Abbildung
	+ Inverse ist Transformationsmatrix für Umkehrabbildung 

### Rang der Transformationsmatrix
+ $V^n$-->$W^m$
+ $M_B^A(F)∈ℝ^{m×n}$
+ F injektiv <==> Kern(F)={0} <==> Rang(M(F))=n
+ F surjektiv <==>Bild(F)=W <==> Rang(M(F))=m
+ F bijektiv <==> dim(V)=dim(W) <==> Rang(M(F))=n <==> $M_B^A(F)$ regulär
