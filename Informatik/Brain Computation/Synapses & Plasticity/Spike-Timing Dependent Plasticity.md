+ long term [plasticity](Plasticity.md) based on relative spike timing $\Delta_t=t_{post}-t_{pre}$ 
	+ according to [Hebbian Learning](Hebbian%20Learning.md)
	+ $\Delta_t$ determines sign and magnitude of weight change
	+ usually $\Delta_t \gt 0 \Rightarrow$ potentiation
		+ anti-Hebbian STDP also exists
+ modeled via eligibility traces
	+ $\Delta w(\Delta_t)=\begin{cases} \eta (1-w)^{\mu_+}exp(\frac{-\Delta t}{\tau_{+}}) & \text{for }\Delta_t \ge 0 \\ -\eta\alpha w^{\mu_-}exp(\frac{-\Delta t}{\tau_{-}}) & \, \text{for }\Delta_t \lt 0\end{cases}$
	+ learning rate $\eta$
	+ relative size $\alpha$ between the two cases
+ interplay of excitation and inhibition ensures system stability
	+ otherwise weights could grow infinitely
+ fails for distal synapses since bAP decays 
	+ [[Clopath Learning]] provides an alternative
