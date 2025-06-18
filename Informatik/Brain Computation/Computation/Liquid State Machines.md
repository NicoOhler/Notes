### Liquid Computing
+ use recurrent [Spiking Neural Network](Spiking%20Neural%20Networks.md) to project input into high dimensional state space
+ assume a [Dynamical System](../Brain%20Models/Dynamical%20Systems.md) with single stable state (i.e. an attractor)
+ extract results using a simple readout 
	+ inputs from a select few neurons
	+ e.g. [Linear Regression](../../../Mathematik/Statistik/Regression/Lineare%20Regression.md)
	+ equivalent to complex, high dimensional feature transformation
+ water pool analogy
	+ flat water surface as stable state
	+ inputs such as wind or pebbles cause waves and ripple effects
	+ extract knowledge about input by analyzing the new dynamics
	+ transient deviation from stable state
		+ waves diminish
		+ return to flat water surface
	+ 