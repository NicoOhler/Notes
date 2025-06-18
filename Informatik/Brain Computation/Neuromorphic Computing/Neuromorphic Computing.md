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
### Neuromorphic Computing
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
+ adaptive due to learning 
