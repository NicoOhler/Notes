### Neural Codes
+ [information representation](../Data%20Science%20and%20AI/Knowledge%20Representation/Knowledge%20Representation.md) of the brain
	+ relationship between brain signal and contained information
+ learning stimuli to action mappings doable
	+ internal representation difficult
+ interpreting firing rate
	+ average spike count for a duration $T$
		+ $v=\frac{1}{T}N_{sp}(0,T)$ 
		+ problem: rapid stimuli change
		+ noisy and varying neural responses 
	+ peristimulus time histogram (PSTH)
		+ average over trials
		+ $v(t)=\frac{1}{M}\sum\limits_m\frac{1}{\Delta t}N_{sp,m}(t,t+\Delta t)$ 
		+ impossible to repeat experiments under identical conditions
		+ non-uniform processing
			+ i.e. process same situation differently
	+ spike timing also encodes information
		+ lost through averaging
### Population Codes
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
	+ ![](../../z_images/Pasted%20image%2020250618201412.png)
+ winner-take-all (WTA) dynamics
	+ only best matching neuron(s) fires
	+ suppress weakly activated neurons
	+ sparse response
	+ theoretical hard WTA corresponds to labeled line code
	+ realistic soft WTA corresponds to position code
+ examples
	+ neurons show preference for oriented bars
		+ ![](../../z_images/Pasted%20image%2020250618201911.png)
	+ concept cells
		+ ![](../../z_images/Pasted%20image%2020250618201934.png)
	+ place cells
		+ robust firing while at location
		+ ![](../../z_images/Pasted%20image%2020250618202006.png)