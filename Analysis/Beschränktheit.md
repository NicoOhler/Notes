# Beschränktheit 
+ Eine Menge A ⊆ ℝ heißt beschränkt, wenn es ein M > 0 gibt, sodass ∀x∈A: |x|≤M
	+ beschränkt ==> jedes Element befindet sich unter der Schranke M

## Supremum und Infimum
+ Jede beschränkte Folge besitzt eine größte und eine kleinste Schranke
	+ Infimum i = größte untere Schranke
	+ Supremum s = kleinste obere Schranke
	+ ∀x∈A: i≤|x|≤s
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




[[Analysis]][[Monotonie]]