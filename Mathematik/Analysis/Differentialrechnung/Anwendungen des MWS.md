+ Neue Schreibweise für $ln(1+x)$
	+  Da $ln'(1+x)=\frac{1}{1+x}=\sum_{n=0}^\infty (-1)^n x^n$ für $|x|<1$
		+ Ableitung der Potenzreihe = $\frac{1}{1+x}$ für $|x|<1$
		+ $g(x)=f(x)-ln(1+x)$ ==> $g'(x)=0$ ==> konstant
		+ $ln(1+x)=\sum_{n=1}^\infty (-1)^{n-1}\frac{x^n}{n}$ für $|x|<1$
		+ alternierende Reihe mit monoton fallenden Gliedern
	+ Leibnizkriterium anwendbar
		+ $|\sum_{n=1}^N (-1)^{n-1}\frac{x^n}{n}-ln(1+x)|≤\frac{x^{N+1}}{N+1}$ für 0 < x < 1
		+ Wegen Stetigkeit bleibt Ungleichung für x-->1 gültig
			+ $|\sum_{n=1}^N \frac{(-1)^{n-1}}{n}-ln(2)|≤\frac{1}{N+1}$ 
	+ Potenzreihendarstellung $\sum_{n=1}^\infty \frac{(-1)^{n-1}}{n}=ln(2)$
+ Neue Schreibweise für $arctan'(x)$
	+ $arctan'(x)=\frac{1}{1+x^2}=\sum_{n=0}^\infty (-1)^n x^{2n}$ für |x| < 1
		+ $arctan(x)=\sum_{n=0}^\infty (-1)^{n} \frac{x^{2n+1}}{2n+1})$
	+  Potenzreihendarstellung  $\sum_{n=0}^\infty \frac{(-1)^{n}}{2n+1} = \frac{π}{4}$
	+  Annäherung von π möglich
		+  ![](Pasted%20image%2020211209133537.png)
		+  desto größer n, desto mehr Nachkommastellen von π

### Beweis von Ungleichungen
+ Beispiel: für $x > -1$ gilt $ln(1+x) ≤ x$
	+ $h(x) = x - ln(1+x)$
	+ $h'(x) = 1 - \frac{1}{1+x}= \frac{x}{1+x}$
	+ $\frac{h(x)-h(0)}{x-0}=h'(εx)=\frac{εx}{1+εx}$ 0 < ε < 1
		+ mit x multipliziert
		+ $h(x)=\frac{εx^2}{1+εx}≥0$

### Berechnung von Grenzwerten - Bernoulli de l'Hospital
+ $f'(x_0)=\lim x \to x_0 (\frac{f(x)-f(x_0)}{x-x_0})$ = "$\frac{0}{0}$"
+ $\lim x \to x_0 f(x)=\lim x \to x_0 g(x)=0$
	+ laut verallg. MWS: $\frac{f(x)}{g(x)}=\frac{f(x)-f(x_0)}{g(x)-g(x_0)}=\frac{f'(ξ)}{g'(ξ)}$ für ξ zwischen x und x<sub>0</sub>
		+ wenn x-->x<sub>0</sub> geht, dann geth auch ξ-->x<sub>0</sub>
	+  Bernoulli de l'Hospital:
		+ Seien f,g auf x<sub>0</sub>∈I  diffbar und $f(x_0)=g(x_0)=0$
		+ Dann gilt:
			+ Wenn $\lim x \to x_0 \frac{f'(x)}{g'(x)}$ existiert
			+ dann existiert  $\lim x \to x_0 \frac{f(x)}{g(x)}$ und ist gleich
		+ darf mehrmals angewendet werden
			+ Grenzwert der n-ten Ableitung existiert ==> gleich für n-1 ==> ...
	+  de l'Hospital gilt auch für
		+ $\lim x \to x_0 f(x)=\lim x \to x_0 g(x)=\infty$ = "$\frac{\infty}{\infty}$"


[[Anwendungen der  Differentialrechnung]] [[Konvergenzkriterien für Reihen]]