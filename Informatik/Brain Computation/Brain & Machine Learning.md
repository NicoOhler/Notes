+ open questions about the brain based on regular [Machine Learning](../Machine%20Learning/Machine%20Learning.md)
	+ what is its objective function?
	+ what is its learning mechanism?
	+ how is credit assigned?
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
	+ synaptic eligibility traces as for [SNNs](Neuromorphic%20Computing/Spiking%20Neural%20Networks.md)
### Reinforcement Learning
+ well established [machine learning](../Machine%20Learning/Machine%20Learning.md) paradigm
+ approach
	+ fuck around and find out
	+ receive reward or punishment
	+ make beneficial actions more likely
	+ maximize future return
	+ ![](../../z_images/Pasted%20image%2020250618224654.png)
+ future return
	+ $G_t=\sum\limits_{k=0}\gamma^k R_{t+1+k}$
	+ prefer immediate rewards due to discount factor $\gamma$
+ choose action based on policy function $\pi(a|s)$
+ expected reward
	+ $V(s)=\mathbb{E}[G_t|S_t=s]$
+ temporal difference learning
	+ online learning rule
	+ $V(s_t)\rightarrow V(s_t) + \alpha [R_{t+1}+\gamma V(s_{t+1})-V(S_t)]$
	+ TD error
		+ updated expected reward - previously expected reward
		+ measure of surprise
			+ unexpected reward $\Rightarrow$ large error
			+ reward as expected $\Rightarrow$ small error
			+ no expected reward $\Rightarrow$ negative error
+ dopamine hypothesis
	+ neuromodulator dopamine encodes TD error
	+ released by dopaminergic neurons in midbrain
		+ global reward signal
	+ alters [synaptic](Neurons/Synapses.md) [plasticity](Plasticity/Plasticity.md)
+ three-factor rules
	+ neuromodulators gate [STDP](Plasticity/Spike-Timing%20Dependent%20Plasticity.md)
	+ $\Delta w \propto F_{pre}(S_{pre}) \times F_{post}(S_{post}) \times F_M([M])$
		+ functions of pre/postsynaptic activity $F_{pre},F_{post}$
		+ function of neuromodulator concentration $F_M$
+ brain performs rapid learning
	+ traditional RL/TD algorithms slow
	+ episodic memory
		+ decide on best action
		+ based on previous, similar experiences
		+ yielding highest expected reward
	+ meta-learning
		+ learn to learn fast
		+ slow RL via dopamine teaches prefrontal cortex to be fast RL agent
