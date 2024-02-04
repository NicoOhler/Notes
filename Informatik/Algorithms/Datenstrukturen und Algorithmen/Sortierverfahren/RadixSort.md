### Eigenschaften
+ nicht vergleichsbasiert
+ Annahme
	+ Anzahl der (Dezimal)Stellen konstant
	+ kleine Anzahl an Stellen
+ effizienter für große Datenmengen
+ hoher Speicheraufwand
+ womöglich hybrides Sortierverfahren
	+ n groß => RadixSort
	+ n klein => InsertionSort

### Verfahren
+ Streuphase
	+ n aufteilen in Fächer/Buckets
	+ 1 Fach für jeden möglichen Wert
		+ 10 für dezimal
		+ 2 für binär
+ Sammelphase
	+ Fächer zusammenfügen
	+ sortiert nach i-ter Stelle
+ wiederholen bis alle Stellen durchlaufen
+ führende Nullen für  Zahlen mit zu wenig Stellen
+ ![[../../../../z_images/Pasted image 20221028162653.png]]
+ ![[../../../../z_images/Pasted image 20221028162857.png]]
