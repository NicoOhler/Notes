+ linear [neuron](../Neurons/Neurons.md) model as motivation using [LIF](../Brain%20Models/Leaky%20Integrate-And-Fire%20Model.md) neurons with [current-based](../Synapses%20&%20Plasticity/Conductance%20&%20Current-Based%20Synapses.md) [synapses](../Synapses%20&%20Plasticity/Synapses.md)
	+ linear response to incoming spikes and currents
	+ reset mechanism expressed as subtraction
+ $u(t)=\eta(t-\hat t)+\sum\limits_j w_j \sum\limits_f \epsilon_j (t-\hat t, t-t^{(f)}_j) + \int_0^\infty \kappa(t-\hat t,s)I_{ext}(t-s)ds$
	+ time of last output spike $\hat t$ 
	+ reset-kernel $\eta$
	+ model response kernel $\epsilon$ to presynaptic spikes
	+ input kernel $\kappa$ for external current
+ common variants
	+ simplified SRM$_0$
		+ no dependency on last spike except for reset
		+ $u(t)=\eta(t-\hat t)+\sum\limits_j w_j \sum\limits_f \epsilon_j (t-t^{(f)}_j) + \int_0^\infty \kappa(s)I_{ext}(t-s)ds$
	+ cumulative SRM
		+ $u(t)=u_{rest} + \sum\limits_f\eta(t-t^{(f)})+\sum\limits_j w_j \sum\limits_f \epsilon_j (t-\hat t, t-t^{(f)}_j) + \int_0^\infty \kappa(t-\hat t,s)I_{ext}(t-s)ds$
		+  adaptation and bursting effects via cumulative effect of all past spikes
		+ SRM depression example
			+ reduce membrane potential on spike
			+ exponential decay with $\eta(t)=-A e^{\frac{-t}{\tau_{decay}}}$
				+ only noticeable for short time periods
				+ membrane potential normalizes over time
			+ subsequent spikes in short time period
				+ reduction overlaps
				+ larger inputs needed for spiking
+ spikes occur on crossing of variable threshold $\Theta(t)$ 
	+ $\Theta(t)=\Theta_0+\sum\limits_f\Theta_1(t-t^{(f)})$
	+ threshold kernel $\Theta_1$
