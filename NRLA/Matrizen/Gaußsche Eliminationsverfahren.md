# Gaußsche Eliminationsverfahren
## Algorithmus

## Lösungssatz
Lösungen des linearen Gleichungssystem: A * x = B
+ eindeutige Lösung:  Rang(A) = Rang(A|b) = Spaltenanzahl
+ keine Lösung: Rang(A) < Rang(A|b)
+ ∞ Lösungen: Rang(A) = Rang(A|b) < Variablenanzahl

## Bestimmen von ∞ Lösungen:
+ freie Variable x<sub>n</sub>=t
+ In reduziertem System mithilfe der neuen Variable die anderen Variablen bestimmen
	+ Rückwärts einsetzen oder Gauß-Jordan-Verfahren
+ Beispiel:
 
![[Gaußsche, Bestimmung unendlicher Lsg.png]]
#### Struktursatz:
+  Die allgemeine reelle Lösung des reellen lineare Gleichungssysten: A * x = B 
	kann geschrieben werden als:
+ x<sub>allg</sub> = x<sub>H</sub> + x<sub>P</sub>
	+  x<sub>H</sub> allgemeine homogene Lösung
	+  x<sub>P</sub> (eine) partikuläre/spezielle Lösung


[[NRLA]]