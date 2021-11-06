 # Beschränktheit 
+ Eine Menge A ⊆ ℝ heißt beschränkt, wenn es ein M > 0 gibt, sodass ∀x∈A: |x|≤M
	+ beschränkt ==> jedes Element befindet sich unter der Schranke M
+ Ist eine Folge beschränkt und monoton fallend/wachsend ist sie konvergent

## Supremum und Infimum
+ Jede beschränkte Folge besitzt eine größte und eine kleinste Schranke
	+ Supremum s ==> kleinste obere Schranke
		+ größte Häufungspunkt
		+ limes superior ==> obere Häufungsgrenze
	+ Infimum i ==> größte untere Schranke
		+ kleinste Häufungspunkt
		+ limes inferior ==> untere Häufungsgrenze
	+ ∀x∈A: i≤|x|≤s
+ Eine Folge ist konvergent, wenn limes inferior = limes superior
+ Supremum und Infimum können mittels Intervallschachtelung bestimmt werden

``` ad-note
title: Beispiel am Supremum
a<sub>0</sub> = keine obere Schranke
b<sub>0</sub> = obere Schranke
m<sub>n+1</sub> = (a<sub>n</sub> + b<sub>n</sub>)/2
+ m<sub>n+1</sub> = obere Schranke ==> a<sub>n+1</sub> = a<sub>n</sub>, b<sub>n+1</sub> = m<sub>n</sub>
+ m<sub>n+1</sub> = keine obere Schranke ==> a<sub>n+1</sub> = m<sub>n</sub>, b<sub>n+1</sub> = b<sub>n</sub>
+ Bestimmen von m<sub>n+1</sub> bis Supremum gefunden
```




[[Analysis]][[Monotonie]][[Reihen und Folgen]]