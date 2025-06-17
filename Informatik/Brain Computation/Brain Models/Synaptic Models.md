+ [Synaptic Transmissions](../Neurons/Synaptic%20Transmission.md) lead to postsynaptic potentials (PSPs)
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

TODO: this is a mess