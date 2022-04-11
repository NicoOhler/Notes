# Substitutionen in Prädikatenlogik
### Substitution
+ Variablen können substituiert werden
	+ ![[Pasted image 20220411113248.png]]
	+ y wird mit f(u,v) substituiert

### Semantische Äquivalenz
+ gegeben ist Σ-Modell $M=(Ä,ω)=(A,Σ,ω)$ für $F_{V,Σ}$
	+  x aus V
	+  a aus A
+  $M[x/a]$ ist Modell mit Belegung $ω_x^a(y):=a$, falls y=x ansonsten ω(y)
	+  $M^a_x=(Ä,ω_x^a)=(A,Σ,ω_x^a)$
+  Erfüllungsrelation für Formeln in $F_{V,Σ}$
	+  für Primformeln gilt
		+  M ==> $(s=t)$, falls $s^M=t^M$
		+  M ==> $R(t_1,...,t_n)$, falls $R^M(t_1,...,t_n)$
	+  für P, Q Formeln gilt
		+  M==> $¬P$, falls M==>P nicht gilt
		+ ![[Pasted image 20220411114800.png]]
+  P und Q sind semantisch äquivalent, falls
	+ ∀M: gilt M==>Q <==> ==>P


[[First Order Logic]]