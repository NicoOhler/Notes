# Winkelfunktionen
+ $e^x=\sum_{n=0}^∞ \frac{x^n}{n!}$ konvergiert für alle x∈ℂ
	+ $i^2=-1$
	+  $e^{ix}=\sum_{n=0}^∞ \frac{(ix)^n}{n!}=\sum_{n=0}^∞ \frac{(ix)^{2n}}{(2n)!} + \sum_{n=0}^∞ \frac{(ix)^{2n+1}}{(2n+1)!}=$
	+  $=\sum_{n=0}^∞ (-1)^n \frac{x^{2n}}{(2n)!} + i \sum_{n=0}^∞ (-1)^n \frac{x^{2n+1}}{(2n+1)!}=cos(x) + sin(x)$ 
		+ $\sum_{n=0}^∞ (-1)^n \frac{x^{2n}}{(2n)!}=cos(x)$	
		+ $\sum_{n=0}^∞ (-1)^n \frac{x^{2n+1}}{(2n+1)!}=sin(x)$
	+ $e^{ix}=cos(x) + isin(x)$
+ $sin(x)^2+cos(x)^2=1$
+ $|sin(x)|≤1$ und $|cos(x)|≤1$
+ $sin(-x)=-sin(x)$
	+ gerade Funktion
+ $cos(-x)=cos(x)$
	+ ungerade Funktion
+ $sin(x)$ und $cos(x)$ sind alternierende Reihen
+ $sin(x)$ und $cos(x)$ sind bijektiv in [0,2π)

### Additionstheoreme
+ $cos(x+/-y)=cos(x)*cos(y)-/+sin(x)*sin(y)$
	+ $cos(x+y)=cos(x)*cos(y-sin(x)*sin(y)$
	+ $cos(x-y)=cos(x)*cos(y)+sin(x)*sin(y)$
		+ $cos(x)cos(y)=\frac{1}{2}(cos(x+y)+cos(x-y))$
		+ $sin(x)sin(y)=\frac{1}{2}(cos(x-y)-cos(x+y))$
+ $sin(x+/-y)=sin(x)*cos(y)+/-cos(x)*sin(y)$
	+ $sin(x+y)=sin(x)*cos(y)+cos(x)*sin(y)$
	+ $sin(x-y)=sin(x)*cos(y)-cos(x)*sin(y)$
		+ $sin(x)cos(y)=\frac{1}{2}(sin(x+y)+sin(x-y))$
		+ $cos(x)sin(y)=\frac{1}{2}(sin(x+y)-sin(x-y))$
+ Äquivalenzen mit α und β siehe VO#21
+ Spezialisierungen
	+ $sin(2x)=2sin(x)cos(x)$
	+ $cos(2x)=cos(x)cos(x)-sin(x)sin(x)=2cos(x)^2-1=1-2sin(x)^2$

### Besondere Stellen
+ sin(x) und cos(x) wiederholen sich periodisch alle 2π
	+ $cos(x+2kπ) = cos(x)$
	+ $sin(x+2kπ) = sin(x)$
+ $e^{iπ}=cos(π) + isin(π)=-1$
+ Nullstellen
	+  $cos(x) = 0$ ==> $\frac{π}{2} + kπ$
	+ $sin(x)=0$ ==> $kπ$
	+ für k∈ℤ
+ Extremwerte
	+ $cos(x)=1$ ==> $2kπ$
	+ $cos(x)=-1$ ==> $(2k+1)π$
	+ $sin(x)=1$ ==> $\frac{π}{2}+2kπ$
	+ $sin(x)=-1$ ==> $\frac{π}{2}+(2k+1)π$ 
	+ für k∈ℤ


### Umkehrfunktionen
+ arc(us)cosinus und arc(us)sinus
	+ Umkehrfunktionen der eingeschränkten cos(x) und sin(x)
	+ Zyklometrische Funktionen
	+ messen Einheitskreisbogen ab
+ Zurückrechnen:
	+ $cos(x)=y$
		+ {$x∈ℝ|cos(x)=y$} = {$arccos(y)+2kπ,2kπ-arccos(y)|k∈ℤ$}		
	+ $sin(x)=y$
		+ {$x∈ℝ|sin(x)=y$} = {$arcsin(y)+2kπ,(2k+1)π-arcsin(y)|k∈ℤ$}

### TODO Polarkoordinaten
+ #VO 23 bis min 18

### Tangens und Cotangens
 + $tan(x)=\frac{sin(x)}{cos(x)}$
	 + nicht definiert für cos(x)=0
 + $cot(x)=\frac{cos(x)}{sin(x)}$
	 + $cot(x)=\frac{1}{tan(x)}$
	 + nicht definiert für sin(x)=0
 + $tan(-x)=-tan(x)$
	 + ungerade Funktion
 + Monotonie
	 + streng monoton wachsend auf ($\frac{-π}{2},\frac{π}{2}$)
	 + somit injektiv und stetig