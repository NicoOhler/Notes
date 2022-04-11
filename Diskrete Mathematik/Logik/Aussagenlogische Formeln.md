# Aussagenlogische Formeln
### Belegung
+ V ist die Menge der aussagenlogischen Variablen
	+ V'⊆V
+ Belegung mit Wahrheitswerten
	+ Funktion β: V'-->{w,f}
+ vollständige Belegung mit Wahrheitswerten
	+ wenn alle Variablen abgebildet werden
	+ Funktion β: V-->{w,f}


### Fortsetzung
+ L ist die Menge aller Formeln über Variablen in V
+ Fortsetzung ß  L: -->{w,f}, x-->ß(x)
	+ ∀v∈V: ß(v)=β(v)
	+ ∀x∈L: ß(¬x)=¬ß(x)
	+ ∀x,y∈L: ß(x∧y)=ß(x)∧ß(y)
		+ analog für andere binäre Operationen
	+ ß(x) heißt Wahrheitswert von x unter Belegung β
		+ $[[x]]_β$
+ > **_NOTE:_** Unterschied zwischen ß und β!
+ vollständige Belegung β erfüllt x, wenn ß(x)=w
	+ β ist Model für x
	+ b|=x
	+ ![[Pasted image 20220401141438.png]]
+ Formel erfüllbar, wenn für mindestens eine Belegung gilt:
	+ ß(x)=w
+ Tautologie T 
	+ wenn jede vollständige Belegung erfüllbar ist
	+ |=x
	+ ![[Pasted image 20220401142028.png]]
+ Kontradiktion bzw. unerfüllbar ⊥
	+ wenn jede vollständige Belegung unerfüllbar ist
		+ ß(x)=f
+ Beispiele:
	+ ![[Pasted image 20220401142240.png]]

[[Diskrete Mathematik]]