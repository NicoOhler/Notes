### Motivation
+ [synaptic transmissions](Synaptic%20Transmission%20of%20Chemical%20Synapses.md) lead to postsynaptic potentials (PSPs)
+ some [ion channels](../Neurons/Ion%20Channels.md) have nonlinear voltage dependencies
	+ $I_{syn}(t)=-g_{syn}(t)\gamma(u(t))$
### Conductance-based [Synapses](Synapses.md)
+ focus on modeling the conductance instead of the current
	+ biologically plausible
+ $I_{syn}(t)=-g_{syn}(t)(u(t)-E_{syn})$
	+ neurotransmitters open [ion channels](../Neurons/Ion%20Channels.md) 
		+ influence conductance and thus also the current
		+ voltage dependency due to gating mechanism
	+ amplitude scaled by $u(t)-E_{syn}$ 
		+ excitatory for large $E_{syn}$
		+ inhibitory for small $E_{syn}$
+ presynaptic spikes cause transient change in $g_{syn}​(t)$
	+ superposition of changes from previous spikes
	+ $g_{syn}​(t)=\bar g_{syn}​(t) \sum\limits_f \alpha(t-t^{(f)})$
	+ $\alpha(t)$ represent stereotypical time dependent changes
+ typical choices for $\alpha(t)$ 
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
### Current-based Synapses
+ focus on directly modeling the current
	+ simplification of conductance-based synapses
+ $I_{syn}(t)=w_{syn}\sum\limits_f \alpha(t-t^{(f)})$
	+ uses abstract synaptic weight
	+ constant amplitude
	+ does not rely on $u(t)$
	+ may grow infinitely