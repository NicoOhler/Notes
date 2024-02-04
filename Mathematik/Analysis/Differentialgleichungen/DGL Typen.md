### Getrennte Variablen
+ x und y voneinander trennbar
+ Vorgehensweise:
	+ gegeben: $y'=\frac{f(x)}{g(y)}=\frac{dy}{dx}$
	+ nach Umformung: $g(y)dy=f(x)dx$
	+ nach Integration: $G(y)=F(x)+C$
	+ ![](Pasted%20image%2020220412173422.png)
+ Beispiele:
	+ ![](Pasted%20image%2020220412173917.png)
	+ ![](Pasted%20image%2020220412174224.png)
		+ nicht möglich, da Lösung Definitionsbereich verlässt

### Lineare DGL
+ $y'=a(x)y$==>$\frac{y'}{y}=a(x)$
+ wenn $y(x_0)=0$ ==> laut Satz von P-L $y(x)=0$ für alle x
+ $ln|y(x)|=\int a(x)dx$
	+ $y(x)=C*e^{A(x)}$ ist allgemeine Lösung
+ Beispiel:
	+ ![](Pasted%20image%2020220412175042.png)

### Inhomogene lineare DGL
+ $y'=a(x)y+b(x)$
	+ $b(x)$ ==> Inhomogenität durch Störfunktion
+ Vorgehensweise:
	+ homogene GL lösen
		+ $y_H'=a(x)y_H(x)$ ==> $y_H(x)=C*e^{A(x)}$
	+ inhomogene GL lösen
		+ $y_P(x)=C(x)*e^{A(x)}$
			+ $C(x)$ gesuchte Funktion
			+ Variation der Konstanten
		+ $y_P=C'(x)*e^{A(x)}+C(x)*e^{A(x)}*a(x)=a(x)*C(x)*e^{A(x)}+b(x)$
			+ ==> $C'(x)=b(x)*e^{-A(x)}$ ==> $C(x)=\int b(x)*e^{-A(x)}dx$
	+ $y(x)=y_P(x)+D*e^{A(x)}$
		+ allgemeine Lösung
		+ homogene + partikuläre Lösung
+ Beispiel:
	+ ![](Pasted%20image%2020220413090213.png)
	+ ![](Pasted%20image%2020220413090708.png)

### Exakte DGL
+ $P(x,y)dx+Q(x,y)dy=0$ <==> $y'=\frac{dy}{dx}=-\frac{P(x,y)}{Q(x,y}$
	+ Stammfunktion existiert, wenn $\frac{\partial Q}{\partial x}=\frac{\partial P}{\partial y}$
		+ wenn nicht exakt ==> Multiplikation mit integrierenden Faktor μ(x)
			+ alternative Formen $\mu(x)$ in Reihenfolge zum Versuchen
			+ desto mehr Versuche desto verzweifelter
			+ ![](Pasted%20image%2020220413092948.png)
		+ $\mu(x)$ bestimmen
			+ ![](Pasted%20image%2020220413092458.png)
			+ DGL nach $\mu(x)$ lösen
		+ siehe 2. Beispiel
	+ Stammfunktion: $d\phi=0$ ==> $\phi(x,y)=const$
		+ Lösungen von $P(x,y)dx+Q(x,y)dy=0$ sind Niveaulinien von $\phi$
+ Beispiele:
	+ ohne $\mu(x)$
		+ ![](Pasted%20image%2020220413091800.png)
	+ mit $\mu(x)$
		+ ![](Pasted%20image%2020220413092634.png)
		+ ![](Pasted%20image%2020220413092916.png)
	+ mit $\mu(x*y)$
		+ ![](Pasted%20image%2020220413093600.png)
		+ ![](Pasted%20image%2020220413093614.png)
	+ Lotka-Volterra Räuber-Beute-Modell
		+ ![](Pasted%20image%2020220413094158.png)
		+ ![](Pasted%20image%2020220413094541.png)
	+ logistisches Wachstum
		+ ![](Pasted%20image%2020220413094851.png)


[[Differentialgleichungen]]