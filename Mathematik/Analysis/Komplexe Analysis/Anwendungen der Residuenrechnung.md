### Zählen von Nullstellen
+ gesucht # Nullstellen innerhalb von C (Vielfachheit gezählt)
+ U sternförmig, f∈H(U), C geschlossen in U
+ ![](Pasted%20image%2020220526105612.png)
+ ![](Pasted%20image%2020220526105537.png)
	+ ![](Pasted%20image%2020220526105600.png)
+ ![](Pasted%20image%2020220526110109.png)
+ Satz vom logarithmischen Residuum
	+ ![](Pasted%20image%2020220526110214.png)
+ Satz von Rouchê
	+ ![](Pasted%20image%2020220526111034.png)
	+ ![](Pasted%20image%2020220526111042.png)
	+ Beispiel
		+ ![](Pasted%20image%2020220526111225.png)
		+ ![](Pasted%20image%2020220526111626.png)

### Bestimmung von Integralen
+ rationale Funktionen
	+ $R(x)=\frac{p(x)}{q(x)}$, für die gilt
		+ p, q Polynome
		+ $deg(p)<=deg(q)-2$
		+ q hat keine reellen Nullstellen
	+ ![](Pasted%20image%2020220608113244.png)
		+ Summe der Residuen von Polen $z_0$ mit $Im(z_0)>0$
		+  ![](Pasted%20image%2020220608113221.png)
	+ Beispiel:
		+ Pol erster Ordnung
			+ ![](Pasted%20image%2020220608113656.png)
			+ ![](Pasted%20image%2020220608113710.png)
		+ Pol höherer Ordnung
			+ ![](Pasted%20image%2020220608113813.png)
+ rationale Funktionen in Winkelfunktionen
	+ $R(cos(x),sin(x))$
		+ Winkelfunktionen durch komplexe Äquivalent ersetzen
			+ $cos(x)=\frac{1}{2}(e^{ix}+e^{-ix})$
			+ $sin(x)=\frac{1}{2i}(e^{ix}-e^{-ix})$
		+ $e^{ix}$ substituieren mit $z$
			+ ![](Pasted%20image%2020220608114739.png)
	+ ![](Pasted%20image%2020220608114253.png)
	+ Beispiel:
		+ ![](Pasted%20image%2020220608114906.png)
+ rationale Funktionen mal $e^{itx}$
	+ ![](Pasted%20image%2020220608121205.png)
	+ $R(x)$ mit $deg(p)<deg(q)-2$
	+ $t=0$ 
		+ $e^{itx}=e^0=1$ ==> rationale Funktion ohne $e^{itx}$
	+ $t>0$
		+ obere Halbkreis wird integriert
		+ ![](Pasted%20image%2020220608121133.png)
	+ $t<0$
		+ untere Halbkreis wird integriert
		+ ![](Pasted%20image%2020220608121345.png)
	+ R reell ==> Konjugation von Integral für $t>0$ = Integral für $t<0$
	+ Beispiel:
		+ ![](Pasted%20image%2020220608121915.png)
		+ ![](Pasted%20image%2020220608122218.png)

### [[Laplace Transformation]]

[[Residuensatz]]