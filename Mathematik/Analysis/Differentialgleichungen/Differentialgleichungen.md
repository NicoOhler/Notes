### Definition
+ Sei F: $ℝ^{n+2}$-->ℝ
	+ $F(x,y,y',...,y^{(n)})$ ist eine Differentialgleichung
	+ x unabhängig
	+ y abhängig
	+ Beispiel:
		+ $xy'+y^2+y''=0$
		+ DGL 2. Ordnung
		+ gesucht y=y(x)

### Herkömmliche Methode
+ ![](../../z_images/Pasted%20image%2020220404173350.png)
+ nur wenn x und y auf verschiedene Seiten bringen möglich ist
+ unendlich viele Lösungen

### Anfangswertproblem AWP
+ Anfangswertproblem
	+ GLG der Form y'=f(x,y) mit $y(a)=y_0$
+ Satz von Picard-Lindelöf
	+ f: $[a,b]×[y_0-b,y_0+b]$--> ℝ stetig und gilt für ein L≥0
		+ $∀x∈[a,b]∀y_1, y_2∈[y_0-b,y_0+b]: |f(x,y_1)-f(x,y_2)|≤|y_1-y_2|$
		+ sei M so, dass $∀x,y∈ℝ:|f(x,y)≤M|$
	+ dann hat das AWP genau eine Lösung y=y(x) auf das Intervall $[a,m]$
		+ $m=min(b,a+\frac{b}{M})$
		+ ![](../../z_images/Pasted%20image%2020220404174640.png)
+ Beispiele: keine Eindeutigkeit
	+ ![](../../z_images/Pasted%20image%2020220412171519.png)
	+ für y=0 gibt es ∞ Lösungen

### Euler-Verfahren
+ Annäherung der Lösung durch Polygonzug
+ Vorgehensweise
	+ Schrittweite h wird definiert
	+ Steigung $k_i$ in Punkt wird bestimmt
	+ Gerade (Steigung $k_i$, Länge h) bis zu nächstem Punkt
	+ dies wird x mal wiederholt
+ ![](../../z_images/Pasted%20image%2020220412172308.png)

[[Mehrdimensionale Differentialrechnung]]
