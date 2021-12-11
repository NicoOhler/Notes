# Orthonormieren nach GRAM-SCHMIDT
+ im reellen unitären VR $φ:=<(v,w)=arcos(\frac{<v,w>}{||v||||w||})$
	+ $-1≤\frac{<v,w>}{||v||||w||}≤1$
		+ wegen Schwarzsche Ungleichung
		+ $0≤φ≤π$
	+ kein Winkel für $v=0$ oder $w=0$
+ Eigenschaften
	+ $<(v,w)=<(w,v)$
	+ $v,w≠0$ und $<v,w>=0$ ==> $<(v,w)=\frac{π}{2}$ ==> v orthogonal zu w
	+  $<(v,-v)=π$
+  WInkelmessung hängt von der Definition des Skalarprodukt ab
+  im $V=ℝ^n$
	+  Winkel bzgl. kanonischem Skalarprodukt ist der "geometrische" Winkel

### Orthogonalität und orthonormiert
+ im unitären VR sind v und w orthogonal, wenn
	+ $<v,w>=0$ bzgl. gewähltem Skalarprodukt
+ {} ≠ A ⊆ V ist orthonormiert, wenn
	+ alle v∈A normiert
	+ alle v∈A die Länge 1 haben <==> ||v||=1
	+ paarweise orthogonal sind
+ Jede endlich orthonormierte Teilmenge eines unitären VR mit <,> ist linear
	+ Beweis VO#18 1:43

### Orthonormierungsverfahren von GRAM-SCHMIDT
+ ![[Pasted image 20211211140604.png]]
	+ Orthogonale Projektion des $v_2$ auf den von $v_1$  aufgespannten Unterraum
	+ $v_2^*=<v_2,v_1'>$$v_1'$
		+ v' normierter Vektor von v
+ Verfahren
	+ unitärer VR V mit <,> und induzierter Norm $||.||=\sqrt{<,>}$
	+ linear unabhängige Menge des Raumes ${v_1,...,v_n}$
	+ Unterraum $W = {w_1,...,w_n}$ mit 
		+ $w_1=\frac{1}{||v_1||}$
		+ $w_j=\frac{1}{||u_j||}||u_j||$
			+ $||u_j||=v_j-v_j^*$

[[Unitäre Räume]] [[Schwarzsche Ungleichung]]