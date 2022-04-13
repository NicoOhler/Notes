# DGL Typen
### Getrennte Variablen
+ x und y voneinander trennbar
+ Vorgehensweise:
	+ gegeben: $y'=\frac{f(x)}{g(y)}=\frac{dy}{dx}$
	+ nach Umformung: $g(y)dy=f(x)dx$
	+ nach Integration: $G(y)=F(x)+C$
	+ ![[Pasted image 20220412173422.png]]
+ Beispiele:
	+ ![[Pasted image 20220412173917.png]]
	+ ![[Pasted image 20220412174224.png]]
		+ nicht möglich, da Lösung Definitionsbereich verlässt

### Lineare DGL
+ $y'=a(x)y$==>$\frac{y'}{y}=a(x)$
+ wenn $y(x_0)=0$ ==> laut Satz von P-L $y(x)=0$ für alle x
+ $ln|y(x)|=\int a(x)dx$
	+ $y(x)=C*e^{A(x)}$ ist allgemeine Lösung
+ Beispiel:
	+ ![[Pasted image 20220412175042.png]]

### Inhomogene lineare DGL
+ $y'=a(x)y+b(x)$
	+ $b(x)$ ==> Inhomogenität durch Störfunktion
+ Vorgehensweise:
	+ homogene GL lösen
		+ $y_H'=a(x)y_H(x)$ ==> $y_H(x)=C*e^{A(x)}$
	+ inhomogene GL lösen
		+ $y_P$

[[Differentialgleichungen]]