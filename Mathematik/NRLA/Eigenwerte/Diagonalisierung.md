+ A ist diagonalisierbar, wenn A n l. u. EV besitzt
	+ ONB aus EV bilden
	+ $S=(v_1,...,v_n)$
		+ EV als Spalten eintragen
	+ $S^{-1}=S^T$
		+ $S^{-1}S=S^TS=(<v_i,v_j>)=δ_{ij}$ - [[Kronecker-Delta]]
	+ $AS=(Av_1,...,Av_n) = (λ_1v_1,...,λ_nv_n)$
		+ $S^{-1}AS=$ Matrix mit EV in Hauptdiagonale sonst nur 0
		+ ![[../../../z_images/Pasted image 20220105150102.png]]
		+ diese Matrix ist ähnlich zu A
+ $A^{n×n}$ ist diagonalisierbar, wenn $D=S^{-1}AS$
	+ D Diagonalmatrix
	+ EW von D sind Hauptdiagonalelemente
+ wird S aus EV von gebildet, dann gilt auch $D=S^{-1}AS$
	+ jedoch ist Inverse berechnen mühsamer

### Spektralsatz  der lin. Alg.
 + $A∈ℝ^{n×n}$ symmetrisch $(A=A^T)$==>
	 + alle [[Eigenwerte]] sind reell
	 + EV zu verschiedenen EW sind orthogonal
	 + A besitzt n orthonormierte EV
	 + A ist diagonalisierbar mittels ONB von EV (Orthonogale Diagonalisierung)
 + das übliche innere Produkt wird verwendet
	 + $<v,ww>:=\sum_{j=i}^n v_j\bar w_j$
 + Q heißt Orthogonalmatrix, wenn $Q^{-1}=Q^T$
 + $A∈ℝ^{n×n}$  ist orthogonal, wenn Spalten eine ONB bilden

### Bestimmung der diagonalisierenden Matrix Q
1. EW bestimmen
2. Basis der Eigenräume von A bestimmen
3. [[Orthonormieren nach GRAM-SCHMIDT]] wenn nötig
4. Spalten von Q sind ONB Eigenvektoren von 3.

