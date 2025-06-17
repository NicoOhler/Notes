+ theory for long term [plasticity](../Neurons/Plasticity.md) 
	+ if cell A repeatedly takes part in causing cell B to fire
	+ then the synaptic efficacy of A on B increases
	+ i.e. presynaptic spike before postsynaptic spike increases synaptic weight
+ fails to take depression into account
+ unidirectional
+ spike timing dependent plasticity STDP
	+ relative spike timing $\Delta_t=t_{post}-t_{pre}$ 
	+ $\Delta_t$ determines sign and magnitude of weight change
	+ usually $\Delta_t \gt 0 \Rightarrow$ potentiation
		+ anti-Hebbian STDP also exists
+ modeled via eligibility traces
	+ $\Delta w(\Delta_t)=\begin{cases} \eta (1-w)^{\mu_+}exp(\frac{-\Delta t}{\tau_{+}}) & \text{for }\Delta_t \ge 0 \\ 23 & \, \text{for }\Delta_t \lt 0\end{cases}$
