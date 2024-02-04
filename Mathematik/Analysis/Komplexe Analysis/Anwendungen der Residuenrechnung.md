### Zählen von Nullstellen
+ gesucht # Nullstellen innerhalb von C (Vielfachheit gezählt)
+ U sternförmig, f∈H(U), C geschlossen in U
+ ![](../../z_images/Pasted%20image%2020220526105612.png)
+ ![](../../z_images/Pasted%20image%2020220526105537.png)
	+ ![](../../z_images/Pasted%20image%2020220526105600.png)
+ ![](../../z_images/Pasted%20image%2020220526110109.png)
+ Satz vom logarithmischen Residuum
	+ ![](../../z_images/Pasted%20image%2020220526110214.png)
+ Satz von Rouchê
	+ ![](../../z_images/Pasted%20image%2020220526111034.png)
	+ ![](../../z_images/Pasted%20image%2020220526111042.png)
	+ Beispiel
		+ ![](../../z_images/Pasted%20image%2020220526111225.png)
		+ ![](../../z_images/Pasted%20image%2020220526111626.png)

### Bestimmung von Integralen
+ rationale Funktionen
	+ $R(x)=\frac{p(x)}{q(x)}$, für die gilt
		+ p, q Polynome
		+ $deg(p)<=deg(q)-2$
		+ q hat keine reellen Nullstellen
	+ ![](../../z_images/Pasted%20image%2020220608113244.png)
		+ Summe der Residuen von Polen $z_0$ mit $Im(z_0)>0$
		+  ![](../../z_images/Pasted%20image%2020220608113221.png)
	+ Beispiel:
		+ Pol erster Ordnung
			+ ![](../../z_images/Pasted%20image%2020220608113656.png)
			+ ![](../../z_images/Pasted%20image%2020220608113710.png)
		+ Pol höherer Ordnung
			+ ![](../../z_images/Pasted%20image%2020220608113813.png)
+ rationale Funktionen in Winkelfunktionen
	+ $R(cos(x),sin(x))$
		+ Winkelfunktionen durch komplexe Äquivalent ersetzen
			+ $cos(x)=\frac{1}{2}(e^{ix}+e^{-ix})$
			+ $sin(x)=\frac{1}{2i}(e^{ix}-e^{-ix})$
		+ $e^{ix}$ substituieren mit $z$
			+ ![](../../z_images/Pasted%20image%2020220608114739.png)
	+ ![](../../z_images/Pasted%20image%2020220608114253.png)
	+ Beispiel:
		+ ![](../../z_images/Pasted%20image%2020220608114906.png)
+ rationale Funktionen mal $e^{itx}$
	+ ![](../../z_images/Pasted%20image%2020220608121205.png)
	+ $R(x)$ mit $deg(p)<deg(q)-2$
	+ $t=0$ 
		+ $e^{itx}=e^0=1$ ==> rationale Funktion ohne $e^{itx}$
	+ $t>0$
		+ obere Halbkreis wird integriert
		+ ![](../../z_images/Pasted%20image%2020220608121133.png)
	+ $t<0$
		+ untere Halbkreis wird integriert
		+ ![](../../z_images/Pasted%20image%2020220608121345.png)
	+ R reell ==> Konjugation von Integral für $t>0$ = Integral für $t<0$
	+ Beispiel:
		+ ![](../../z_images/Pasted%20image%2020220608121915.png)
		+ ![](../../z_images/Pasted%20image%2020220608122218.png)

### [[Laplace Transformation]]

[[Residuensatz]]