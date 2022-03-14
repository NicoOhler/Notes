# Dreifachintegral
+ $R=[a_1,b_1]x[a_2,b_2]x[a_3,b_3]$
+ $\int\underset{R}\int\int f(x,y,z) dy dy dz =\int_{x=a_1}^{b_1}(\int_{x=a_2}^{b_2}(\int_{x=a_3}^{b_3}f(x,y,z)dz)dy)dx$
	+ andere Reihenfolgen auch möglich

### Normalbereich im R^3
+ $N={(x,y,z)∈ℝ^3|(x,y)∈M, g(x,y)≤z≤h(x,y)}$
+ $vol(N)=\int^d_{y=c}(\int^{φ(y)}_{x=ψ(y)}(\int_{z=g(x,y)}^{h(x,y)}dz)dx)dy$
+ Beispiel
	+ ![[Pasted image 20220314130508.png]]
	+ 