+ biologically plausible [brain models](Brain%20Models/Brain%20Models.md) are hard to interpret
+ can we learn from regular [Machine Learning](../Machine%20Learning/Machine%20Learning.md) instead?
+ relation between ANNs and the brain
	+ brain and ANNs 
		+ overparameterized networks of simple, identical units
		+ hard to interpret
		+ perform well due to powerful learning algorithms
		+ sometimes use similar representations e.g. CNNs
	+ ANNs are slow learners, need tons of examples, humans fast
	+ ![](../../z_images/Pasted%20image%2020250618222057.png)
+ inductive biases
	+ bias towards simple solutions which make sense
	+ great for generalization
+ what is the brain's objective function? learning mechanism? how is credit assigned?
### Credit Assignment
+ define contribution of each neuron to output
+ requires feedback from output
+ neuron needs local information
	+ spikes
	+ neuromodulators
+ weight perturbation
	+ same feedback for all neurons?
	+ keep changes only if beneficial for objective
	+ slow improvements due to high variance
+ issues of backpropagation
	+ separate forward and backward pass required
	+ symmetric/same weights for forward and backward pass 
	+ feedback changes synaptic values, not activity?
	+ biologically unrealistic
+ alternatives to backpropagation
	+ ![](../../z_images/Pasted%20image%2020250618223853.png)
	+ synaptic eligibility traces as for [Spiking Neural Networks](Neuromorphic%20Computing/Spiking%20Neural%20Networks.md)

### Reinforcement Learning in the Brain