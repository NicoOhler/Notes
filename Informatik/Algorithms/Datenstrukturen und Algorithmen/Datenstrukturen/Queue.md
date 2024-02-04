### Eigenschaften
+ implementiert mit [[Array]]
+ FIFO Prinzip
	+ first in first out
+ ![](../../../z_images/Pasted%20image%2020221016134107.png)

### Operationen
+ O(1) für alle Operationen 
![](../../../z_images/Pasted%20image%2020221016134201.png)

### Queue Implementation mittels [[Stack]]
+ verwendet zwei Stacks $S_1, S_2$
	+ S1 zum Einfügen
	+ S2 zum Auslesen/Löschen
+ Elemente von S1 wenn Auslesen/Löschen gefordert nach S2 pushen
+ Elemente von S2 wenn Einfügen gefordert nach S1 pushen
+ ![](../../../z_images/Pasted%20image%2020221016142927.png)
+ Algorithmus/Funktionen
+ ![](../../../z_images/Pasted%20image%2020221016221724.png)
