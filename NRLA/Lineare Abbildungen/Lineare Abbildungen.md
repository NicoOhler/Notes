# Lineare Abbildungen
+ Lineare Abbildungen repektieren Linearkombinationen
+  F: $ℝ^n$-->$ℝ^m$, $\overrightarrow{x}$-->$\overrightarrow{y}=A-\overrightarrow{x}$
	+ F ist linear, wenn 
		+ $\overrightarrow{x}+\overrightarrow{x'}$-->$F(x)+F(x')$
		+ $λ\overrightarrow{x}$-->$λF(x)$
		+ $λ\overrightarrow{x}+μ\overrightarrow{x'}$-->$λF(x)+μF(x')$

### Rieszsche Darstellungsgesetz d. lin. Alg.
+ F: $V^n$-->ℝ, $\overrightarrow{v}$-->$y=F(\overrightarrow{v})$
	+ ==> $F(\overrightarrow{v})=<\overrightarrow{b},\overrightarrow{v}>$ - eindeutig bestimmt

### Eigenschaften von linearen Abbildungen
+ $\overrightarrow{0}$-->$\overrightarrow{0}$
+ $\overrightarrow{a}-\overrightarrow{b}$-->$F(a)-F(b)$

### Kern und Bild
+ Kern(F):=$\{\overrightarrow{v}∈V:\overrightarrow{v}$-->$\overrightarrow{0}\}$
	+ Kern von F = Menge aller Elemente, welche Null abbilden
+ Bild(F):=$\{F(\overrightarrow{v}):\overrightarrow{v}∈V\}$
	+ Bild von F = Menge aller Elemente in V erreichbar durch Abbildung F

### Menge linearer Abbildungen von V und W
+ $L(V,W):=\{F:V$-->$W:F linear\}$

### Spezielle Abbildungen
+ Nullabbildung:
	+ jeder Vektor bildet den Nullvektor ab
+ identische Abbildung
	+ V-->V
	+ jeder Vektor bildet sich selber ab
+ Gerade
	+ F: ℝ-->ℝ³
	+ $λ$-->$λ\overrightarrow{v}$
	+ Fallunterscheidung:
		+ $\overrightarrow{v}=\overrightarrow{0}$
			+ Kern(F)= ℝ
			+ Bild(F)= $\{\overrightarrow{0}\}$
		+ $\overrightarrow{v}≠\overrightarrow{0}$
			+ Kern(F)=$\{\overrightarrow{0}\}$
			+ Bild(F)=Span($\{\overrightarrow{v}\})$
+  Ebene
	+ F: ℝ²-->ℝ³
	+ $λ$-->$λ\overrightarrow{v}$
	+ Fallunterscheidungen
+ Matrix
	+ A∈ℝ<sup>m×n</sup>
	+ F: ℝ<sup>n</sup>-->ℝ<sup>m</sup>
	+ $\overrightarrow{v}$-->$y=A\overrightarrow{v}$
		+ Kern(F)=Kern(A)=Lösungsmenge des homogenen linearen xGLS

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
+ Bild(F) = span({(0,1), (1,0),(0,0)})
	+ Erzeugendensystem
	+ Basis ohne letzten Vektor

### Verknüpfungen linearer Abbildungen
+ U --> V --> W
	+ U --> W

### Koordinatenabbildung
+ 