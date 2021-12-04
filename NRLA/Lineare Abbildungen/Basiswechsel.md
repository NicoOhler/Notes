# Basiswechsel
### Koordinatentransformation
+ alte und neue Abbildung mit gewünschter Basis werden über identische Abbildung verknüpft
	+ ![[Pasted image 20211204154219.png]]
+ lineare Transforrmation
	+ ![[Pasted image 20211204155133.png]]
+ Transformationsmatrix
	+ Spalten sind Koordinatenvektoren der alte Basisvektoren
	+ muss invertierbar sein ==> Transformation in beide Richtungen möglich
	+ n Dimensionen ==> n Gleichungssysteme zu lösen

### Praktische Umsetzung
+ Gleichungssystem aufstellen mit Transformationsmatrix
	+ n Gleichungen ==> viel Rechenaufwand
+ Rechenaufwand mindern
	+ B ist kanonische Basis in V
	+ Orthonormalbasis für B
		+ $<b_j, b_k>=δ_{jk}$ - Kronecker-Delta
		+ Vektoren paarweise orthogonal + Einheitsvektoren
	+ $V=ℝ^n$
		+ 