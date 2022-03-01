# Hauptsatz über implizite Funktionen
### Problemstellung
+ Gleichungssystem mit p + q Variablen und p Gleichungen 
	+ nach q Variablen auflösen
	+ ![[Pasted image 20220301114831.png]]
+  Vorgehensweise:
	+  alle "ungwollten" Variablen auf linke Seite
	+  Koeffizientenmatrix aufstellen
		+  invertierbar <==> auflösbar nach "gewollten" Variablen
	
### Hauptsatz über implizite Funktionen
+ f: $M⊆ℝ^{p+q}$-->$ℝ^p$
	+ M offen
	+ GLS mit p+q Variablen und p Gleichungen
	+ $M(ζ): f_i(x_1,...,x_p,y_{p+1},y_{p+q})=0$
+ Bedingungen
	+ $f_i(ζ)=0$ für i = 1 bis p
	+ Koordinatenfunktion $f_i$ mindestens einmal stetig differenzierbar
		+ für i = 1 bis p
	+ Ableitungsmatrix (nicht Jacobi)
		+ $\partial (f_1,...,f_p)$