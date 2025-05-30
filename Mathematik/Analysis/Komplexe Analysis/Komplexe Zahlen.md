+ ℂ = { z = x + iy | x,y∈ℝ}
	+ x - Realteil - Re(z)
	+ y - Imaginärteil - Im(z)
	+ i - imaginäre Einheit
+  $i = \sqrt[2]{-1}$
+ $i^2 = -1$

### Grundrechenarten
+ (x<sub>1</sub> + iy<sub>1</sub>) +/- (x<sub>2</sub> + iy<sub>2</sub>) = (x<sub>1</sub> + x<sub>2</sub>) + i(y<sub>1</sub> + y<sub>2</sub>)
+  (x<sub>1</sub> + iy<sub>1</sub>)\*(x<sub>2</sub> + iy<sub>2</sub>) = x<sub>1</sub>x<sub>2</sub> + iy<sub>1</sub>x<sub>2</sub> + ix<sub>1</sub>y<sub>2</sub> + i<sup>2</sup>y<sub>1</sub>y<sub>2</sub>= (x<sub>1</sub>x<sub>2</sub> - y<sub>1</sub>y<sub>2</sub>) + i(x<sub>1</sub>y<sub>2</sub> + x<sub>2</sub>y<sub>1</sub>)
+  $\frac{1}{x+iy} = \frac{x-iy}{x^2 + y^2} = \frac{x}{x^2 + y^2} - i\frac{y}{x^2 + y^2}$ für  $x^2 + y^2 ≠ 0$

### Ordnungen/Vergleiche
+ keine Ordung auf ℂ
	+ $i > 0$ ==> $i^2 = -1 > 0$
	+ $i < 0$ ==> $i^2 = -1 > 0$

### Konjugation
+ konjugiert komplexe Zahl x - iy =  \_x+iy\_ (eigentlich mit Strich darüber)
+ z \* Z = x<sup>2</sup> + y<sup>2</sup> ≥ 0 
+ |z| =  $\sqrt[2]{z*Z}$ ∈ ℝ
+ (Z + W) = (Z) + (W)
+ (Z \* W) = (Z) \* (W)
+ |z \* w| = |z| \* |w|

### Wurzel
+ Sei $z^2 = a + ib$
	+ $x^2 - y^2 = a$
	+ $2xy = b$
	+ $x = +-\sqrt[2]{\frac{a + \sqrt[2]{s^2 + b^2}}{2}}$
	+ $y = +-\sqrt[2]{\frac{-a + \sqrt[2]{s^2 + b^2}}{2}}$
	+ Vorzeichen sind so zu wählen, dass 2xy = b gilt ==> 2 Lösungen
		+ +x, -y
		+ -x, +y

### Komplexe Zahlen im Graph
+ X/Y-Diagramm
	+ x = Re(z)
	+ y = Im(z)
+ Rechenoperationen:
	+ Addition ==> Zahlen zusammenhängen
		 ![](Pasted%20image%2020211108172201.png)		
	+ Konjugieren ==> Spiegeln an Achse des Realteils
		 ![](Pasted%20image%2020211108172217.png)
	+ Multiplikation ==> Längen multipliziert und Winkel addiert
		 ![](Pasted%20image%2020211108172247.png)

### Wurzel ziehen in ℂ
+ $z^n=w$ w∈ℂ\\{0}, n∈ℕ
+ $z=|z|e^{iφ}$ - unbekannt
+ $w=|w|e^{iψ}$ - bekannt
	+ $|w|=\sqrt[2]{a+bi}$
	+ $ψ$ 
		+ $|w|e^{iψ}=|w|(cos(ψ)+isin(ψ))$
		+ $cos(ψ)=a/|w|$
			+ 2 Lösungen
			+ $arcos(a/|w|)=ψ$
			+ $-arcos(a/|w|)=ψ$
		+ $sin(b/|w|)=ψ$
			+ positiv ==> $arcos(a/|w|)=ψ$
			+ negativ ==> $-arcos(a/|w|)=ψ$
+ Formel: $z=\sqrt[n]{|w|}exp(\frac{i}{n}(ψ+2kπ))$ k=0,...,n-1
	+ hergeleitet durch $z^n=|z|^n e^{inφ}=|w|e^{iψ}=w$
	+ keine Lösung für w=0

### Multiplikation
+ z,w∈ℂ
	+ $z=|z|e^{iφ}$
	+ $w=|w|e^{iψ}$
+ $zw=|z||w|e^{i(ψ+φ+2kπ)}$

### Logarithmus
+ $log(w)=ln|w|+i arg(w)$
	+ $arg(w)∈(-∈,∈]$
+ $i^i=e^{ilog(i)}=e^{i^2\frac{π}{2}}=e^{-\frac{π}{2}}$

