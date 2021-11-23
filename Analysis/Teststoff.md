# Teststoff
## 1. Klausur
+ vollständige Induktion
	1) Basis A(1)
	2) Voraussetzung A(n)
	3) Behauptung A(n+1)
	4) Schritt A(n)==>A(n+1)
+ Kombinatorik?
	+ 
	Cheat-Sheet ausdrucken
+ Binomische Lehrsatz
	+ (a+b)^n = sum k=0 bis inf (n über k) x^k y^(n-k)
	+ n über k = n!/(k!(n-k)!)

+ Folgen
	+ Konvergenz
		+ Cauchy Kriterium
			+ TODO
		+ monoton wachsend/fallend und beschränkt
		+ Monotonie bei rekursiv definierten Folgen
			+ x<sub>n</sub> > x<sub>n+1</sub>
			+ umformen auf x<sub>n+1</sub> > x<sub>n+2</sub>
	+ Grenzwertrechnungen
	+ a+-*b=lim an+-*bn
	+ auch div wenn != 0
	+ Bruch durch n^x
+ Reihen
	+ Wert
		+ Teleskopreihen und TODO
	+ konvergiert genau dann, wenn Folge ihrer Partialsummen konvergiert - todo
	+ Konvergenzkriterien
		+ Cauchy-Kriterium notwendig?
		+ Majorantenkriterium
		+ Minorantenkriterium
		+ Leibniz-Kriterium
		+ Quotienten-Kriterium
		+ Wurzel-Kriterium
+ Funktionen
	+ injektiv ==> Element der Zielmenge höchstens einmal von f(x) abgebildet
	+ surjektiv ==> jedes Element in Zielmenge mindestens einmal von f(x) abgebildet
	+ bijektiv ==> injektiv und surjektiv ==> jedes Element in Zielmenge genau einmal von f(x) + abgebildet
	+ Fixpunkt ==> f(x)=x
	+ strenge Monotonie ==> injektiv
	+ gerade Funktion symmetrisch zur y-Achse ==> f(x) = f(-x)
	+ ungerade Funktion symmetrisch zum Ursprung ==> f(-x) = -f(x)

+ Stetigkeit
	+ Nullstellensatz
		i+ st f: [a,b]-->R stetig und f(a)*f(b) < 0 ==> f(x)=0 existiert und kann mittels Intervallschachtelung bestimmt werden
	+ Zwischenwertsatz
		+ ist f: [a,b]-->R stetig ==> f nimmt jeden Wert zwischen f(a) und f(b) an
	+ Grenzwertkriterium
		+ f ist stetig in x0 wenn für jede Folge xn mit x0=lim(xn) gilt f(x0)=lim(f(xn))=f(lim(xn))
	+ delta epsilon Kriterium
		∀ε>0 ∃δ>0 ∀x∈I: |x - x0| < δ ==> |f(x) - f(x0)| < ε
		+ |f(x) - f(x0)| ersetzen mit Formel ==> umformen/abschätzen
		+  ==> |x - x0| separater Term
		+  	λ * |x - x0| < ε ==> |x - x0| < λε = δ ==> stetig in x0
		+ Trick TODO

+ Sonstige Sätze
	+ Bolzano Weierstraß
		+ Jede beschränkte Folge reeller Zahlen (mit unendlich vielen Gliedern) hat (mindestens) einen Häufungspunkt.
	 + (1+x)^n ≥ 1 + nx
