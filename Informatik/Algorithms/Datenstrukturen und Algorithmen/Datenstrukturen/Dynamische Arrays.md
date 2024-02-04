### Eigenschaften
+ herkömmliches [[Array]]
	+ ![](Pasted%20image%2020221114162748.png)
	+ hat jedoch fixe Größe
+ dynamische Größe
+ gleich effiziente Operationen
	+ amortisierter konstanter Zeit
+ ![](Pasted%20image%2020221114162851.png)

### Grundprinzip
+ ![](Pasted%20image%2020221114162912.png)
+ ersten n Elemente sind befüllt
	+ restlichen können befüllt werden
+ Größe wird verdoppelt, wenn $n_{cap}+1$ Elemente notwendig
	+ Array mit doppelter Größe anlegen
	+ Elemente hinüberkopieren
+ analog beim Löschen
	+ ![](Pasted%20image%2020221114163112.png)

### Operationen
+ Einfügen
	+ ![](Pasted%20image%2020221114163232.png)
+ Löschen
	+ ![](Pasted%20image%2020221114163316.png)

### Speicherverbrauch und Laufzeit
+ ![](Pasted%20image%2020221114163408.png)
+ Einfügen und Löschen haben potentiell schlechte Laufzeit $Ω(n)$
	+ wenn erweitert/geschrumpft wird
	+ ![](Pasted%20image%2020221114163623.png)
	+ [[Amortisierte Analyse]]