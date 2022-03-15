# Basiswechsel
### Koordinatentransformation
+ alte und neue Abbildung mit gewünschter Basis werden über identische Abbildung verknüpft
	+ ![[Pasted image 20211204154219.png]]
	+ kommutatives Diagramm
+ lineare Transforrmation
	+ ![[Pasted image 20211204155133.png]]
+ Transformationsmatrix
	+ Spalten sind Koordinatenvektoren der alte Basisvektoren
	+ muss invertierbar sein ==> Transformation in beide Richtungen möglich
	+ n Dimensionen ==> n Gleichungssysteme zu lösen

### Praktische Umsetzung
+ Gleichungssystem aufstellen mit Transformationsmatrix T
	+ n Gleichungen ==> viel Rechenaufwand
+ Möglichkeiten Rechenaufwand zu mindern
	+ B ist kanonische Basis in V
	+ Orthonormalbasis für B
		+ $<b_j, b_k>=δ_{jk}$ - Kronecker-Delta
		+ Vektoren paarweise orthogonal + Einheitsvektoren
	+ $V=ℝ^n$
		+ Abbildung dazwischen mit kanonischer Basis
		+ ![[Pasted image 20211204161531.png]]
		+ beide Transformationsmatrizen auf diese Abbildung bestimmen
			+ Matrix besteht aus Basisvektoren
				+ $M=(b_1,...,b_n)$
		+ Transformationsmatrix mal Inverse der anderen Transformationsmatrix
			+ $T_{alt} * T_{neu}^{-1}$
		+ Beispiel
			+ ![[Pasted image 20211204163106.png]]

[[Lineare Abbildungen]] [[Basis]]