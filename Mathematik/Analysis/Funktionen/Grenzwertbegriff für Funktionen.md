# Grenzwertbegriff für Funktionen
+ f: \[a,b]\\{$x_0$}-->ℝ
+ Wenn ∀ε>0 ∃δ>0 ∀x∈\[a,b]: 0<|x-$x_0$|<δ ==> |f(x)-A|<ε
	+ $A=\lim_{x \to x_0} f(x)$
+ TODO Image missing
	+ $A=\lim_{x \to x_0} f(x)$ <==> f' ist stetig in $x_0$ 
	+ $A=\lim_{x \to x_0} f(x)$ <==> für jede Folge $x_n$ mit $x0=\lim_{n \to \infty} x_n$ gilt
		+ $A=\lim_{n \to \infty} f(x_n)$

### Einseitiger Grenzwert
+ f: \[a,b]\\{$x_0$}-->ℝ
	+ A<sub>-</sub> heißt linksseitiger Grenzwert von f in x<sub>0</sub>
			+ $A_-=\lim{x \to x_0-} f(x)$
			+ wenn ∀ε>0 ∃δ>0 ∀x∈(x<sub>0</sub>-δ,x<sub>-</sub>): |f(x)-A<sub>-</sub>|<ε
		+ A<sub>+</sub> heißt rechtsseitiger Grenzwert von f in x<sub>0</sub>
			+ $A_+=\lim{x \to x_0+} f(x)$
			+ wenn ∀ε>0 ∃δ>0 ∀x∈(x<sub>0</sub>,x<sub>0</sub>+δ): |f(x)-A<sub>+</sub>|<ε
+ $A=\lim_{x \to x_0} f(x)$ existiert, wenn A<sub>+</sub> und A<sub>-</sub> existiern und gleich A

### Uneigentlicher Grenzwert
+ $\lim{x \to x_0+} f(x)=+\infty$ <==> ∀M>0 ∃δ>0 ∀x∈\[a,b]: 0<|x-$x_0$|<δ ==> |f(x)-A|>M
+ $\lim{x \to x_0-} f(x)=-\infty$ <==> ∀M>0 ∃δ>0 ∀x∈\[a,b]: 0<|x-$x_0$|<δ ==> |f(x)-A|< -M
+ $\lim{x \to +\infty} f(x)=A$ <==> ∀ε>0 ∃M ∀x>M: |f(x)-A|< ε
+ $\lim{x \to -\infty} f(x)=A$ <==> ∀ε>0 ∃M ∀x< -M: |f(x)-A|< ε

[[Funktionen]]