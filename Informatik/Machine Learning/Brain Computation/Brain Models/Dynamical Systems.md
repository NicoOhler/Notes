+ mathematical models describing how a system changes over time
	+ $\frac{ds}{dt}=F(s)$
+ often used by [Brain Models](Brain%20Models.md)
### Equilibrium Points
+ fix points where states no longer change
+ types
	+ stable for $F'(s)\lt0$
		+ attractor
		+ stay there for small perturbations like noise
	+ unstable for $F'(s)\gt0$
		+ repeller
		+ move away for small perturbations like noise
	+ semi-stable for $F'(s)=0$
		+ saddle node bifurcation
			+ i.e. two fix points collide and cancel each other
			+ for this case an attractor and a repeller
		+ stay for one direction, move away for other
+ in reality noise will always slightly alter the state
	+ never settle at unstable point
	+ always jump over saddle nodes
+ 