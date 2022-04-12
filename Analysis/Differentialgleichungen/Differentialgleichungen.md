# Differentialgleichungen
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
+ ![[Pasted image 20220404173350.png]]
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
		+ ![[Pasted image 20220404174640.png]]
+ Beispiele: keine Eindeutigkeit
	+ ![[Pasted image 20220412171519.png]]
	+ für y=0 gibt es ∞ Lösungen

### Euler-Verfahren
+ Annäherung 

[[Mehrdimensionale Differentialrechnung]]
