### SRM
+ linear [neuron](../Neurons/Neurons.md) model as motivation 
	+ [LIF](../Brain%20Models/Leaky%20Integrate-And-Fire%20Model.md) model with [current-based](Synaptic%20Models.md) [synapses](../Neurons/Synapses.md)
	+ linear response to incoming spikes and currents
	+ reset mechanism expressed as subtraction
+ $u(t)=\eta(t-\hat t)+\sum\limits_j w_j \sum\limits_f \epsilon_j (t-\hat t, t-t^{(f)}) + \int_0^\infty \kappa(t-\hat t,s)I_{ext}(t-s)ds$
	+ time of last output spike $\hat t$ 
	+ reset-kernel $\eta$
	+ model response kernel $\epsilon$ to presynaptic spikes
	+ input kernel $\kappa$ for external current