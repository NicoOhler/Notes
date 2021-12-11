# Unitäre Räume
+ unitärer Raum, wenn Skalarprodukt und Norm gilt
	+ siehe unten
+ 

### Skalarprodukt <v,w>
+ Inneres Produkt $<x,y>=x_1 y_1+...+x_n y_n$
	+ Winkel
	+ Orthogonalität
+  Definitheit: 
	+  $<v,v> > 0$, wenn v ≠ 0
+  $<v,w>=<w,v>$
	+  konjugiert komplexe Zahl
+  Linearität im ersten Argument
	+  $<λv,w>=λ<v,w>$
		+  $<v,λw>=\overrightarrow{<λv,w>}=\overrightarrow{λ<v,w>}=\overrightarrow{λ}\overrightarrow{λ}$
	+  $<v+v',w>=<v,w> + <v',w>$
	+  jedoch nicht im zweiten Argument
	+  je nach Definition auch nur im zweiten Argument möglich
 
### Norm ||x||
+ synonym mit Betrag oder Länge
+ $||x||=\sqrt{x_1^2+...+x_n^2}=\sqrt{<x ,x>}$
+ Definitheit
	+ $||v||=0$<==>$v=0$
+ Homogenität
	+ $||λv||=|λ|*||v||$
+ Dreiecksungleichung
	+ $||v+w||≤||v||+||w||$
+ $||v||=1$ ==> v ist normiert bzw. Einheitsvektor
	+ Normieren von $v$ ==> $v'=\frac{1}{||v||} * v$
+ Abstand $d(v,w);=||v-w||$
+ Alternative Normen
	+ 1-Norm $||x||_1=|x_1|+...+|x_n|$	
		+ Betragsnorm = Manhattan Norm/Taximetrik
	+ m-Norm $||x||_m=\sqrt[m]{x_1^m+...+x_n^m}$	
	+ Max-norm $||x||_\infty=max\{|x_1|+...+|x_n|\}$