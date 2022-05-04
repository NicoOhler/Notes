# Inhomogene DGL mit mit konstanten Koeffizienten
### Übersicht
+ analog zu [[Lineare DGL mit konstanten Koeffizienten]] jedoch mit Störfunktion
+ $y^{(n)}+a_{n-1}*y^{(n-1)}+...+a_1*y'+a_0*y=s(t)$
	+ $s(t)$ Störfunktion
		+ Linearkombination von $e^{\lambda t}, te^{\lambda t},t^me^{\lambda t},...$
+ allgemeine Lösung der inhomogenen Gleichung
	+ $y(t)=y_P(t)+y_H(t)$
		+ $y_P(t)$ ist eine Lösung der inhomogenen Gleichung
		+ $y_H(t)$ ist allgemeine Lösung der homogenen Gleichung
+ innere Resonanz, wenn Nullstelle $\lambda$ mehrfach auftritt
+ äußere Resonanz für $f_i(x)$, wenn
	+ $f_i(x)$ eine Lösung der zugehörigen homogenen Differentialgleichung

### Ansatz für partikuläre Lösung
+ abhängig von Resonanz und s(x)
+ keine äußere
	+ ![[Pasted image 20220504123011.png]]
	+ ![[Pasted image 20220504123016.png]]
+ äußere und keine innere
	+ Ansatz x multiplizieren
+ äußere und innere
	+ Ansatz mit linearem Polynom x^n multiplizieren
	+ n ist Ordnung von $\lambda$
+ keine äußere und keine innere
	+ nicht mit Polynom multiplizieren
+ Cheat-Sheet
	+ ![[Pasted image 20220504151709.png]]

### Herleitung
+ ![[Pasted image 20220502143123.png]]

### Beispiele
+ ![[Pasted image 20220502144122.png]]
	+ ![[Pasted image 20220502144426.png]]
+ ![[Pasted image 20220502152349.png]]
	+ ![[Pasted image 20220502152440.png]]
+ ![[Pasted image 20220502153239.png]]
	+ ![[Pasted image 20220502153314.png]]



