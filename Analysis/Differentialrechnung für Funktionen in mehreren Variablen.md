# Differentialrechnung für Funktionen in mehreren Variablen
+ $U⊆ℝ^n$ ist offen, wenn $∀\overrightarrow{x}∈U ∃ε>0: B(\overrightarrow{x},ε)⊆U$
	+ $B(\overrightarrow{x},r)={\overrightarrow{x}∈ℝ^n : ||\overrightarrow{x}-\overrightarrow{y}||<r}$

### Stetigkeit für ...
+ Ist $U⊆ℝ^n$ offen, $f:U--> ℝ$
	+ f stetig in U, wenn
		+ Kriterien der [[Stetigkeit]] gelten
			+  auch im mehrdimensionalen
			+ z.B.	$∀ε>0 ∃δ>0 ∀\overrightarrow{x}∈U: |\overrightarrow{x} - \overrightarrow{x_0}| < δ ==> |f(\overrightarrow{x}) - f(\overrightarrow{x_0})| < ε$
	+ f stetig auf U, wenn f in jedem Punkt von U stetig ist

### Grenzwerte für ...
+ $A=\lim{\overrightarrow{x} \to \overrightarrow{x_0}} f(\overrightarrow{x_0})=\lim{x to x_0} \lim{y to y_0} f(x,y)=\lim{y to y_0} \lim{x to x_0} f(x,y)$
	+ Grenzwerte unterschiedlich <==> Grenzwert existiert nicht