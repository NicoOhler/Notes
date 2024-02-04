### Übersicht
+ $y^{(n)}+a_{n-1}*y^{(n-1)}+...+a_1*y'+a_0*y=0$
	+ a ... gegebene Konstanten
	+ DGL n-ter Ordnung
	+ Anwendungsfall: Masse-Feder abhängig von
		+ Masse mal Beschleunigung
		+ Reibung mal Geschwindigkeit
		+ Federzug mal Strecke
		+ ![](../../../z_images/Pasted%20image%2020220413095615.png)
+ zweidimensionales GLS lösbar, wenn zwei linear unabhängige Lösungen gegeben
	+ z.B.
		+ $x(0)$ Anfangsauslenkung gegeben
		+ $x'(0)$ Anfangsgeschwindigkeit gegeben
	
### Ansatz
+ ![](../../../z_images/Pasted%20image%2020220427141810.png)
+ ![](../../../z_images/Pasted%20image%2020220427142310.png)
	+ Nullstellen des charakteristischen Polynoms entsprechen Lösungen
	+ alle Nullstellen verschieden ==> alle Lösungen gefunden
+ ![](../../../z_images/Pasted%20image%2020220427143038.png)
+ ![](../../../z_images/Pasted%20image%2020220427143648.png)

### Vorgehensweise
+ ![](../../../z_images/Pasted%20image%2020220427145109.png)
+ Gleichung in charakteristische Polynom umwandeln
+ Polynom in Linearfaktoren zerlegen
	+ mehrere Nullstellen ==> innere Resonanz
+ umformen nach λ
	+ quadratische Gleichung
+ Fallunterscheidung der Diskrimante D
	+ D < 0
		+ zwei komplexe Lösungen (x+yi)
			+ kongugiert ebenfalls Lösungen
		+ umwandeln in reelle Lösungen
			+ Nullstellen ergeben zusammen reelle Lösung
			+ $λ_{1/2}=e^xe^{±iy} = e^x*sin(y)/cos(y)$
			+ ![](../../../z_images/Pasted%20image%2020220427145926.png)
		+ ![](../../../z_images/Pasted%20image%2020220427145359.png)
	+ D = 0
		+ Doppellösung ==> allgemeine Lösung
		+ ![](../../../z_images/Pasted%20image%2020220427145410.png)
	+ D > 0
		+ zwei verschiedene reellle Lösungen
		+ ![](../../../z_images/Pasted%20image%2020220427145416.png)
+ Zusammenfassung
	+ ![](../../../z_images/Pasted%20image%2020220427150013.png)

### Beispiele
+ ![](../../../z_images/Pasted%20image%2020220427150842.png)
+ ![](../../../z_images/Pasted%20image%2020220427151157.png)
	

[[Differentialgleichungen]]