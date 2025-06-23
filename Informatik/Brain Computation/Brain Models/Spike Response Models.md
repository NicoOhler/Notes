### Motivation
+ [synaptic transmissions](../Plasticity/Synaptic%20Transmission%20of%20Chemical%20Synapses.md) lead to postsynaptic potentials (PSPs)
+ some [ion channels](../Neurons/Ion%20Channels.md) have nonlinear voltage dependencies
	+ $I_{syn}(t)=-g_{syn}(t)\gamma(u(t))$
### Conductance-Based [Synapse](../Neurons/Synapses.md)
+ membrane conductance is superposition of individual input weighted by synaptic weight
	+ $g_{syn}(t)=\bar g_{syn} \sum_\limits f \alpha(t-t^{(f)})$
	+ $I_{syn}(t)=-g_{syn}(t)(u(t)-E_{syn})$ 
+ biologically plausible
+ typical choices for $\alpha$ 
	+ delta spike $\alpha(t)=\alpha(t)$
		+ simple
	+ rectangular shape $\alpha(t)=\Theta(t)-\Theta(t-\tau)$
		+ convenient
	+ exponential $\alpha(t)=exp(-\frac{t}{\tau_{decay}})\Theta(t)$
		+ simple but reasonable
	+ alpha $\alpha(t)= t exp(-\frac{t}{\tau_{decay}})\Theta(t)$
		+ very realistic
		+ slow onset
	+ double exponential $(exp(-\frac{t}{\tau_{decay}}) - exp(-\frac{t}{\tau_{rise}}))\Theta(t)$
		+ realistic 
		+ slow onset and decay
		+ way easier to implement
	+ ![](../../../z_images/Pasted%20image%2020250617095008.png)
### Current-Based Synapse
+ relation to others?
+ simplification using abstract synaptic weight
	+ $I_{syn}(t)=w_{syn}\sum_\limits f \alpha(t-t^{(f)})$
+ properties
	+ no reliance on $u(t)$
	+ may grow infinitely
	+ constant amplitude
### Spike Response Model (SRM)
+ linear [neuron](../Neurons/Neurons.md) model as motivation using [LIF](../Brain%20Models/Leaky%20Integrate-And-Fire%20Model.md) neurons with current-based synapses
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
