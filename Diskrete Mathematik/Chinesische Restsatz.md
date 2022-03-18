# Chinesische Restsatz
+ gesucht Menge aller Lösungen x∈ℤ der simultanen Kongruenzen
	+  $x≡c_1$ mod $m_1$	 
	+  $x≡c_2$ mod $m_2$	
	+  ...
	+  $x≡c_n$ mod $m_n$
+  Vorgehensweise
	+  $m_1$ bis $m_n$ sind teilerfremd
		+  ansonsten redundante Kongruenzen eliminieren
	+  Produkt berechnen
		+ $M=\prod_{i=1}^n a_i$
	+ $M_i=\frac{M}{m_i}$
	+ euklidischen Alg. anwenden
		+ $a_i*m_i+b_i*M_i=1$
	+ Lösung
		+ $x=\sum_{i=1}^n x_i*s_i*Ai$