+ [Synaptic Transmissions](../Neurons/Synaptic%20Transmission.md) lead to postsynaptic potentials (PSPs)
+ simplified model
	+ membrane conductance is superposition of individual input weighted by synaptic weight
	+ $g_{syn}(t)=\bar g_{syn} \sum_\limits f \alpha(t-t^{(f)})$
+ typical choices for $\alpha$ 
	+ delta spike $\alpha(t)=\alpha(t)$
		+ simple
	+ rectangular shape $\alpha(t)=\Theta(t)-\Theta(t-\tau)$
		+ convenient
	+ exponential $\alpha(t)=exp(-\frac{t}{\tau_{decay}})\Theta(t) $
		+ simple but reasonable
	+ alpha $\alpha(t)= t exp(-\frac{t}{\tau_{decay}})\Theta(t)$
		+ very realistic
	+ double exponential $(exp(-\frac{t}{\tau_{decay}}) - exp(-\frac{t}{\tau_{rise}}))\Theta(t)$
		+ realistic but easier
	+ ![](../../../z_images/Pasted%20image%2020250617095008.png)