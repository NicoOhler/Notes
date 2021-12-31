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