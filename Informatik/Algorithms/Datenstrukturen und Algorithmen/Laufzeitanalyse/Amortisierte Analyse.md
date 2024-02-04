### Motivation
+ seltene schlechte Laufzeiten mit vielen effizienten Laufzeiten
	+ nicht automatisch ineffizient
+ Begründung
	+ einzelne Operationen sind aufwendig
	+ m aufeinander folgende Operationen sind dennoch effizient
	+ seltene schlechte Laufzeit wird auf häufige gute Laufzeit aufgeteilt

### Beispiel [[Dynamische Arrays]]
+ n-mal Einfügen und einmal erweitern in $O(n)$
	+ $n*O(1)+O(n)=O(2n)=O(n)$
+ ![[../../../../z_images/Pasted image 20221114165707.png]]
+ ![[../../../../z_images/Pasted image 20221114170200.png]]

