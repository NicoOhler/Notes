# Komplexe Kurvenintegrale
### Überblick
+ sei eine Kurve C \[a,b]-->U stückweise differenzierbar
	+ t-->z(t)
	+ f holomorph auf U
+ $\int_Cf(z)dz=\int_a^bf(z(t))z'(t)dt$
	+ Substitution mit $z=z(t)$, $dz=z'(t)dt$
	+ unabhängig von Parametrisierung
+ Zerlegung in Real- und Imaginärteil
	+ $\int_Cf(z)dz=\int_C(u(x,y)+i(v(x,y)))*(dx+idy)=$
	+ $\int_Cu(x,y)dx-v(x,y)dy + i\int_Cv(x,y)dy+u(x,y)dy$
+ wegunabhängig, wenn
	+ Definitionsbereich von f sternförming
	+ $\oint f(z)dz=0$
		+ wegen Cauchy-Riemann-Gleichungen
		+ ![[Pasted image 20220511141142.png]]
		
### Cauchyscher Integralsatz
+ $\oint f(z)dz=0$, wenn
	+ U sternförmig
	+ f holomorph
	+ C geschlossen in U
+ Beispiele:
	+ ![[Pasted image 20220511142112.png]]
	+ ![[Pasted image 20220511142302.png]]
	+ ![[Pasted image 20220511142346.png]]
+ Umläufe zählen
	+ ![[Pasted image 20220511150220.png]]
	+ ![[Pasted image 20220511150743.png]]
	+ ![[Pasted image 20220511151006.png]]
	+ ![[Pasted image 20220511151330.png]]
+ Cauchysche Integralformel
	+ $f(z_0)*Ind_C(z_0)=\frac{1}{2\pi}\oint_C\frac{f(z)}{z-z_0}dz$
+ Erkenntnisse
	+ ![[Pasted image 20220511151750.png]]
	+ ![[Pasted image 20220511151805.png]]
	+ f lässt sich als Potenzreihe mit Konvergenzradius ≥R darstellen
	+ f beliebig oft differenzierbar
	+ $a_n=\frac{f^{(n)}(z_0)}{n!}=\frac{1}{2\pi}\oint_{|ζ-z_0| } \frac{f(ζ)}{(ζ-z_0)^{n+1}}dζ$
		+ $=\frac{1}{2\pi}\oint_C \frac{f(ζ)}{(ζ-z_0)^{n+1}}dζ$
		+ C eine Kurve in U mit $Ind_C(z_0)=1$

[[Komplexe Analysis]]