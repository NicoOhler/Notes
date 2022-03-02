# Extremwertaufgaben mit Nebenbedingungen
+ Finde Extrema von $f(x_1,...,x_n)$ unter den Nebenbedingungen
	+ $N_1(x_1,...,x_n)=0$
	+ ...
	+ $N_k(x_1,...,x_n)=0$
+ Anzahl der Nebenbedingungen k ist beliebig
+ Satz:
	+ $M⊆ℝ^n$ offen
	+ f (mind.) 1x stetig diffbar
	+ Extremum $x_0$ unter NB $N_1(x)=...=N_k(x)=0$ ==> ∃λ für jede NB
	+ $grad(f(x_0))-λ_1 grad(N_1)(x_0)-...-λ_k grad(N_k)(x_0)=0$
		+ $grad f = λ grad N$
+ Vorgehensweise
	+ in obige Formel einsetzen
	+ eine Gleichung für jede Variable nach der abgeleitet wird
	+ Determinante der Koeffizientenmatrix mit 0 gleichsetzen
		+ λ bestimmen
	+ λ in Gleichung einsetzen und Variablenwerte bestimmen
		+ ==> mögliche Extrema
		+ Satz von Weierstraß ==> Min und Max muss existieren
		+ Min und Max durch logische Vergleiche bestimmen? 
+ Anschauliches Beispiel
	+ ![[Pasted image 20220301130440.png]]

### Im Mehrdimensionalen
+ grad f senkrecht auch Tangentialebene von A
	+ $grad f ∈ span\{grad N_1, ..., grad N_p\}$