+ $R=[a_1,b_1]x[a_2,b_2]x[a_3,b_3]$
+ $\int\underset{R}\int\int f(x,y,z) dy dy dz =\int_{x=a_1}^{b_1}(\int_{x=a_2}^{b_2}(\int_{x=a_3}^{b_3}f(x,y,z)dz)dy)dx$
	+ andere Reihenfolgen auch möglich

### Normalbereich im R^3
+ $N={(x,y,z)∈ℝ^3|(x,y)∈M, g(x,y)≤z≤h(x,y)}$
+ $vol(N)=\int^d_{y=c}(\int^{φ(y)}_{x=ψ(y)}(\int_{z=g(x,y)}^{h(x,y)}dz)dx)dy$
+ Beispiel
	+ ![](../../../z_images/Pasted%20image%2020220314130508.png)
	+ ![](../../../z_images/Pasted%20image%2020220314131029.png)

### Substitutionsregel (Transformationsformel)
+ $T: B$-->$ℝ^3$
+ T differenzierbar und injektiv
+ $\int\underset{T(B)}{\int}\int f(x,y,z)dx dy dz=\int\underset{B}{\int}\int f*T(u,v,w)*|det \frac{\partial(x,y,z)}{\partial(u,v,w)}|du dv dw$
+ Volumensumrechnungsfaktor - JACOBI-Determinante
	+ x,y,z beliebig vertauschbar
+ Beispiel: dreidimensionale Polarkoordinaten
	+ x ==> rsin(ψ)cos(φ)
	+ y ==> rsin(ψ)sin(φ) 
	+ z ==> rcos(ψ)	
	+ Bedingungen
		+ r≥0
		+ 0≤ψ≤π
		+ 0≤φ≤2π
	+ ![](../../../z_images/Pasted%20image%2020220314132808.png)
	+ Beispiel: Polarkoordinaten bei Kugel
		+ ![](../../../z_images/Pasted%20image%2020220314143710.png)
+ Zylinderkoordinaten
	+ x ==> rcos(φ)
	+ y ==> rsin(φ) 
	+ z ==> z
	+ Volumenselement
		+ $dxdydz=rdrdφdz$
	+ Beispiel
		+  ![](../../../z_images/Pasted%20image%2020220314145659.png)
		+  ![](../../../z_images/Pasted%20image%2020220314145710.png)
	
	[[Mehrdimensionale Integralrechnung]]