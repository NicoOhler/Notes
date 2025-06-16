### Motivation
+ some [Neurons](Neurons/Neurons.md) adapt their behavior
+ neuron types
	+ type I neurons increase their firing rate proportional to current
	+ type II neurons fire only at one specific frequency
	+ type III neurons fire once if the current is constant
	+ more complex behaviors also exist
+ ![](../../../../z_images/Pasted%20image%2020250616151154.png)
### Modeling Adaptation Behavior
+ requires 2D [Dynamical Systems](Dynamical%20Systems.md)
+ approach 1
	+ $\tau_m\frac{du}{dt}=F(u,w)+R_mI(t)$
	+ $\frac{dw}{dt}=g(u,w)$
+ approach 2 modeling adaptation as current
	+ $\tau_m\frac{du}{dt}=F(u,w)-R_m w +R_mI(t)$
	+ $\tau_w\frac{dw}{dt}=g(u,w,S(t))$
		+ $\tau_w$...adaptation time constant
		+ 


