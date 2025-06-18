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
	+ replaces Heaviside step function with awful gradient
		+ $\Theta(t)=\begin{cases} 1 & \text{for }t \ge 0 \\ 0 & \, \text{for }t \lt 0\end{cases}$
		+ $\frac{d\Theta(t)}{dt}=\begin{cases} \infty & \text{for }t = 0 \\ 0 & \, \text{otherwise }\end{cases}$
	+ by surrogate
