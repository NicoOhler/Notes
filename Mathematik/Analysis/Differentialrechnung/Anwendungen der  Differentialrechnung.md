+ f: I-->ℝ, $x_0∈I$
	+  lokale Extremstelle
		+ $x_0$ lokales Maxiumum
			+ ∃δ>0: f(x)≤f(x<sub>0</sub>) ∀x∈(x<sub>0</sub> - δ, x<sub>0</sub> + δ) <==> x<sub>0</sub> ist größtes Element in der Umgebung +/-δ
		+  $x_0$ lokales Maxiumum
			+ ∃δ>0: f(x)≥f(x<sub>0</sub>) ∀x∈(x<sub>0</sub> - δ, x<sub>0</sub> + δ) <==>  x<sub>0</sub> ist kleinstes Element in der Umgebung +/-δ
	+ globale Extremstelle
		+  $x_0$ globales Maxiumum
			+ f(x)≤f(x<sub>0</sub>) ∀x∈I <==> x<sub>0</sub> ist größtes Element in I
		+  $x_0$ globales Maxiumum
			+ f(x)≥f(x<sub>0</sub>) ∀x∈I <==> x<sub>0</sub> ist kleinstes Element in I
	+ x<sub>0</sub> ist lokale Extremstelle ==> f'(x<sub>0</sub>)=0
		+ f'(x<sub>0</sub>) = 0 = Steigung ==> Hochpunkt/Tiefpunkt
		+ Umkehrschluss gilt nicht
		+ Gegenbeispiel: $f(x)=x^3$
		
### Satz von Rolle
+ f: [a,b]-->ℝ differenzierbar
+ f(a)=f(b) ==> ∃x<sub>0</sub>∈(a, b): f'(x<sub>0</sub>) = 0
+ Im Intervall muss mindestens ein lokales Maximum/Minimum existieren
+ Wenn f'(x) = 0 ∀x[a,b] ==> f ist konstant

### Mittelwertsatz der Differentialrechnung - MWS
+ Verallgemeinerung von Satz von Rolle
+ f: [a,b]-->ℝ differenzierbar
+ ∃x<sub>0</sub>∈(a, b): f'(x<sub>0</sub>) = $\frac{f(b)-f(a)}{b-a}$
+  $\frac{f(b)-f(a)}{b-a}$ entspricht der Steigung einer Gerade zwischen a und b
	+  es existiert mindestens eine Tangente, welche parallel zu dieser Gerade ist.

### Verallgemeinerung MWS
+ f,g: [a,b]-->ℝ differenzierbar
+ ∀x∈(a, b): g'(x) ≠ 0
	+ ==> ∃x<sub>0</sub>∈(a, b): $\frac{f(b)-f(a)}{g(b)-g(a)} = \frac{f'(x_0))}{g'(x_0)}$

[[Differentialrechnung]]