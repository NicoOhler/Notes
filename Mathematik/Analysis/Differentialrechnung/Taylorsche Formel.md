+ Näherung $f(x)=f(x_0)+f'(x_0)(x-x_0)+r(x)(x-x_0)$
+ gesucht sind höhere Näherungen
	+ Sei f: (a,b)-->ℝ diffbar
	+ wenn f': (a,b)-->ℝ auch diffbar
	+ dann heißt $f''=(f')'$ die zweite Aleitung
	+ f heißt n mal diffbar, wenn $f^n=(f^{n-1})'$ existiert
+ n-te Taylor-Polynom
	+ Sei f: (a,b)-->ℝ  n mal diffbar x<sub>0</sub>∈(a,b)
	+ dann heißt $T_n(f,x_0,x)=\sum^n_{k=0} \frac{f^k(x_0)}{k!}(x-x_0)^k$ das n-te Taylor-Polynom von f an der Stelle x<sub>0</sub>
+ $T_n(f,x_0,x_0)=f(x_0)$
+ $T_n'(f,x_0,x_0)=f'(x_0)$
+  $T_n(f,x_0,x_0)$ ist Polynom von Grad ≤n, das bei  x<sub>0</sub> mit f in den ersten n Ableitungen übereinstimmt
	+ $T_n^l(f,x_0,x_0)=f^l(x_0)$

### Taylor-Lagrauge
+ Sei f: (a,b) --> ℝ (n+1)-mal diffbar, $x,x_0∈(a,b)$
	+ Dann gibt es ein t zwischen x und $x_0$, sodass
		+ $f(x)=T_n(f,x,x_0) + \frac{f^{n+1}(t)}{(n+1)!}(x-x_0)^{n+1}$
		+ Restglied von Lagrauge
		+ wiederholbar für n Ableitungen - alle Glieder des Taylor-Polynom

[[Differentialrechnung]]