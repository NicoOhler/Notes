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
	+ $\frac {p(x)}{q(x)}=a(x)+\frac{r(x)}{q(x)}$
		+ Grad(r) < Grad(q)
		+ Grad(p) ≥ Grad(q)
	+ analog zur Division mit Rest
		+ r(x) = Rest < Divisor
	+ ![[Pasted image 20211228115747.png]]
+ Sei q(x) ein  Polynom, gibt es ein α∈ℂ,  sodass q(α)=0
	+ unter Berücksichtigung von mehrfach auftretender Nullstellen gilt:
		+ $q(x)=(x-α_1)^{k_1}(x-α_2)^{k_2}...(x-α_n)^{k_n}$
		+ $\sum k = n$ - Vielfachheiten
+ Algorithmus:
	+ Polynomdivision
		+ $\frac {p(x)}{q(x)}=a(x)+\frac{r(x)}{q(x)}$
	+ Zerlegung des Nenners in Linearfaktoren
		+ $q(x)=(x-α_1)^{k_1}(x-α_2)^{k_2}...(x-α_n)^{k_n}$
	+ Partialbruchzerlegung
		+ $\frac {r(x)}{q(x)}=\sum_{i=1}^k \sum_{j=1}^{n_i} \frac{A_{ij}}{(x-α_i)^j}$
		+ Bestimmung von $A_{ij}$
	+ Integration der einzelnen Terme
		+ j = 1
			+ α∈ℝ ==> $\int \frac {A}{x-α}dx = A*ln|x-α| + C$
			+ α∈ℂ\\ℝ ==> $\frac {A}{x-α} + \frac {A^{*}}{x-α^{*}}$	==> $\int \frac {ax+b}{x^2+px+q}dx =\frac{a}{2}ln(x^2+px+q)+\frac{2b-ap}{\sqrt{bq-p^2}}arctan(\frac{2x+p}{\sqrt{bq-p^2}})+C$
		+ j > 1
			+ $\int \frac {A}{(x-α)^j}dx =-\frac {A}{(j-1)(x-α)^{j-1}} + C$