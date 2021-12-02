# Differentialrechnung
### Probleme
+ Tangentenproblem
	+ Gerade, welche Funktionsgraph in x<sub>0</sub> berührt
	+ Tangentengleichung: $y=f(x_0)+k(x-x_0)$
	+ Steigung k ist zu bestimmen
		+ $k=\lim{x \to x_0} \frac{f(x)-f(x_0)}{x-x_0}$
		+ Differenzenquotient
+ Problem der ersten Näherung
	+ $\frac{f(x)-f(x_0)}{x-x_0}=k+r(x)$
	+ r(x) - Fehler
	+ stetig, wenn Fehler gegen 0 geht
		+ $\frac{f(x)-f(x_0)}{x-x_0}=k+r(x)$ <==>$k=\lim{x \to x_0} \frac{f(x)-f(x_0)}{x-x_0}$
	+ Problem der Momentangeschwindigkeit
		+ $\frac{s(t)-s(t_0)}{t-t_0}$ - mittlere Geschwindigkeit
		+ $\lim{t \to t_0} \frac{s(t)-s(t_0)}{t-t_0}$ - Momentangeschwindigkeit zum Zeitpunkt $t_0$

### Differenzierbarkeit
+ differenzierbar, wenn
	+ f: \[a,b]-->ℝ stetig
	+ in jedem Punkt $x_0$∈\[a,b] existiert der Grenzwert $\lim{x \to x_0} \frac{f(x)-f(x_0)}{x-x_0}$
+ f': \[a,b]-->ℝ, x-->$\lim{x \to x_0} \frac{f(x)-f(x_0)}{x-x_0}$ ist die erste Ableitung
+ f in $x_0$ differenzierbar ==> f in $x_0$ stetig
	+ Umkehrung gilt nicht

### Rechenregeln
+ f, g sind differenzierbar
+ Summenregel
	+ $(f+g)(x)=f(x)+g(x)$ ==> $(f+g)'=f'+g'$
+ Produktregel
	+ $(f*g)(x)$ ==> $(f*g)'=f'*g+f*g'$
+ Kettenregel
	+ $(f.g)'(x)=f'(g(x)$
+ Quotientenregel