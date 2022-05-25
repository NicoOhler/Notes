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
+ sei $g_0$ in $φ_0$ stetig
	+ 