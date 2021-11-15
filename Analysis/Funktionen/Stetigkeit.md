# Stetigkeit
+ Graph kann ohne Definitionslücken nahtlos gezeichnet werden
+ Nullstellensatz	
	+ Sei $f: [a;b]-->ℝ$ stetig auf [a;b] und $f(a)*f(b) < 0$
		+ ∃ x∈[a;b]\: f(x) = 0

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
	+  Ausdruck in der Form λ \* |x - x<sub>0</sub>| < ε ensteht ==> |x - x<sub>0</sub>| < λε = δ
	+  Wenn |x - x<sub>0</sub>| < λε, dann gilt |f(x) - f(x<sub>0</sub>)| < ε

### Spezielle Funktionen
+ Polynomfunktionen sind immer stetig
+ p, q sind Polynome ==> $r(x) = \frac{p(x)}{q(x)}$ ist eine rationale Funktion
	+ r ist stetig auf Definitionsbereich D = {x∈ℝ | q(x) ≠ 0}
	+ rationale Funktionen sind stetig, wenn Nenner ≠ 0

### Eigenschaften stetiger Funktionen
+ Sei I ein abgeschlossenes, beschränktes Intervall und f: I-->ℝ stetig auf I
	+ ∃ M>0 ==> ∀x∈I: |f(x)| ≤ M ==> f ist beschränkt
	+ ∃ x<sub>min</sub>,x<sub>max</sub>∈I ∀x∈I: |f(x<sub>min</sub>)| ≤ f(x)  |f(x<sub>max</sub>)|
		+ es gibt kleinste, obere und größte, untere Schranke
	+ nicht abgeschlossen: $f: ]0;1]-->ℝ, f(x)=\frac{1}{x}$
		+ $x_max = 1$
		+ $x_min$ existiert nicht!
			+ $f(0)=\frac{1}{0}$ ==> Error

[[Funktionen]] [[Supremum und Infimum]]