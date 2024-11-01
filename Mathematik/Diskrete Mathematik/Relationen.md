 # Relationen
+ Relation auf X ist Beziehung zwischen Elementpaaren von x
+ xRy, wenn x zu y in Beziehung steht
	+ xRy <==> (x,y)∈R

### Relationsarten
+ Sei R ⊆ X×X eine Relation auf X
+ R ist
	+ reflexiv, wenn $∀x∈X: xRx$
		+ alle Elemente stehen zu sich selbst in Relation
	+ symmetrisch, wenn $∀x,y∈X: xRy$ ==> $yRx$
		+ a zu b in Relation, dann auch umgekehrt
	+ antisymmetrisch, wenn $∀x,y∈X: xRy∧yRx$ ==> x=y
		+ a zu b und b zu a muss a=b gelten
	+ transitiv, wenn 
		+ a zu b und b zu c, dann auch a zu c
+ R ist Äquivalenzrelation, wenn
	+ reflexiv, symmetrisch und transitiv
+ R ist Ordnungsrelation, wenn
	+ reflexiv, antisymmetrisch und transitiv

### Modulooperationen
+ ![](Pasted%20image%2020220317141822.png)

### Inverse
+ ![](Pasted%20image%2020220317142739.png)
+ $[a]_m∈ℤ_m$ ist invertierbar, wenn
	+ $∃b∈S:[a]_m*[b]_m=[b]_m*[a]_m=[1]_m$
+ $[a]_m=[b]_m^{-1}=$
+ Inverse $[n]_m^{-1}$ bestimmen
	+ ggT(m,n)=1
		+ sonst keine Inverse
	+ erweiterte euklidische Algorithmus anwenden
		+ a und b bestimmen
			+ $a_i, b_i$ mit i der Spalte bevor r=0
		+ $am+bn=1$
		+ $[b]_m$ ist Inverse

[[Diskrete Mathematik]]