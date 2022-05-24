# Matching
### Matching
+ Matching in G ist Menge M⊆E, sodass jeder Knoten höchstens eine Kante von M berührt
+ ![[Pasted image 20220513211821.png]]
+ ![[Pasted image 20220513211946.png]]
+ Matching ist perfekt, wenn jeder Knoten gematcht ist
	+ $|M|=\frac{|V|}{2}$
	+ größtmögliches Matching

### Satz von Hall
+ bipartite Graph G
	+ ![[Pasted image 20220513212219.png]]
+ G hat Matching, wenn $N(S)≥|S|$ für $∀S⊆A$
	+ ![[Pasted image 20220513212531.png]]
+ Pfad $P=(x_0,e_1,x_1,e_2,x_2,...,e_n,x_n)$ alternierend bzgl. M, wenn
	+ $x_0$ ungematcht:
		+ $e_i∈M$ für gerade i
		+ $e_i∉M$ für ungerade i
+ P ist augmentierend bzgl. M, wenn
	+ alternierend 
	+ letzte Knoten $x_kn$ ungematcht
	+ $M'=M△E(P)=(M/E(P))∪(E(P)/M)$ symmetrische Differenz
		+ Matching mit einer Kante mehr als M
		+ ![[Pasted image 20220524123037.png]]
+ falls M nicht größtmöglich ==> augmentierender Pfad existiert