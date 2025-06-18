+ estimate time-varying firing rate of whole [neuron](Neurons/Neurons.md) population
+ population rate
	+ $A(t)=\frac{1}{N}\sum\limits_n\frac{1}{\Delta t}N_{sp,n}(t,t+\Delta t)$ 
	+ instantaneous average over many neurons
	+ robust estimate without need to repeat trials
	+ truly homogeneous populations do not exist
+ collaborative encoding through individual activity
	+ i.e. construct signal vector instead of average
	+ train linear decoder on activity vectors
+ neurons have receptive fields
	+ i.e. responsible for certain stimulus range
	+ continuous position code for overlaps
	+ discrete labeled line code for 1:1 mapping of neuron to value range
	+ ![](../../../z_images/Pasted%20image%2020250618201412.png)
+ winner-take-all (WTA) dynamics
	+ only best matching neuron(s) fires
	+ suppress weakly activated neurons
	+ sparse response
	+ theoretical hard WTA corresponds to labeled line code
	+ realistic soft WTA corresponds to position code
+ distributed encoding
	+ decode information from joint activity of several neurons
	+ possible even if all neuron show non-specific responses
+ examples
	+ neurons show preference for oriented bars
		+ ![](../../../z_images/Pasted%20image%2020250618201911.png)
	+ concept cells
		+ neurons associated with everything "Luke Skywalker" related
		+ ![](../../../z_images/Pasted%20image%2020250618201934.png)
	+ place cells
		+ robust firing while at location
		+ red boxes are not location selective
		+ ![](../../../z_images/Pasted%20image%2020250618202006.png)