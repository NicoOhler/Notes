# Laplace Transformation
### Übersicht
+ [[Anwendungen der Residuenrechnung]]
+ f: $[a,\infty)$-->ℝ
+ Laplace Transformation 
	+ ![[Pasted image 20220608124719.png]]
	+ $Lf(s)$ f existiert, wenn $∃A,C∈ℝ ∀t∈ℝ^+:|f(t)|≤Ce^{At}$
+ Konvergergenzabszisse $c_0(f)$
	+ $∀f∃c_0(f)∈ℝ:∀s∈ℂ$ mit $Re(s)>c_0(f)$ $Lf(s)$ existiert
	+ $Lf(s)$ ist holomorphe Funktion für $Re(s)>c_0(f)$
+ Doetsch Symbol
	+ Beziehung zwischen f und Lf
	+ ![[Pasted image 20220608130107.png]]

### Rechenregeln für L
![[Pasted image 20220608130146.png]]
![[Pasted image 20220608133621.png]]

### DGL lösen
+ ![[Pasted image 20220608132508.png]]
	+  Laplace Transformation auf lineare DGL
	+ dividieren statt DGL lösen  
	+ Rücktransformation
+ Beispiel: Rücktransformation mit PBZ
	+ ![[Pasted image 20220608133514.png]]

### Laplace Umkehrformel
+ ![[Pasted image 20220608134312.png]]
+ Rücktransformation mit CIF statt
	+ PBZ
	+ Bekanntsein der Rechenregeln für L
+ Verschiebung in Gebiet mit Polstellen
	+ ==> Residuensatz statt CIF
	+ ![[Pasted image 20220608135348.png]]
		+  Verschieben des Kurvenintegrals im holomorphen Gebiet ändert nichts
		+  Kurvenintegral = 0
		+  Summe der Residuen bleibt übrig

### Beispiele mit Umkehrformel 
+ gleiche Beispiel wie oben jedoch ohne PBZ
	+ ![[Pasted image 20220608135221.png]]
	+ ![[Pasted image 20220608135420.png]]
+ Rechteckschwingung mit unendlich Polen
	+ ![[Pasted image 20220608140316.png]]
	+ ![[Pasted image 20220608140742.png]]
	+ ![[Pasted image 20220608140835.png]]
+ Kirchhoffsche Gesetz
	+ ![[Pasted image 20220608145504.png]]
	+ ![[Pasted image 20220608150128.png]]
	+ ![[Pasted image 20220608150811.png]]
+ 