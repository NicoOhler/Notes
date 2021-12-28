# Integralrechnung
+ Umkehraufgabe der Differentiation
+ F'=f - gesuchte Funktion F heißt Stammfunktion von f.
+ Da Konstanten beim Differentieren verschwinden, kann auf diese nicht zurückgeschlossen werden
	+ $F'+const = f$
	+ außer Wert der ursprünglichen Funktion ist gegeben
+ f: [a,b]-->ℝ
	+ $\int f(x)dx={F[a,b]-->ℝ|F'(x)=f(x)}=F(x)+C$
	+ unbestimmte Integral
	+ C∈ℝ
+ Tabelle bekannter Integrale
	+ siehe Skriptum S. X

### Rechenregeln
+ Linearität
	+ $\int λf(x)dx=λ\int f(x)dx+C$
+ $\int (f(x)+g(x))dx=\int f(x)dx + \int g(x)dx + C$
+ partielle Integration
	+ $\int f(x)G(x)dx=F(x)G(x)dx-\int F(x)g(x)dx$
	+ $\int v'u =vu-\int v u' + C$
+ Substitutionsregel
	+ ![[Pasted image 20211215170747.png]]
+ $\frac{1}{a}F(ax+b)$ ist Stammfunktion von f(ax+b)
+ logarithmische Regel
	+ $\int \frac{f'(x)}{f(x)}=ln|f(x)|+C$

### Integration rationer Funktionen
+ $\int \frac{p(x)}{q(x)}=?$
	+ p, q sind Polynome in x
	+ beides rationale Funktionen
+ Polynomdivision
	+ $p(x)=a(x)q(x)+b(x)$
	+ Grad(b) < Grad(q)
	+ analog zur Division mit Rest
		+ b(x) = Rest < Divisor
	+ ![[Pasted image 20211228115747.png]]
+ Sei q(x) ein  Polynom, gibt es ein 