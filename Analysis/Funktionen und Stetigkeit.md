# Funktionen und Stetigkeit
+ Eine Abbildung f: I --> ℝ (I⊆ℝ, zumeist ein Intervall) heißt reelle Funktion
	+ injektiv
		+ wenn für jedes x: f(x) eindeutig ist
	+ surjektiv
		+ jedes Element in Zielmenge mindestens einmal von f(x) abgebildet
	+ bijektiv
		+ injektiv und surjektiv
		+ jedes Element in Zielmenge genau einmal von f(x) abgebildet
+ Graph von f
	+ {(x,y)∈I×B | y=f(x)}
	+ x und y=f(x) als Achsen des Graphen
+ Beispiel
	+  f: ℝ --> ℝ, x ==> x² + 1
	+ Kurzform: f(x) = x² + 1

### Eigenschaften von Funktionen
+ Monotonie
	+ monoton wachsend, wenn jedes f(x<sub>n</sub>) ≤ f(x<sub>n+1</sub>)
		+ streng, wenn f(x<sub>n</sub>) < f(x<sub>n+1</sub>)
	+ monoton fallend, wenn jedes f(x<sub>n</sub>) ≥ f(x<sub>n+1</sub>)
		+ streng, wenn f(x<sub>n</sub>) > f(x<sub>n+1</sub>)
	+ strenge Monotonie impliziert Injektivität
+ Gerade Funktion
	+ symmetrisch zur y-Achse
	+ f(x) = f(-x)
+ Gerade Funktion
	+ symmetrisch zum Ursprung
	+ f(-x) = -f(x)

### Stetigkeit
+ Sei f: I --> ℝ eine reelle Funktion:
+ f ist stetig in x<sub>0</sub>∈I, wenn
	+ für jede Folge x<sub>n</sub> aus I mit  $x_0 = \lim x_n$ auch $f(x_0) = \lim f(x_n) = f(\lim x_n)$ gilt.
+ f ist stetig auf I, wenn f stetig in jedem Punkt x∈I
+ Graph kann ohne Definitionslücken nahtlos gezeichnet werden

### Spezielle Funktionen
+ Polynomfunktionen sind immer stetig
+ p, q sind Polynome ==> $r(x) = \frac{p(x)}{q(x)}$ ist eine rationale Funktion
	+ r ist stetig auf Definitionsbereich D = {x∈ℝ | q(x) ≠ 0}
	+ rationale Funktionen sind stetig, wenn Nenner ≠ 0
