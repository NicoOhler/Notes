### Übersicht
+ [[Anwendungen der Residuenrechnung]]
+ f: $[a,\infty)$-->ℝ
+ Laplace Transformation 
	+ ![](../../z_images/Pasted%20image%2020220608124719.png)
	+ $Lf(s)$ f existiert, wenn $∃A,C∈ℝ ∀t∈ℝ^+:|f(t)|≤Ce^{At}$
+ Konvergergenzabszisse $c_0(f)$
	+ $∀f∃c_0(f)∈ℝ:∀s∈ℂ$ mit $Re(s)>c_0(f)$ $Lf(s)$ existiert
	+ $Lf(s)$ ist holomorphe Funktion für $Re(s)>c_0(f)$
+ Doetsch Symbol
	+ Beziehung zwischen f und Lf
	+ ![](../../z_images/Pasted%20image%2020220608130107.png)

### Rechenregeln für L
![](../../z_images/Pasted%20image%2020220608130146.png)
![](../../z_images/Pasted%20image%2020220608133621.png)

### DGL lösen
+ ![](../../z_images/Pasted%20image%2020220608132508.png)
	+  Laplace Transformation auf lineare DGL
	+ dividieren statt DGL lösen  
	+ Rücktransformation
+ Beispiel: Rücktransformation mit PBZ
	+ ![](../../z_images/Pasted%20image%2020220608133514.png)

### Laplace Umkehrformel
+ ![](../../z_images/Pasted%20image%2020220608134312.png)
+ Rücktransformation mit CIF statt
	+ PBZ
	+ Bekanntsein der Rechenregeln für L
+ Verschiebung in Gebiet mit Polstellen
	+ ==> Residuensatz statt CIF
	+ ![](../../z_images/Pasted%20image%2020220608135348.png)
		+  Verschieben des Kurvenintegrals im holomorphen Gebiet ändert nichts
		+  Kurvenintegral = 0
		+  Summe der Residuen bleibt übrig

### Beispiele mit Umkehrformel 
+ gleiche Beispiel wie oben jedoch ohne PBZ
	+ ![](../../z_images/Pasted%20image%2020220608135221.png)
	+ ![](../../z_images/Pasted%20image%2020220608135420.png)
+ Rechteckschwingung mit unendlich Polen
	+ ![](../../z_images/Pasted%20image%2020220608140316.png)
	+ ![](../../z_images/Pasted%20image%2020220608140742.png)
	+ ![](../../z_images/Pasted%20image%2020220608140835.png)
+ Kirchhoffsche Gesetz
	+ ![](../../z_images/Pasted%20image%2020220608145504.png)
	+ ![](../../z_images/Pasted%20image%2020220608150128.png)
	+ ![](../../z_images/Pasted%20image%2020220608150811.png)

### Exkurs: Distributionen
+ ![](../../z_images/Pasted%20image%2020220608155543.png)
+ ![](../../z_images/Pasted%20image%2020220608155620.png)
+ ![](../../z_images/Pasted%20image%2020220608155743.png)