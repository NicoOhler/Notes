+ $U⊆ℝ^n$ ist offen, wenn $∀\overrightarrow{x}∈U ∃ε>0: B(\overrightarrow{x},ε)⊆U$
	+ $B(\overrightarrow{x},r)={\overrightarrow{x}∈ℝ^n : ||\overrightarrow{x}-\overrightarrow{y}||<r}$
	+ um jeden Punkt gibt es Platz
		+ Platz = Kugel mit gewissem Radius um Punkt herum

### Stetigkeit für ...
+ Ist $U⊆ℝ^n$ offen, $f:U--> ℝ$
	+ f stetig in U, wenn
		+ Kriterien der [[Stetigkeit]] gelten
			+  auch im mehrdimensionalen
			+ z.B.	$∀ε>0 ∃δ>0 ∀\overrightarrow{x}∈U: |\overrightarrow{x} - \overrightarrow{x_0}| < δ ==> |f(\overrightarrow{x}) - f(\overrightarrow{x_0})| < ε$
	+ f stetig auf U, wenn f in jedem Punkt von U stetig ist
	+ Folgenkriterium
		+ f ist genau dann stetig in $\overrightarrow{x_0}$, wenn für jede Folge $\overrightarrow{x_n}$ mit Grenzwert$\overrightarrow{x_0}$ auch der Limes der Funktionswerte=f($\overrightarrow{x_0}$) gilt

 
### Grenzwerte für ...
+ $A=\lim{\overrightarrow{x} \to \overrightarrow{x_0}} f(\overrightarrow{x_0})=\lim{x \to x_0} \lim{y \to y_0} f(x,y)=\lim{y \to y_0} \lim{x \to x_0} f(x,y)$
	+ Grenzwerte unterschiedlich <==> Grenzwert existiert nicht
	+ Ableitungen der beiden iterierten Grenzwerte können existieren, ohne dass der Grenzwert existiert

### Partielle Ableitung
+ f: $U-->ℝ$ ist differenzierbar in $x_0$, wenn f eine erste Näherung zulässt
	+ $∃l:ℝ-->ℝ$ linear: $f(\overrightarrow{x})=f(\overrightarrow{x_0})+l(\overrightarrow{x}-\overrightarrow{x_0})+||\overrightarrow{x}-\overrightarrow{x_0}||r(\overrightarrow{x})$ mit $\lim_{x \to x_0} r(\overrightarrow{x})=0$
+ Vorgehensweise:
	+ für f(x,y)
	+ $\frac{\partial f}{\partial x}=$ Ableitung von f(x,y) nach x jedoch ist y konstant
		+ bzw. wird angenommen
+ partielle Ableitung kann existieren, obwohl f nicht differenzierbar
	+ sind alle partielle Ableitungen stetig in $x_0$ <==> differenzierbar
+ Richtungsableitung
	+ partielle Ableitung entlang einer Richtung möglich
	+ entspricht Änderungsrate entlang des Vektor n
	+ Richtung ≠ Achsen/Variablen
	+ ![](../../z_images/Pasted%20image%2020220121171531.png)
	+ $\frac{\partial f}{\partial \overrightarrow{n}}=l(\overrightarrow{n})$
		+ gilt wenn f in $x_0$ differenzierbar

### Gradient von f
+ Koordinaten der linearen Abbildung als Vektor
+ ![](../../z_images/Pasted%20image%2020220121172207.png)
+ $\frac{\partial f}{\partial \overrightarrow{n}}=<grad(f)(\overrightarrow{x_0}),\overrightarrow{n}>$
	+ Richtungsableitung = Skalarprodukt von Gradient und Richtungsvektor
	+ $<grad(f)(\overrightarrow{x_0}),\overrightarrow{n}>$
		+ Gradient von f zeigt in Richtung des größten Anstiegs
		+ senkrecht zu Gradient findet keine Änderung statt
			+ <..,..>=0

[[Differentialrechnung]]