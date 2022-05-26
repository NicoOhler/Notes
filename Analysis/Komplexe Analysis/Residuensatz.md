# Residuensatz
###  Meromorphität
+ Funktion f ist meromorph auf U, wenn
	+ A⊆U hat in U keine Häufungspunkte
	+ f holomorph auf U bis auf A
	+ f hat in A höchstens Pole
	+ A Menge der Singularitäten in f

### Residuensatz
+ $\oint_Cf(z)dz=2\pi i\sum_{a∈A}Ind_C(a)Res_{z=a}f(z)$, wenn
	+ f meromorph auf U
	+ U sternförmig
	+ A die Menge der Singularitäten von f
	+ C eine geschlossene Kurve in U, die nicht durch A verläuft
+ Beispiel
	+ ![[Pasted image 20220526104241.png]]
	+ ![[Pasted image 20220526104257.png]]
	+ ![[Pasted image 20220526104312.png]]

### Bestimmung von Residuen
+ Pole erster Ordnung
	+ $\frac{p(z)}{q(z)}$
		+ $p(z)$ holomorph um $z_0$
		+ $q(z_0)=0$, $q'(z_0)≠0$
	+ $Res_{z=z_0}\frac{p(z)}{q(z)}=\frac{p(z_0)}{q'(z_0)}$
+ Pole höherer Ordnung m>1
	+ ![[Pasted image 20220526104933.png]]

### Anwendungen der Residuenrechnung
+ Zählen von Nullstellen
	+ U sternförmig, f∈H(U), C geschlossen in U
	+ ![[Pasted image 20220526105537.png]]
		+ ![[Pasted image 20220526105600.png]]
	+ ![[Pasted image 20220526105612.png]]
	+ gesucht # Nullstellen innerhalb von C (Vielfachheit gezählt)
	+ 

[[Singularität]]