# Bäume & Spannbäume
### Bäume
+ Graph ohne Kreis heißt Wald
+ Grap heißt Baum, wenn
	+ zusammenhängend
	+ ohne Kreis <==> $|E|=|v|-1$
+ für je zwei Knoten, gibt es genau einen Pfad
+ Wurzel $x_0$ ist "Spitze" von Baum
	+ ![[Pasted image 20220512164947.png]]
	+ jeder Knoten (außer $x_0$) hat genau einen (ersten) Vorgänger $v(x)$
		+ $d(x_0,v(x))<d(x_0,y)$
		+ $v^{k}(x)=$ k-te Vorgänger 
	+ Nachfolger sind Nachbarn ohne Vorgänger
		+ ![[Pasted image 20220512165341.png]]
		+ Blätter Nachfolger ohne Nachfolger
	+ Höhe von x $h(x)=d(x_0,x)$

### Path Finder
+ Input: Baum T, Knoten x,y
+ Output: kürzeste Pfad von x nach y
+ Algorithmus
	+ wähle Knoten $x_0$ aus $V/\{x,y\}$ als Wurzel
	+ bestimme Pfad  $P_x$ von x bis $x_0$
		+ $P_x=(x,v^{1}(x),v^{2}(x),...,v^{k}(x)=x_0)$
		+ automatisch kürzeste Pfad
	+ bestimme Pfad $P_y$ von y bis $x_0$
	+ bestimme kleinsten gemeinsamen Vorgänger j
		+ ![[Pasted image 20220512170005.png]]
	+ return Pfad von x zu j nach y
		+ ![[Pasted image 20220512170121.png]]

### Spannbäume
+ Baum T ist Spannbaum von G, wenn
	+ $V(T)=V(G)$
	+ $E(T)⊆E(G)$
	+ ![[Pasted image 20220512170337.png]]
+ Laplace-Matrix L(G)
	+ n×n Matrix mit bis zu n Eigenwerten $λ_1,λ_2,...,λ_{n-1}$
		+ $∀0≤i≤n-1: λ_i≥0$
		+ kleinste λ = 0
		+ ![[Pasted image 20220512173159.png]]
+ Matrix-Baum-Satz von Kirchhoff
	+ sei G ein zusammenhängender Graph mit n Knoten
	+ \#Spannbäume von G = $\frac{1}{n} λ_1*...*λ_{n-1}$
+ Cayley-Formel
	+ \#Spannbäume von $K^n=n^{n-2}$
	+ ![[Pasted image 20220513134027.png]]
	+ ![[Pasted image 20220512173648.png]]
	+ ![[Pasted image 20220512173715.png]]

[[Wege und Kreise]]