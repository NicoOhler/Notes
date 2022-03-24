# Gruppen, Halbgruppen und Untergruppen
### Halbgruppen
+ Menge X zusammen mit binärer Operation \* (X,\*)
	+ X≠∅
	+ heißt Halbgruppe, wenn assoziativ <==> $(x*y)*z=x*(y*z)$ $∀x,y,z∈X$
		+ ![[Pasted image 20220319103800.png]]
	+ Halbgruppe kommutativ, wenn $x*y=y*x$ $∀x,y∈X$
	+ neutrales Element e bzgl. \*, wenn 
		+ $x*e=e*x=x$ $∀x∈X$
		+ Halbgruppe mit neutralem Element heißt Monoid
+ Monoid (X,\*) mit neutralem Element e
	+ y ist inverses Element zu x, wenn
		+ $x*y=y*x=e$

### Gruppen
+ (X,\*) heißt Gruppe, wenn
	+ \* assoziativ
	+ $∃!$ neutrales Element
	+ $∀x∈X$ besitzt inverses Element $x^{-1}∈X$

### Untergruppen
+ H ⊆ G
	+ H≠∅
	+ (H,\*) ist Untergruppe von G(,\*)
		+ falls (H,\*) auch eine Gruppe ist
			+ Assoziativität muss nicht erneut bewiesen werden
			+ neutrale und inverses Element hingegen schon
			+ Binäroperation muss abgeschlossen sein
				+ ähnlich wie [[Untervektorräume]]
