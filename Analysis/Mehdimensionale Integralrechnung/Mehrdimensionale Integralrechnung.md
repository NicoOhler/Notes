# Mehrdimensionale Integralrechnung
+ R=$[a,b]x[c,d]$
+ f: R-->ℝ
+ f ist Riemann-Darboux-integrierbar auf R, wenn
	+ ![[Pasted image 20220302150614.png]]
+ Integral bzw. Volumen von f
	+ $\int^d_c (\int^b_a f(x,y)dx)dy$
	+ Reihenfolge vertauschbar
	
### Substitutionsregel (Transformationsformel)
+ differenzierbar und injektiv
+ $\int\underset{T(B)}{\int} f(x,y)dxdy=\int\underset{B}{\int} f*T(u,v)*|det \frac{\partial(x,y)}{\partial(u,v)}|du dv$
+ Volumensumrechnungsfaktor - JACOBI-Determinante