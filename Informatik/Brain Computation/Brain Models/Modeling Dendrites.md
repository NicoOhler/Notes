### Motivation
+ dendrites impact [neurons](../Neurons/Neurons.md) via spatiotemporal filtering and active effects
	+ are neuromodulators meant with active effects?
	+ neurons extend spatially
		+ dendrites more than 99% of neuron's surface
	+ different compartments connected to different brain regions
	+ ![](../../../z_images/Pasted%20image%2020250618140034.png)
+ distance to soma impacts action potential
	+ passive effects
		+ current propagates towards soma but also away
		+ currents leak through membrane
		+ decay and delay
			+ distal input and backpropagated AP may not reach soma
		+ modeled via cable equation
	+ active effects
		+ nonlinear signal processing
		+ [ion channels](../Neurons/Ion%20Channels.md)
		+ structural [plasticity](../Plasticity/Plasticity.md)
		+ ...
### Multi-Compartment models
+ idea
	+ divide dendrites into small cylindric volumes
	+ use separate [Hodgkin-Huxley Model](Hodgkin-Huxley%20Model.md) for each
	+ electrically connected and conductance between them
+ multiple abstraction levels down to point neuron model
	+ very realistic modeling of individual neurons
		+ ~200 compartments
		+ parameters fit to recordings
	+ simpler models use one compartment per branch
	+ ![](../../../z_images/Pasted%20image%2020250618135209.png)

### Cable Equation
+ ![](../../../z_images/Pasted%20image%2020250618140613.png)
+ ![](../../../z_images/Pasted%20image%2020250618140624.png)
+ solution
	+ ![](../../../z_images/Pasted%20image%2020250618140641.png)
	+ distance-dependent attenuation
		+ exponential decay with length constant $\lambda$
		+ depends on diameter $a$
			+ large $a\Rightarrow$ slow decay, small amplitude