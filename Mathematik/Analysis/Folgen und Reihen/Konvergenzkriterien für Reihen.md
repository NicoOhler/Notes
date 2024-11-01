### Majoranten und Minorantenkriterium
+ Seien a<sub>n</sub> und b<sub>n</sub> mit positiven Gliedern und ∀n: a<sub>n</sub> ≤ b<sub>n</sub>
	+ Majorantenkriterium: ist b konvergent, muss auch a konvergieren
		+ b ist die konvergente Majorante von a
	+ Minorantenkriterium: ist a divergent, muss auch b divergieren
		+ a ist die divergente Minorante von b
+ Variation:
	+ Ist Reihe Σ b<sub>n</sub> konvergent, b<sub>n</sub> ≥ 0 und lim a<sub>n</sub>/b<sub>n</sub> ≥ 0 ==> Reihe Σ a<sub>n</sub> konvergent
	+  Ist Reihe Σ b<sub>n</sub> divergent, b<sub>n</sub> ≥ 0 und lim a<sub>n</sub>/b<sub>n</sub> <0  ==> Reihe Σ a<sub>n</sub> divergent

### Quotientenkriterium/test
+ Sei  Σ a<sub>n</sub> eine Reihe mit positiven Gliedern gilt: 
	+ lim sup a<sub>n+1</sub>/a<sub>n</sub> < 1  ==> konvergent
	+ lim inf a<sub>n+1</sub>/a<sub>n</sub> > 1 ==> divergent
	+ wenn q = lim a<sub>n+1</sub>/a<sub>n</sub> existiert, dann
		+ $q < 1$ ==> konvergent
		+ $q > 1$ ==> divergent
		+ $q = 1$ ==> keine Aussage

### Wurzelkriterium/test
+ Sei  Σ a<sub>n</sub> eine Reihe mit positiven Gliedern gilt für $\lim sup \sqrt[n]{a_n} = q$
	+ $q > 1$ ==>  divergent
		+ weil $\sqrt[n]{a_n} ≥ 1$ ==> ${a_n ≥ 1}$ für ∞ Glieder
	+ $q < 1$ ==> konvergent
		+ weil ∃N ∀n ≥ N ==> $\sqrt[n]{a_n} ≥ 1$ ==>  $\sqrt[n]{a_n} ≤ \frac{1+q}{2} < 1$ ==> ${a_n ≤ (\frac{1+q}{2})^n}$
		+ wenn Grenzwert existiert ==> Grenzwert = lim sup
	+ $q = 1$ ==>  keine Aussage

### Leibnizkriterium
+ Sei a<sub>n</sub> eine monoton fallende Nullfolge ==> konvergiert $\sum_{n=1}^{∞} (-1)^n a_n$

### Cauchy-Kriterium für Reihen
+ [[Cauchy-Kriterium]]

[[Reihen und Folgen]]



