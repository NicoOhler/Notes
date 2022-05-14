# Artificial Neural Networks
### Human Neuron
![[Pasted image 20220508202902.png]]

### I/O Abstraction
+ similar to blackbox/function
+ ![[Pasted image 20220508202945.png]]

### McCulloch-Pitts Neuron
+ simplest neuron
+ binary input, binary output
+ output of 1 if sum of all input bits > threshold else 0
+ ![[Pasted image 20220508203103.png]]

### McCulloch-Pitts Neuron with Inhibitory Inputs
+ based on McCulloch-Pitts Neuron
+ two types of inputs
	+ normal inputs x
	+ inhibitory inputs y
+ one inhibitory input true ==> false
+ allows boolean logic
+ ![[Pasted image 20220508203606.png]]

### Perceptron
+ inputs are now real numbers instead of just true or false
+ each input has a certain weight
+ ![[Pasted image 20220508203903.png]]
+ perceptron networks allow non-linear separation

### Perceptron Learning Algorithm
+ ![[Pasted image 20220514131436.png]]
+ Variables:
	+ ![[Pasted image 20220514131522.png]]
+ Algorithm:
	+ ![[Pasted image 20220514132201.png]]
	+ correct guess ==> weights stay the same
	+ bad guess ==>
		+ output too small ==>
			+ increase weight at positive inputs
			+ decrease weight at negative inputs
		+  output too big ==>
			+ decrease weight at positive inputs
			+ increase weight at negative inputs
+ repeated until 
	+ average error below pre-defined threshold
	+ or after pre-determined number of iterations
