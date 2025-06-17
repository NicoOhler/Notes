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
+ behaviors
	+ stable point attractors
	+ stable periodic motions due to multiple attractors
		+ initial chaos settles into order after transient phase
	+ ongoing a periodic motion
+  chaos
	+ confined subspace
	+ deterministic
	+ only short term predictions possible
	+ infinite transient phase
	+ quantifiable via Lyapunov exponent
		+ $||\delta(t)||\approx ||||e^{\lambda$