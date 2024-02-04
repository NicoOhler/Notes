+ PxA = LxR
	+ P - Permutationsmatrix für Zeilenvertauschungen
	+ A - Ausgangsmatrix
	+ R - rechte Matrix
		+ A nach Zeilenvertauschung in Zeilenstufenform gebracht
	+ L - linke Matrix
		+ 1 in Hauptdiagonale
		+ 0 über Hauptdiagonale
		+ Vielfaches, welche von Zeile abgezogen werden um R in Zeilenstufenform zu bekommen
			+ II - (-3)\*I um erstes Element der 2. Zeile in R auf 0 zu bekommen
			+ ==> erste Element der 2. Zeile in L = -3

## Anwendungen
+ lineares Gleichungssystem: A*x = b
	+ A ist regulär
	+ genau eine Lösung
+ A = LR ==> LRx = b
	+ y := Rx ==>  zwei Gleichungssysteme
		+ Ly = b
		+ Rx = y
	+ leicht zu lösen wegen △-Matrix
![](../../../z_images/Pasted%20image%2020211028131447.png)

[[Matrix]]