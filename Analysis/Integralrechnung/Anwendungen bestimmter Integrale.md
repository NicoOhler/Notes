# Anwendungen bestimmter Integrale
###  Riemannsumme
+ $f:[a,b]-->ℝ$ Riemann-integrierbar
+  $\sum_{i=0}^{n-1}f(ξ_i)(x_{i+1}-x_i)=R(f,Z,E)$
	+  $ξ_i∈[x_i.x_{i+1}]$ 
	+  Z - Zerlegungen
	+  E = Menge aller Stützstellen(ξ)
	
###  Bogenlänge
+ $f:[a,b]-->ℝ$
+ Kurve gegeben durch y=f(x) ist rektifizierbar, wenn 
	+ die größte Bogenlänge L der Zerlegungen Z endlich
	+ $sup L(f,Z)<\infty$
	+ $L(f,Z)=f'(ξ_i)=R(\sqrt{1+(f')^2},Z,E)$
+ $L=\int^b_a \sqrt{1+(f'(x))^2}dx$
+ ![[Pasted image 20211231171822.png]]

### Fläche eines von Kurve begrenzten Sektor
+ VO#36 1:25
+ Leibnizsche Sektorformel
	+ $A_{Sektor}=\frac{1}{2}\int_a^b (x(t)y'(t)-x'(t)y(t))dt$
	+ ![[Pasted image 20211231172742.png]]

### Bogenlänge von Kurven in Parameterdarstellung
+ $C: \overrightarrow{x}=(x(t),y(t))$
	+ $t∈[a,b]$
	+ Länge von C gesucht
	+ $L=\int^b_a\sqrt{x'(t)^2+y'(t)^2}$	+ $L=\int^b_a||\overrightarrow{x'}||$

### Volumen von Drehkörpern
+ $V=π\int^b_a f(x)^2dx$