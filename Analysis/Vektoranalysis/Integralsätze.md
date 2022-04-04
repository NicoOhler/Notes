# Integralsätze
### Satz von Gauß in der Ebene
+ Sei C der Rand eines Bereichs B, der Normalbereich bezüglich beider Achsen ist
	+ ![[Pasted image 20220328151243.png]]
+ Rand von B
	+ ![[Pasted image 20220328151343.png]]
+ $\oint_{\partial B}Pdx+Qdy=\iint_B(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y})dx dy$
	+ muss vollständig definiert sein
	+ Bereich darf keine Löcher haben
+ Leibnizsche Sektorformel
	+ Fläche von B $\frac{1}{2}\oint_{\partial B} -ydx+xdy$
+ Beispiel:
	+ Integralsatz von Gauß nicht möglich, da undefiniert im Ursprung
	+ ![[Pasted image 20220404104341.png]]


### Integralsatz von STOKES
+ Vektorfeld von Fläche mit Rand bestimmen
	+ ![[Pasted image 20220404105041.png]]
+ Herleitung
	+ ![[Pasted image 20220404105446.png]]
	+  Variablensubstitution
		+  $x=x(u,v)$
		+  $y=y(u,v)$
		+  $z =z(u,v)$
		+ $dx=\frac{\partial x}{\partial u} du +\frac{\partial x}{\partial v} dv$
		+  $dy=\frac{\partial y}{\partial u} du +\frac{\partial y}{\partial v} dv$
		+ $dz=\frac{\partial z}{\partial u} du +\frac{\partial z}{\partial v} dv$
	+ ![[Pasted image 20220404105932.png]]
		+ 3D Flächenintegral wird zu 2D Kurvenintegral
		+ Gaußsche Integralsatz
		+ ...
+ $\oint_{\partial B} Pdx+Qdy+Rdz=\int\int_B(\frac{\partial R}{\partial y}-\frac{\partial Q}{\partial z})dy\textasciicircum{}dz+(\frac{\partial P}{\partial z}-\frac{\partial R}{\partial x})dz\textasciicircum{}dx+(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y})dx\textasciicircum{}dy$
+ $\oint_{\partial B} Pdx+Qdy+Rdz=\int\int_B rot(P,Q,R)d\overrightarrow{o}$
+ Orientierung des Normalvektors wird aus der Ebene übernommen

### Integralsatz von Gauß im Raum
+ $\oint\oint_{\partial B}\overrightarrow{V}d\overrightarrow{o}=\int\int\int_B div(\overrightarrow{o})dxdydz$
	+ $div(\overrightarrow{V})=\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}$
	+ Bereich darf keine Löcher haben

### Vektorfeld Eigenschaften
+ wirbelfrei, wenn Rotation Null
+ quellenfrei, wenn Divergenz Null

[[Oberflächenintegral]]