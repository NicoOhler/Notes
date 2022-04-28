# Rekursionen und erzeugende Funktionen
### Lineare Rekursion
+ $a_n$ mit n∈ℕ
	+ $a_n=c_1*a_{n-1}+c_2*a_{n-2}+...+c_l*a_{n-l}$
		+  ==>$a_n-c_1*a_{n-1}-c_2*a_{n-2}-...-  c_l*a_{n-l}=0$
	+ $c_i$ Konstante
	+ Anfangsbedingung/startwert fix gegeben
+ Charakteristische Polynom
	+  $Q(x)=x_l-c_1*x_{l-1}-c_2*x_{l-2}-...-c_l$
	+  hat Q(x) l verschiedene Nullstellen $ß_1,ß_2,...,ß_l$
		+  $a_n=α_1*ß^n_1+α_2*ß^n_2+...+α_l*ß^n_l$
		+  Konstanten $α_1, α_2,...,α_l$, sodass Anfangsbedingungen erfüllt
+  Beispiel: Fibonacci-Folge
	+ ![[Pasted image 20220411163659.png]]
	+ ![[Pasted image 20220411163705.png]]

### Erzeugende Funktionen
+ formale Potenzreihe
	+ $A(z):=a_0+a_1*z+a_2*z^2+...=\sum_{n=0}^\infty a_n*z^n$
	+ z formale Variable
+ A(z) heißt erzeugende Funktion/Potenzreihe der Folge $a_n$
+ $[z^n]A(z):=a_n$
	+ Reskalierung
		+ $[Z^n]A(ßz)=ß^n[z^n]A(z)$
	+ Rechenregeln
		+ $A(z)+B(z)=\sum_{n≥0} (a_n+b_n)z^n$
		+ $A(z)*B(z)=\sum_{n≥0}^\infty (\sum_{k=0}^n a_k*b_{n-k})z^n$
		+ $\frac{\partial}{\partial z}(\sum_{n≥0} a_n*z^n)=\sum_{n≥1}n*a_n*z^{n-1}$
+ $B(z)$ ist Reziprokes von $A(z)$, wenn $A(z)*B(z)=B(z)*A(z)=1$
	+ $A(z)=\frac{1}{B(z)}$
	+ Beispiele:
		+ geometrische Reihe
			+ ![[Pasted image 20220428144758.png]]
		+ Fibonacci
			+ ![[Pasted image 20220428145740.png]]
			+ ![[Pasted image 20220428145813.png]]
			+ ![[Pasted image 20220428145823.png]]
+ $a_n$ bestimmen?
	+ ![[Pasted image 20220428151212.png]]


### Nicht lineare Rekursion
+ Binomial Lehrsatz für nicht lineare Rekursionen
	+ ![[Pasted image 20220428152048.png]]
+ Binärbaum △ rekursiv definiert, wenn
	+ einzelner externer Knoten oder
	+ interner Knoten zusammen mit Binärbaum links und rechts 
		+ links $△_l$
		+ rechts $△_r$
+ interne Knoten heißen Wurzel
+ externe Knoten heißen Blätter
+ ![[Pasted image 20220428153058.png]]
+ Beispiel: Anzahl der Menge von Binärbaume mit n Blättern
	+ ![[Pasted image 20220428153307.png]]
	+ 

[[Kombinatorik]]