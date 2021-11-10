# Stetigkeit
+ Graph kann ohne Definitionslücken nahtlos gezeichnet werden

### Grenzwertkriterium
+ Sei f: I --> ℝ eine reelle Funktion:
+ f ist stetig in x<sub>0</sub>∈I, wenn
	+ für jede Folge x<sub>n</sub> aus I mit  $x_0 = \lim x_n$ auch $f(x_0) = \lim f(x_n) = f(\lim x_n)$ gilt.
+ f ist stetig auf I, wenn f stetig in jedem Punkt x∈I

### ε-δ-Kriterium
+ Sei f: I --> ℝ eine reelle Funktion:
+  f ist stetig in x<sub>0</sub>∈I, wenn
	+  ∀ε>0 ∃δ>0 ∀x∈I: |x - x<sub>0</sub>| < δ ==> |f(x) - f(x<sub>0</sub>)| < ε
 ![[Pasted image 20211110154416.png]]
+  Vorgehensweise
	+  |f(x) - f(x<sub>0</sub>)| ersetzen mit Formel hinter Funktion
	+  umformen/abschätzen sodass |x - x<sub>0</sub>| separater Term ist
	+  Ausdruck in der Form λ \* |x - x<sub>0</sub>| < ε ensteht
	+  ==> |x - x<sub>0</sub>| < λε = δ
	+  Somit gilt wenn |x - x<sub>0</sub>| < λε, dann gilt |f(x) - f(x<sub>0</sub>)| < ε


### Spezielle Funktionen
+ Polynomfunktionen sind immer stetig
+ p, q sind Polynome ==> $r(x) = \frac{p(x)}{q(x)}$ ist eine rationale Funktion
	+ r ist stetig auf Definitionsbereich D = {x∈ℝ | q(x) ≠ 0}
	+ rationale Funktionen sind stetig, wenn Nenner ≠ 0