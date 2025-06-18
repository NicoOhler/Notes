### Reservoir and Liquid Computing
+ use recurrent [Spiking Neural Network](Spiking%20Neural%20Networks.md) to project input into high dimensional state space
+ assume a [Dynamical System](../Brain%20Models/Dynamical%20Systems.md) with single stable state (i.e. an attractor)
+ extract results using a simple readout 
	+ inputs from a select few neurons
	+ e.g. [Linear Regression](../../../Mathematik/Statistik/Regression/Lineare%20Regression.md)
	+ equivalent to complex, high dimensional feature transformation
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
+ maps inputs to high dimensional state space
+ ![](../../../z_images/Pasted%20image%2020250618092449.png)