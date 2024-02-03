# Kombinatorik
### Permutation
+ Anordnung von n Elementen
+ Anzahl von Permutation
	+  ohne Wiederholung: n!
	+ mit Wiederholung: $\frac{n!}{k_1!...k_n!}$
		+ $k_i$ Anzahl gleicher Objekte
		+ Beispiel: 8 Kugeln, davon 3 rot und 5 blau
			+ $n=8$
			+ $k_1=3$
			+ $k_2=5$

### Variation
+ Auswahl von k Elementen aus n verschiedenen Elementen
+ Berücksichtigung der Reihenfolge
+ Anzahl von Variationen
	+ ohne Wiederholung: $\frac{n!}{(n-k)!}$ 
	+ mit Wiederholung: $n^k$

### Kombination
+ Auswahl von k Elementen aus n verschiedenen Elementen
+ keine Berücksichtigung der Reihenfolge
+ Anzahl von Kombinationen
	+ ohne Wiederholung: $\binom{n}{k}=\frac{(n+k-1)!}{(n-1)!k!}$ 
	+ mit Wiederholung: $\binom{n+k-1}{k}=\frac{n!}{(n-k)!k!}$ 



### Cheat-Sheet
![[Kombinatorik-Formeln-1024x576.jpg]]

[[Diskrete Mathematik]] [[../../../test/a.md/Analysis]] [[Binomische Lehrsatz]]