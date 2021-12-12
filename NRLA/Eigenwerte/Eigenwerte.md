# Eigenwerte und Eigenvektoren
 + F: V --> V
	 + lineare Selbstabbildung
	 + $Av=λv$
		 + v - Eigenvektor
		 + λ - Eigenwert
		 + A quadratisch
	 + dim(V) endlich ==> EW/EV Problem für Matrizen

### Eigenwert/Eigenvektor-Problem
 + $Av=λv=λIv$ ==> $(A-λI)v=0$
	 +  homogenes lineares Gleichungssystem
	 +  nichttriviale Lösung $v≠0$, wenn $det(A-λI)=0$
		 + $det(A-λI)=0$ charakteristische Gleichung
		 +  $P(λ)=det(A-λI)$charakteristisches Polynom
		 +  $P(λ)=(-1)^nλ^n+b_{n-1}λ^{n-1}+...+b_1λ+b_0$
		 +  Polynomgleichung mit reellen Koeffizienten ==> genau $A^{n×n}$ hat n Eigenwerte
			 +  mit Vielfachheit gezählt
+   $P(λ)=(λ-λ_1)^{k1}...(λ-λ_r)^{kr}$
	+   $λ_1≠λ_2≠...≠λ_r$
	+   $λ_n$ hat algebraische Vielfachheit $k_n$
+ $Av=λv$  ==> Eigenvektoren spannen zum Eigenwert einen Unterraum von $ℂ^n$
	+ $Eigen(λ,A):={v∈ℂ^n: Av=λv}=Kern(A-λI)$
+ Vorgehensweise
	+ Eigenwerte bestimmen
		+ Lösen der charakteristischen Gleichung $det(A-λI)=0$
		+ Polynom als Lösung
		+ dessen Nullstellen/Eigenwerte und Vielfachheiten bestimmen
	+ Eigenvektoren bestimmen
		+ Gleichung $(A-λI)v=0$ für alle Eigenwerte lösen
		+ Eigenraum/span/Dimensionen bestimmen