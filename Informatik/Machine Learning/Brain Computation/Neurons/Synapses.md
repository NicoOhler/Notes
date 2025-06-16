### Electrical Synapses
+ common throughout the brain
+ neglected in most [Brain Models](../Brain%20Models/Brain%20Models.md)
+ electrical transmission via gap junctions
	+ i.e. connection between two membranes
+ transmission characteristics
	+ bidirectional
		+ neurons influence each other
	+ rapid, basically instantaneous
	+ continuous and independent of action potential?
		+ strong coupling and synchronization?

### Chemical Synapses
+ common throughout the brain and used by most models
+ electrical signal from axon causes chemical transmission at synapse which causes electrical signal at dendrite
+ slow, unidirectional transmission
	+ presynaptic activity influences postsynaptic neuron
+ transmission sequence
	1. action potential arrives at presynaptic terminal (axon end)
	2. depolarization open $Ca^{2+}$ channels
	3. $Ca^{2+}$ enters presynaptic terminal and triggers synaptic vesicles 
		+ containers full of neurotransmitter cocktails
	4. synaptic vesicles fuse with membrane
		+ neurotransmitters released into synaptic cleft
	5. diffusion with [Ion Channels](Ion%20Channels.md) on postsynaptic side
	6. postsynaptic conductance change causes postsynaptic current 
		+ $I_{syn}(t)=-g_{syn}(t)(u(t)-E_{syn})$ 
		+ excitatory (e.g. glutamate) or inhibitory effect (e.g. GABA)
	7. current causes postsynaptic potential
		+ $C_m\frac{du}{dt}=-g_{L}(u(t)-u_{rest}) + I_{syn}(t)$ 
+ Dale's principle
	+ neurons perform same chemical action at all their outgoing synapses
	+ thus neurons either excitatory or inhibitory
+ neurotransmitter release is stochastic
	+ probability depends on pre/postsynaptic factors such as
		+ recent activity
		+ long term [Plasticity](Plasticity.md)
		+ homeostasis
	+ multiple release sites per synapse
		+ $\Rightarrow$ postsynaptic potential varies
		+ synaptic weight = average
+ neuromodulators
	+ chemicals regulating neuron properties
		+ excitability
		+ plasticity
	+ difference to neurotransmitter
		+ slow acting
		+ widespread and diffuse
		+ alters neuron properties instead of sending them signals
