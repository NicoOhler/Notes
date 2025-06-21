+ mathematical models describing how a system changes over time
	+ $\frac{ds}{dt}=F(s)$
+ often used by [brain models](Brain%20Models.md)
### Equilibrium Points
+ fix points where states no longer change
+ types
	+ stable for $F'(s)\lt0$
		+ attractor
		+ stay there for small perturbations like noise
		+ ![](../../../../z_images/Pasted%20image%2020250616130918.png)
	+ unstable for $F'(s)\gt0$
		+ repeller
		+ move away for small perturbations like noise
		+ ![](../../../../z_images/Pasted%20image%2020250616130931.png)
	+ semi-stable for $F'(s)=0$
		+ saddle node bifurcation
			+ i.e. two fix points collide and cancel each other
			+ for this case an attractor and a repeller
		+ stay for one direction, move away for other
		+ ![](../../../../z_images/Pasted%20image%2020250616130944.png)
+ in reality noise will always slightly alter the state
	+ never settle at unstable point
	+ always jump over saddle nodes
### 2D Dynamical Systems
+ can be represented in an x/y plane
	+ $\dot x=0$ at x-nullcline
	+ $\dot y=0$ at y-nullcline
+ equilibrium points at $\dot x=\dot y=0$
	+ intersection of nullclines
	+ attractors, repellers and saddle nodes still exist
	+ behavior depends on [eigenvalues](../../../../Mathematik/NRLA/Eigenwerte/Eigenwerte.md) of Jacobian (see [complex analysis](../../../../Mathematik/Analysis/Komplexe%20Analysis/Komplexe%20Analysis.md))
		+ $det(A-\lambda I)=0$
		+ real with mixed signs $\Rightarrow$ saddle node
		+ real and negative $\Rightarrow$ attractor
		+ real and positive $\Rightarrow$ repeller
### High-Dimensional Dynamical Systems
+ stable point attractors
+ stable periodic motions due to multiple attractors
	+ initial chaos settles into order after transient phase
+ ongoing a periodic motion
+  chaos
	+ confined subspace
	+ deterministic
	+ only short term predictions possible
	+ infinite transient phase
	+ quantifiable via Lyapunov exponent $\lambda$
		+ $||\delta(t)||\approx ||\delta_0(t)||e^{\lambda t}$
		+ $\lambda > 0 \iff$chaos
		+ $\lambda \approx 0, \lambda < 0 \iff$edge of chaos
