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
+ Cauchy-Abschätzung
	+ Maximumprinzip
		+ $|a_n|≤$ Maximum am Rand des Kreises
		+ ![[Pasted image 20220516101649.png]]
	+ Satz von Liouville
		+ Sei f eine ganze Funktion und beschränkt ==> f ist konstant
		+ ![[Pasted image 20220516102124.png]]
	+ Fundamentalsatz der Algebra
		+ Polynom p(z) mit Grad n≥1
		+ $∃z_0: p(z_0)=0$
		+ jedes Polynom hat eine komplexe Nullstelle
		+ Beweis
			+ ![[Pasted image 20220516102832.png]]
+ Nullstellen holomorpher Funktionen
	+ $N_f=\{z∈U|f(z)=0\}$ Nullstellenmenge
	+ $N_f$ entweder ganz U oder kein Häufungspunkt laut [[Satz von Bolzano-Weierstraß]]]
	+ ![[Pasted image 20220516105419.png]]
+ Seien f,g holomorph auf U, C eine Kurve aus U
	+ $∀z∈ℂ:f(z)=g(z)$ ==> $f(z)=g(z):∀z∈U$
	+ Definitionen der elementaren Funktionen (exp,log,...) für $z∈ℂ$ sind die einzig möglichen Fortsetzungen der reellen elementaren Funktionen
+ 

[[Komplexe Analysis]]