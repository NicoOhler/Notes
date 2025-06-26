### Conductance-based Synapses
+ focus on modeling the conductance instead of the current
+ $I_{syn}(t)=-g_{syn}(t)(u(t)-E_{syn})$
	+ neurotransmitters open [ion channels](../Neurons/Ion%20Channels.md) 
		+ influence conductance and thus also the current
		+ voltage dependency due to gating mechanism
	+ excitatory for large $E_{syn}$
	+ inhibitory for small $E_{syn}$
+ presynaptic spikes cause transient change in $g_{syn}​(t)$
	+ superposition of changes from previous spikes
	+ $g_{syn}​(t)=\bar g_{syn}​(t) \sum\limits_f \alpha(t-t^{(f)})$
	+ $\alpha(t)$ represent stereotypical time dependent changes
		+ delta, rectangular, exponential, alpha, double exponential
### Current-based Synapses
+ focus on directly modeling the current
+ $I_{syn}(t)=w_{syn}\sum\limits_f \alpha(t-t^{(f)})$
	+ 