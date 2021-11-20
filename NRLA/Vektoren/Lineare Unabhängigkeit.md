# Lineare Unabhängigkeit
+ Sei $\overrightarrow{v_1}, ..., \overrightarrow{v_n}$∈V und $λ_1,...,λ_n$∈ℝ
	+ $λ_1\overrightarrow{v_1}, ..., λ_n\overrightarrow{v_n}$ ist Linearkombination von $\overrightarrow{v_1}, ..., \overrightarrow{v_n}$
+ triviale Linearkombination ==> alle λ = 0
	+ nichttriviale Linearkombination ==> mindestens ein λ ≠ 0

### Span
+ Sei U = {$\overrightarrow{v_1}, ..., \overrightarrow{v_n}$}⊆V
+ Span(U) = {$λ_1\overrightarrow{v_1}, ..., λ_n\overrightarrow{v_n} | λ_1,...,λ_n∈ℝ$}
	+ Menge aller Linearkombinationen von U
	+ der von den Vektoren ans U aufgespannte Raum
+ Span(U) ist Unterraum von V
+ Span({$e_1, e_2, e_3$}) = ℝ

### Lineare Unabhängigkeit
+ $\overrightarrow{v_1}, ..., \overrightarrow{v_n}$∈V 
	+ $\overrightarrow{v_1}, ..., \overrightarrow{v_n}$ sind linear abhängig, wenn es eine nichttriviale Linearkombination $λ_1\overrightarrow{v_1}, ..., λ_n\overrightarrow{v_n} = \overrightarrow{0}$ gibt
	+  $\overrightarrow{v_1}, ..., \overrightarrow{v_n}$ sind linear unabhängig, wenn es NUR  triviale Linearkombinationen $λ_1\overrightarrow{v_1}, ..., λ_n\overrightarrow{v_n} = \overrightarrow{0}$ gibt
+ Gleichsetzen mit 0 und Finden von Lösungen
	+ $A = (\overrightarrow{v_1}, ..., \overrightarrow{v_n})$
	+ $A * e_j = \overrightarrow{v_j}$ ==> $A * (λ_1, ..., λ_n)^T = (\overrightarrow{0})$
		+ eindeutige Lösung ==> lineare Unabhängigkeit
		+ ∞ Lösung ==> lineare Abhängigkeit
+ Lineare Abhängigkeit
	+ mindestens ein Vektor $v_j$ ist Linearkombination der übrigen
+ Menge U ist linear unabhängig, wenn je endlich viele Vektoren aus U linear unabhängig
	+ sonst linear abhängig

[[Untervektorräume]]