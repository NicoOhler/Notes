# Satz von Taylor
+ Taylor Polynom P(x,...,y) mit mehreren Variablen
	+ nähert f(x,...,y) für die ersten Ableitungen gut an
	+ $a_{n_1 n_2}=\frac{1}{n_1!n_2!}\frac{\partial^{n_1 + n_2} f}{\partial x^{n_1}\partial y^{n_2}}(0,0)$
	+ ![[Pasted image 20220301085740.png]]
+ Multinomialkoeffizient
	+ $\binom{n}{n_1,...,n_p} = \frac{n!}{n_1!...n_p!}$
	+ Parameteranzahl in zweiter Zeile = n
	+ Binomialkoeffizient $\binom{n}{k}=\binom{n}{k,n-k}$
+ Multinomialer Lehrsatz
	+ ![[Pasted image 20220301090151.png]]
	+ ![[Pasted image 20220301090413.png]]
	+ 
### Satz von Taylor
+ $U⊆ℝ^p$ offen
+ liegen $x_0$ und $x_0 + h$ samt Verbindungsstrecke in U
+ ==> $f(x_0 + h)=\sum^n_{v=0} (\frac{1}{v!}(h_1\frac{\partial}{\partial x_1} + ... + h_p\frac{\partial}{\partial x_p})f|_{x_0}) + \frac{1}{(n+1)!}(h_1\frac{\partial}{\partial x_1} + ... + h_p\frac{\partial}{\partial x_p})f|_{x_0+θh}$
	+ 1. Term Taylor-Polynom
	+ 2. Term Rest

### Extremwerte für Funktionen $ℝ^2$-->$ℝ$
+ im eindimensionalen
	+ Extremstelle, wenn f'(x)=0
	+ Min/Max, wen f''(x)>/< 0
+ mehrdimensionalen
	+ Extremstelle, wenn Gradient von f(x)= 0
	+ Max, wenn Hessematrix im Punkt negativ definit
	+ Min, wenn Hessematrix im Punkt positiv definit
	+ kein Extremum, wenn indefinit
		+ sondern Sattelpunkt
	+ semidefinit ==> keine Aussagekraft
	+ Definitheit
		+ quadratische Form $Q_A(x)$
			+ ![[Pasted image 20220301092217.png]]
		+ positiv definit <==> $Q_A(x)>0 ∀x≠0$
		+ negativ definit <==> $Q_A(x)<0 ∀x≠0$
		+ positiv semidefinit <==> $Q_A(x)≥0 ∀x≠0$
		+ negativ semidefinit <==> $Q_A(x)≤0 ∀x≠0$
		+ ansonsten indefinit
+ Rechnerische Bestimmung von Extrema im mehrdimensionalen
	+ ![[Pasted image 20220301092715.png]]
	+ Vorzeichen von Unterdeterminanten
		+ positiv def. <==> positives Vorzeichen
		+ negativ def. <==> alternierendes Vorzeichen
		+ ![[Pasted image 20220301092945.png]]
	+ Aussagekraft der $Δ_j$
		+ eins der Δ = 0 ==> keine Aussagekraft
		+ alle Δ > 0 ==> Min
		+ ungerade Δ < 0, gerade Δ > 0 ==> Max
		+ ein gerades Δ < 0 ==> Sattelpunkt

[[Mehrdimensionale Differentialrechnung]]




