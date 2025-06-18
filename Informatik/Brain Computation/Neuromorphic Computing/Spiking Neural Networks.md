### Network Modeling Approaches
+ feed forward
	+ not ideal
	+ feedback from higher levels required
	+ to minimize surprise
+ recurrent
	+ biologically plausible
	+ automatically incorporates information from higher levels
### Spiking Neural Networks
+ high-dimensional [dynamical system](../Brain%20Models/Dynamical%20Systems.md)
	+ individual [differential equation](../../../Mathematik/Analysis/Differentialgleichungen/Differentialgleichungen.md) per neuron
	+ linked via synaptic interplay
+ network of [LIF](../Brain%20Models/Leaky%20Integrate-And-Fire%20Model.md) [neurons](../Neurons/Neurons.md)
+ trained with special version of backpropagation
	+ replacing Heaviside step function with awful gradient
		+ $\Theta(t)=\begin{cases} 1 & \text{for }t \ge 0 \\ 0 & \, \text{for }t \lt 0\end{cases}$
		+ $\frac{d\Theta(t)}{dt}=\begin{cases} \infty & \text{for }t = 0 \\ 0 & \, \text{otherwise }\end{cases}$
	+ by surrogate pseudo derivative
		+ e.g. $g(x)=\gamma \,\text{max}(0,1-|x|)$
+ extends to 
	+ recurrent spiking neural networks (RSNNs)
		+ mediocre performance
	+ long-short term memory (LSNNs)
		+ some neurons exhibit adaptation
		+ perform exceptionally
+ using backpropagation through time (BPTT)
	+ ![](../../../z_images/Pasted%20image%2020250618134044.png)
	+ implementation on neuromorphic hardware requires eligibility traces
		+ $\frac{dE}{dw_{ij}}\approx\sum\limits_t\vb{}{L}_j^t \, \vb{e}^t_{ij}$
		+ $\boldmath $a$$
		+ 
		+ ![](../../../z_images/Pasted%20image%2020250618134324.png)
	+ 
