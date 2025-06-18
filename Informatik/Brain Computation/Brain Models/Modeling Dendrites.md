### Motivation
+ dendrites impact [neurons](../Neurons/Neurons.md) via spatiotemporal filtering and active effects
	+ neurons extend spatially
		+ dendrites more than 99% of neuron's surface
	+ different compartments connected to different brain regions
	+ ![](../../../z_images/Pasted%20image%2020250618140034.png)
+ distance to soma impacts action potential via passive and active effects
	+ see below
+ point neuron models are incapable of
	+ logical operations on inputs
		+ dendritic tree corresponds to cascade of logical operations
	+ low pass filter and attenuation
	+ coincidence detection
		+ i.e. simultaneously bAP + input + channel behavior
	+ segregation and amplification
		+ i.e. strong local input $\Rightarrow$ dendritic spike $\Rightarrow$ nonlinear amplification
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
### Passive Dendrites Properties
+ spatiotemporal filtering
	+ current propagates towards soma but also away
	+ currents leak through membrane
	+ decay and delay
		+ distal input and backpropagated AP may not reach soma
+ modeled via cable equation
	+ ![](../../../z_images/Pasted%20image%2020250618140613.png)
	+ ![](../../../z_images/Pasted%20image%2020250618140624.png)
	+ solution
		+ ![](../../../z_images/Pasted%20image%2020250618140641.png)
		+ distance-dependent attenuation
			+ exponential decay with length constant $\lambda$
			+ depends on diameter $a$
				+ large $a\Rightarrow$ slow decay, small amplitude
### Active Dendrites Effects
+ nonlinear signal processing arises from [ion channels](../Neurons/Ion%20Channels.md)
	+ e.g. potential above threshold causes channels to open
+ action potential typically increases bAP
	+ which boosts passive propagation
+ dendritic spikes
	+ chain reaction of many nearby channels opening
		+ results in large all or nothing effects
	+ highly dependent on channel density
		+ complexity arises from varying densities for different neuron types
	+ sodium spikes
		+ small amplification 
		+ longer duration than somatic spikes
	+ calcium spikes 
		+ lead to very long plateaus 
		+ up to several 100 ms
		+ evoked by simultaneous bAP and local input
