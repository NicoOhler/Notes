### Reservoir and Liquid Computing
+ use complex [Dynamical System](../Brain%20Models/Dynamical%20Systems.md) to project input into high dimensional state space
+ assume a single stable state (i.e. an attractor)
+ extract results using a simple readout 
+ liquid filter performs simple high dimensional computation
	+ would be difficult in lower dimension
	+ basically complex feature transformation
+ water pool analogy
	+ initially in a stable state
		+ flat water surface 
	+ inputs cause transient deviation
		+ wind or pebbles cause waves and ripple effects
		+ waves diminish
		+ return to flat water surface
	+ extract knowledge about input by analyzing the new dynamics
		+ waves from east to west $\Rightarrow$ east wind
### Liquid State Machine
+ use liquid filter to map inputs to state space
	+ receives no training
	+ deterministic (i.e. same input same output)
+ followed by a readout
	+ receives snapshot of the liquid filter as input
		+ i.e. inputs from a select few neurons at certain time intervals
	+ trained to receive desired output
	+ simple models often sufficient for good results
		+ e.g. [Linear Regression](../../../Mathematik/Statistik/Regression/Lineare%20Regression.md)
+ requirements for arbitrary input-output mapping
	+ time invariant liquid filter
		+ fading memory
		+ always returns to stable state
	+ separation property
		+ different inputs yield different outputs
	+ approximation property
		+ readout capable of distinguishing states and mapping them to target?
### Implementation
+ liquid filter
	+ often a recurrent [Spiking Neural Network](Spiking%20Neural%20Networks.md) of [LIF](../Brain%20Models/Leaky%20Integrate-And-Fire%20Model.md) [neurons](../Neurons/Neurons.md)
+ ![](../../../z_images/Pasted%20image%2020250618092449.png)