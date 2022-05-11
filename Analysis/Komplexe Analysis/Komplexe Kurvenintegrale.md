# Komplexe Kurvenintegrale
### Überblic
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
+ Cauchyscher Integralsatz CIS: $\oint f(z)dz=0$, wenn
	+ U sternförmig
	+ f holomorph
	+ C geschlossen in U
+ Beispiel:
	+ ![[Pasted image 20220511142112.png]]
	+ ![[Pasted image 20220511142302.png]]
	+ ![[Pasted image 20220511142346.png]]

[[Komplexe Analysis]]