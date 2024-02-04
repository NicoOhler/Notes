### Substitution
+ Variablen können substituiert werden
	+ ![](Pasted%20image%2020220411113248.png)
	+ y wird mit f(u,v) substituiert

### Semantische Äquivalenz
+ gegeben ist Σ-Modell $M=(Ä,ω)=(A,Σ,ω)$ für $F_{V,Σ}$
	+  x aus V
	+  a aus A
+  $M[x/a]$ ist Modell mit Belegung $ω_x^a(y):=a$, falls y=x ansonsten ω(y)
	+  $M^a_x=(Ä,ω_x^a)=(A,Σ,ω_x^a)$
+  Erfüllungsrelation für Formeln in $F_{V,Σ}$
	+  für Primformeln gilt
		+  M|=$(s=t)$, falls $s^M=t^M$
		+  M|=$R(t_1,...,t_n)$, falls $R^M(t_1,...,t_n)$
	+  für P, Q Formeln gilt
		+  $M|=¬P$, falls $M|=P$ nicht gilt
		+ ![](Pasted%20image%2020220411114800.png)
+  P und Q sind semantisch äquivalent, falls
	+ ∀M: gilt M|=Q <==> M|=P
	+ P<==>Q
+ Umformungsregeln:
	+ ![](Pasted%20image%2020220411142454.png)
+ P ist in pränexer Normalform, wenn
	+ $P=Q_1x_1Q_2x_2...Q_kx_kR$
		+ Q...Quantoren
		+ x...Variablen
		+ R...quantorenfreie Formel aus $F_{V,Σ}$
	+ Jede Formel besitzt äquivalente pränexe NF
		+ ![](Pasted%20image%2020220411143028.png)


[[First Order Logic]]