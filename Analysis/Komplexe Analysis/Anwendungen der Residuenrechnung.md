# Anwendungen der Residuenrechnung
### Zählen von Nullstellen
+ gesucht # Nullstellen innerhalb von C (Vielfachheit gezählt)
+ U sternförmig, f∈H(U), C geschlossen in U
+ ![[Pasted image 20220526105612.png]]
+ ![[Pasted image 20220526105537.png]]
	+ ![[Pasted image 20220526105600.png]]
+ ![[Pasted image 20220526110109.png]]
+ Satz vom logarithmischen Residuum
	+ ![[Pasted image 20220526110214.png]]
+ Satz von Rouchê
	+ ![[Pasted image 20220526111034.png]]
	+ ![[Pasted image 20220526111042.png]]
	+ Beispiel
		+ ![[Pasted image 20220526111225.png]]
		+ ![[Pasted image 20220526111626.png]]

### Bestimmung von Integralen
+ rationale Funktionen
	+ $R(x)=\frac{p(x)}{q(x)}$, für die gilt
		+ p, q Polynome
		+ $deg(p)<deg(q)-2$
		+ q hat keine reellen Nullstellen
	+ ![[Pasted image 20220608113244.png]]
		+ Summe der Residuen von Polen $z_0$ mit $Im(z_0)>0$
		+  ![[Pasted image 20220608113221.png]]
	+ Beispiel:
		+ Pol erster Ordnung
			+ ![[Pasted image 20220608113656.png]]
			+ ![[Pasted image 20220608113710.png]]
		+ Pol höherer Ordnung
			+ ![[Pasted image 20220608113813.png]]
+ rationale Funktionen in Winkelfunktionen
	+ $R(cos(x),sin(x))$
		+ Winkelfunktionen durch komplexe Äquivalent ersetzen
			+ $cos(x)=\frac{1}{2}(e^{ix}+e^{-ix})$
			+ $sin(x)=\frac{1}{2i}(e^{ix}-e^{-ix})$
		+ $e^{ix}$ substituieren mit $z$
			+ ![[Pasted image 20220608114739.png]]
	+ ![[Pasted image 20220608114253.png]]
	+ Beispiel:
		+ ![[Pasted image 20220608114906.png]]
+ rationale Funktionen mal $e^{itx}$
	+ ![[Pasted image 20220608121205.png]]
	+ $R(x)$ mit $deg(p)<deg(q)-2$
	+ $t=0$ 
		+ $e^{itx}=e^0=1$ ==> rationale Funktion ohne $e^{itx}$
	+ $t>0$
		+ obere Halbkreis wird integriert
		+ ![[Pasted image 20220608121133.png]]
	+ $t<0$
		+ untere Halbkreis wird integriert
		+ ![[Pasted image 20220608121345.png]]
	+ R reell ==> Konjugation von Integral für $t>0$ = Integral für $t<0$
	+ Beispiel:
		+ ![[Pasted image 20220608121915.png]]
		+ ![[Pasted image 20220608122218.png]]

[[Residuensatz]]