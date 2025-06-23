### Motivation
+ inspired by the human brain
	+ spike-based
	+ asynchronous 
		+ without the need for clock signal
	+ independent and truly parallel
		+ i.e. no von Neumann bottleneck 
	+ local 
		+ i.e. everything needed is stored nearby
	+ energy efficient 
		+ e.g. our brain operates at ~20W and produces nearly no heat
### Neuromorphic Hardware
+ improves upon von Neumann architecture
	+ bottleneck due to data transfer over central bus
	+ ![](../../../z_images/Pasted%20image%2020250618131132.png)
+ uses low precision
	+ sparse due to spike-based nature
	+ allows for plenty of optimizations
		+ sparse matrices
		+ output = sum of weights for all spiking neurons
+ stochastic
+ utilizes feedback and recurrence
+ memory and processing combined
+ parallel
+ adaptive due to learning and [plasticity](../Learning/Plasticity.md) 
+ optimized for [Liquid State Machines](Liquid%20State%20Machines.md) and [SNNs](Spiking%20Neural%20Networks.md)
### Algorithms
+ deep learning with SNNs
	+ generic, well understood, generalizable
	+ training based
	+ energy efficient
	+ training difficult to implement on neuromorphic hardware
		1. train ANN offline on normal dataset and convert it to SNS
			+ mediocre results
			+ optional finetuning
		2. directly train SNN on special data
			+ good results
		3. train online via loss function and feedback
			+ good results
			+ weird and difficult to implement
+ unsupervised learning with biologically plausible learning rules
	+ adaptation hardware-friendly
	+ worse performance than regular deep learning
+ event-based sensing
	+ extremely efficient for both memory and compute
	+ ideal for low resource use cases such as edge computing 


