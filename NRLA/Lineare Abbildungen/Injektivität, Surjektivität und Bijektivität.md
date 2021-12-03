# Injektivität, Surjektivität und Bijektivität
+ injektiv ==> jedes Element in Zielmenge wird höchstens 1x abgebildet
	+ injektiv, wenn Kern(F)={0}
+ surjektiv ==> jedes Element in Zielmenge wird mindestens 1x abgebildet
	+ surjektiv, wenn Bild(F)=Zielmenge
+ bijektiv ==> jedes Element in Zielmenge wird genau 1x abgebildet
	+ invers möglich
	+ F' auch linear

### Isomorphismus
+ isomorph, wenn F bijektiv und linear

### Konstruktion
+ Für F: V-->W linear mit n Dimensionen benötigen wir
	+ b<sub>1</sub> --> w<sub>1</sub> = F(b<sub>1</sub>)
	+ ...
	+ b<sub>n</sub> --> w<sub>n</sub> = F(b<sub>n</sub>)	
	+ b-Vektoren bilden Basis in V
+ lineare Fortsetzung
	+ v=α<sub>1</sub>b<sub>1</sub>,..., α<sub>n</sub>b<sub>n</sub>--> α<sub>1</sub>F(b)<sub>1</sub>,..., α<sub>n</sub>F(b)<sub>n</sub>
	+ Bild(F)=Span({F(b<sub>1</sub>),..., F(b<sub>n</sub>)})
	+ Bild von F wird von Bildern der Basis-Vektoren aufgespannt

### Projektion
+ Abbildung von höherer auf niedrigere Dimension
+ nie injektiv
+ F: ℝ<sup>3</sup> --> ℝ<sup>2</sup>, (x,y,z) --> (x,y)
+ Kern(F) = span({0,0,t}) ≠ Nullvektor
	+ t - freie Variable
	+ nicht injektiv
+ 