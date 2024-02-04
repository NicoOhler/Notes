+ $\int \frac{p(x)}{q(x)}=?$
	+ p, q sind Polynome in x
	+ beides rationale Funktionen
+ Polynomdivision
	+ $p(x)=a(x)q(x)+b(x)$
	+ $\frac {p(x)}{q(x)}=a(x)+\frac{b(x)}{q(x)}$
		+ Grad(r) < Grad(q)
		+ Grad(p) ≥ Grad(q)
	+ analog zur Division mit Rest
		+ b(x) = Rest < Divisor
	+ ![](../../z_images/Pasted%20image%2020211228115747.png)
+ Sei q(x) ein  Polynom, gibt es ein α∈ℂ,  sodass q(α)=0
	+ unter Berücksichtigung von mehrfach auftretender Nullstellen gilt:
		+ $q(x)=(x-α_1)^{k_1}(x-α_2)^{k_2}...(x-α_n)^{k_n}$
		+ $\sum k = n$ - Vielfachheiten
+ Algorithmus:
	+ Polynomdivision
		+ $\frac {p(x)}{q(x)}=a(x)+\frac{b(x)}{q(x)}$
	+ Zerlegung des Nenners in Linearfaktoren
		+ $q(x)=(x-α_1)^{k_1}(x-α_2)^{k_2}...(x-α_n)^{k_n}$
		+ q(x) ist Polynom mt ganzzahligen Koeffizienten ==> jede ganzzahlige Nullstelle ein Teiler von $a_0$
	+ Partialbruchzerlegung
		+ $\frac {r(x)}{q(x)}=\sum_{i=1}^k \sum_{j=1}^{n_i} \frac{A_{ij}}{(x-α_i)^j}$
		+ Bestimmung von $A_{ij}$
	+ Integration der einzelnen Terme
		+ j = 1
			+ α∈ℝ ==> $\int \frac {A}{x-α}dx = A*ln|x-α| + C$
			+ α∈ℂ\\ℝ ==> $\frac {A}{x-α} + \frac {A^{*}}{x-α^{*}}$	==> $\int \frac {ax+b}{x^2+px+q}dx =\frac{a}{2}ln(x^2+px+q)+\frac{2b-ap}{\sqrt{bq-p^2}}arctan(\frac{2x+p}{\sqrt{bq-p^2}})+C$
		+ j > 1
			+ $\int \frac {A}{(x-α)^j}dx =-\frac {A}{(j-1)(x-α)^{j-1}} + C$

[[Integralrechnung]]