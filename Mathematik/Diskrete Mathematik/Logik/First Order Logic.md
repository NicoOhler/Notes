### Sprache erster Stufe
+ V Menge der Variablen
+ J  Menge der Junktoren
+ K Menge der Klammern
+ Q Menge der Quantoren
+ ![](../../../z_images/Pasted%20image%2020220403105415.png)
+ Signatur Σ bestehend aus
	+ Konstantensymbole
	+ Funktionssymbole
	+ Relationssymbole
	+ ![](../../../z_images/Pasted%20image%2020220403105618.png)
+ Stelligkeit
	+ Funktions- und Relationssysmbole besitze fixe Parameteranzahl
	+ Stelligkeit = Parameteranzahl
+ Menge der Terme über V und Σ
	+ alle Variablen und Konstanten sind Terme
	+ Funktionen, welche Terme als Input bekommen, sind auch Terme
+ Menge aller Formeln über V und Σ $F_{V,Σ}$
	+ Primformeln
		+ T und ⊥ sind Formeln
		+ Terme $t_1, t_2$ ==> $t_1=t_2$ ist Formel
		+ Relationen, welche Terme als Input bekommen, sind auch Formeln
	+ für jede Formel P ist jede Junktoren/Quantorenverknüpfung auch eine Formel
		+ ¬P
		+ ...
+ Menge der freien Variablen $FV(P)$ für $P∈F_{V,Σ}$
	+ P ist Primformel ==> $FV(P)$ = Menge aller Variablen in P
	+ $FV(P)=FV(¬P)$
	+ falls P und Q Formeln ==> $FV(P∧Q)=FV(P∨Q)=FV(P)∪FV(Q)$
	+ Variablen aus Quantoren sind gebundene Variablen
		+ ![](../../../z_images/Pasted%20image%2020220411110023.png)
	+ Beispiel: Vereinigung beider Mengen exklusive Quantoren 
		+ ![](../../../z_images/Pasted%20image%2020220411110344.png)

### Σ-Struktur und Σ-Modell
+ Σ-Struktur $Ä=(A,Σ)$ besteht aus Grundmengen A und Strukturmenge Σ für die gilt
	+ für jede Konstante $C∈Σ$ existiert $C^A∈A$
	+ für jede n-stellige Funktion $f∈Σ$ existiert $f^A: A^n$-->$A$
	+ für jede n-stellige Relation $R∈Σ$ existiert $R^A⊆A^n$
	+ ![](../../../z_images/Pasted%20image%2020220411112821.png)
+ Abbildung $ω: V$-->$A$ heißt Belegung
+  Σ-Modell $M=(Ä,ω)=M(A,Σ,ω)$
	+ Ä mit Belegung ω heißt Σ-Modell für $F_{V,Σ}$
	+ $∀P∈F_{V,Σ}$ wird Auswertung von P in M mithilfe von ω kanonisch definiert
		+ Auswertung $P^M$
	+ ![](../../../z_images/Pasted%20image%2020220411112231.png)



[[Aussagenlogische Formeln]]