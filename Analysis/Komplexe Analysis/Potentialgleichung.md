# Potentialgleichung
### Potentialgleichung
+ $\bigtriangleup u=0$
	+ Lösung dieser Gleichung kommt mit zweiter Funktion v
		+ v erfüllt ebenso Gleichung
		+ v heißt konjugiert harmonische Funktion
		+ v ist mit u über CR-Gleichungen verbunden
			+ bzw. $f(x+iy)=u(x,y)+iv(x,y)$
	+ jede Lösung ergibt quellenfreies Gradientenfeld $grad(u)$
		+ $grad(u)$ senkrecht auf  $grad(v)$ <==> $<grad(u),grad(v)>=0$
		+ Äquipotentiallinien (Niveaulinien) von u und v senkrecht aufeinander
			+ außer $grad(v)=grad(u)=0$
			+ ![[Pasted image 20220516124134.png]]

### Bestimmen von v(x,y) 
+ Gradientenfeld gegeben ==> v(x,y) als Integral
	+ ![[Pasted image 20220516132026.png]]
	+ Integrabilitätsbedingung prüfen ==> wegunabhängig
	+ Beispiel WTF?
		+ ![[Pasted image 20220516132229.png]]
		+ ![[Pasted image 20220516132238.png]]
		+ ![[Pasted image 20220516132258.png]]
		+ ![[Pasted image 20220516132352.png]]

### Randwertaufgabe
+ ![[Pasted image 20220516132432.png]]

### Poissonsche Integralformel
+ sei g: $[0,2\pi]$->ℝ eine Funktion
	+ $u(rcos(φ),rsin(φ))=\frac{1}{2\pi}\int_0^{2\pi}g(t)\frac{1-r^2}{1-2rcos(t-φ)+r^2}dt$
	+ Lösung der Potentialgleichung $\bigtriangleup u=0$ mit
		+ ![[Pasted image 20220525191526.png]]

### Fourier-Reihe
+ sei g: $I$->ℝ
	+ I ... Intervall der Länge 2π
	+ Koeffizienten 
		+ $α_0=\frac{1}{2\pi}\int_I g(t)dt$
		+ $α_n=\frac{1}{\pi}\int_I g(t)cos(nt)dt$
		+ $β_n=\frac{1}{\pi}\int_I g(t)sin(nt)dt$
+ wenn Reihe konvergiert, dann gilt in allen Stetigkeitspunkten von g
	+ $g(φ)=\alpha_0+\sum_{n=1}^\infty(\alpha_n cos(nφ)+\beta_n sin(nφ))$
	+ ![[Pasted image 20220525194148.png]]
+ Beispiele:
	+ ![[Pasted image 20220525193346.png]]
	+ 