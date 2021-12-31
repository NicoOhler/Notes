# Bestimmte Integral
+ Fläche A unter Funktion f im Bereich \[a,b] bestimmen
+ $A=\int^b_a f(x)dx=F(b)-F(a)$, wenn
	+ $f:[a,b]-->ℝ$ stetig
	+ $F:[a,b]-->ℝ$ eine Stammfunktion von f

### Herleitung
+ viele untere und obere Schranken für Fläche finden
	+ Unterschied zwischen Schranken muss beliebig klein werden
+ Fläche wird in x Bereiche unterteilt
	+ Untersummen und Obersummen entstehen
	+ desto mehr Zerteilungen, 
		+ desto größer die Untersummen
		+ desto kleiner die Obersummen
		+ größte Untersumme ≤ kleinste Obersumme
+ Fläche = Infimum der Obersummen = Supremum der Untersummen
	+ gleich, wenn genug Zerteilungen stattfanden
	+ Riemann-Darboux-Integral
	+ beide gleich <==> f ist Riemann-integrierbar auf \[a,b]

### Riemannsches Integralibilitätskriterium
+ f ist Riemann-integrierbar auf \[a,b], wenn
	+ $∀ε>0 ∃Z: \bar{S}(f,Z)-\underline{S}(f,Z)<ε$
+ Sei f stetig <==> f ist Riemann-integrierbar
	+  Beweis VO#35
+ Sei f monoton (wachsend/fallend) <==> f ist Riemann-integrierbar
	+  Beweis VO#35
+  Vorzeichenwechsel in \[a,b]  ==> Fläche mit positiven y - Fläche mit negativen y
+ MWS der Integralrechnung
	+ Sei f:\[a,b] --> ℝ stetig
		+ $∃α∈[a,b]: \int_a^bf(x)dx=f(α)(b-a)$
	+ MWS
		+ Integralwert liegt zwischenMinimum und Maximum
		+ Laut MWS: jeder Wert zwischen Minimum und Maximum wird angenommen

### Eigenschaften
+ a < b < c ==> $\int^b_a f(x)+\int^c_b f(x)=\int^c_a f(x)$
+ $\int^b_a f(x)=-\int^a_b f(x)$
+ Linearität
	+ Summe von Integrale = Integral von Summen
	+ Konstanten darf man herausziehen
+ 
	