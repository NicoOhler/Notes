### Eigenschaften
+ herkömmliches [[Array]]
	+ ![](../../../../z_images/Pasted%20image%2020221114162748.png)
	+ hat jedoch fixe Größe
+ dynamische Größe
+ gleich effiziente Operationen
	+ amortisierter konstanter Zeit
+ ![](../../../../z_images/Pasted%20image%2020221114162851.png)

### Grundprinzip
+ ![](../../../../z_images/Pasted%20image%2020221114162912.png)
+ ersten n Elemente sind befüllt
	+ restlichen können befüllt werden
+ Größe wird verdoppelt, wenn $n_{cap}+1$ Elemente notwendig
	+ Array mit doppelter Größe anlegen
	+ Elemente hinüberkopieren
+ analog beim Löschen
	+ ![](../../../../z_images/Pasted%20image%2020221114163112.png)

### Operationen
+ Einfügen
	+ ![](../../../../z_images/Pasted%20image%2020221114163232.png)
+ Löschen
	+ ![](../../../../z_images/Pasted%20image%2020221114163316.png)

### Speicherverbrauch und Laufzeit
+ ![](../../../../z_images/Pasted%20image%2020221114163408.png)
+ Einfügen und Löschen haben potentiell schlechte Laufzeit $Ω(n)$
	+ wenn erweitert/geschrumpft wird
	+ ![](../../../../z_images/Pasted%20image%2020221114163623.png)
	+ [[Amortisierte Analyse]]