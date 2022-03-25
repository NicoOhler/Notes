# Satz von Euler-Fermat
+ $G_m:={[x_m]∈Z_m:ggT(x,m)=1}$
	+ Repräsentantensystem $R:={0,1,...,m-1}$
+ Eulersche Phi-Funktion
	+  $φ(m):=|G_m|=|{k∈R:ggT(k,m)=1}|$
	+  p∈P ==> $ggT(k,p)=1$ für alle k ==> $φ(p)=p-1$
+  Laut Primfaktorzerlegung gilt für m∈ℕ, m≥2
	+  $m=p_1^{k_1}...p_r^{k_r}$
	+  $φ(p)=p_1^{k_1-1}(p-1)...p_r^{k_r-1}(p_r-1)$
		+  $φ(p)=\prod_{i=1}^k p_i^{l_i-1}(p_i-1)$
+  für $ggT(p,n)=1$ gilt
	+ $a^{p-1}≡_p1$
	+ Beweis
		+  ![[Pasted image 20220325095038.png]]
		+  ![[Pasted image 20220325095238.png]]
		+  ![[Pasted image 20220325095327.png]]
		+  ![[Pasted image 20220325095509.png]]
+  Satz von Euler-Fermat
	+   $a^{φ(m)}≡_m1$
	+   $a^{l(p-1)(q-1)+1}≡_{pq}a$
		+   p,q unterschiedliche Primzahlen