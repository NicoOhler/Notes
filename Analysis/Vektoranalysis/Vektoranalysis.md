# Vektoranalysis 
+ Sei $U⊆ℝ^2 (bzw. ℝ^3)$ offen. Dann ist $\overrightarrow{V}:U$-->$ℝ^2 (bzw. ℝ^3)$ ein Vektorfeld
	+  $\overrightarrow{V}$ besteht aus Koordinatenfunktionen
	+ $\overrightarrow{V}:U$ auf U koordinatenweise differenzierbar
		+ ==> differenzierbares Vektorfeld
+ Gesucht:  geleistete Arbeit W bei Bewegung entlang Kurve C in $\overrightarrow{V}$
	+ C: $\overrightarrow{x}(t)$
	+ t∈\[a,b]
	+ $W = \int_a^b <\overrightarrow{V}(\overrightarrow{x}(t)),\bar{\overrightarrow{x}}(t)>dt$
		+ $\bar{\overrightarrow{x}}(t)dt=d\overrightarrow{x}$
	+ $\overrightarrow{V}$ besteht aus P(t), Q(t), R(t) ==> $W=\int_C Pdx+Qdy+Rdz$
+ Kurven/Wegintegral ist unabhängig von orientierter Parametrisierung
	+ lediglich von Kurve und Vektorfeld
+ Bewegung entlang anderer Kurve in selbem Bereich ==> W anders
	+ ![[Pasted image 20220316090732.png]]
	+ ![[Pasted image 20220316091028.png]]
+ Weitere Beispiele
	+ ![[Pasted image 20220316091413.png]]

### Unabhängig von Kurve
+ ang. W hängt nur von Anfangs- und Endpunkt von C ab
+ ![[Pasted image 20220316092347.png]]
	+ a,b sind Anfangs und Endpunkt
	+ Φ ist Potential zu $\overrightarrow{V}$
+ $grad Φ=\overrightarrow{V}$
	+ gibt es nur, wenn
	+ $\frac{\partial P}{\partial y}=\frac{\partial Q}{\partial x}$