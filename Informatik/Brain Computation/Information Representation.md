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
	+ assumes trulyhomogeneous population which do not exist
+ 
