# Perceptron
### Perceptron Overview
+ [[Artificial Neural Networks]] neutron
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
+ ![[Pasted image 20220514133250.png]]

### PLA Properties
+ goes over set of examples
+ compares each example's output with desired output
+ weight changes based on correct output or not
+ convergence towards solution guaranteed if training set is linearly separable
+ may not find best solution, quality jumps around 
+ variants
	+ batch learning
		+ change weigths only after batch of training examples
		+ less quality jumps
	+ keep best seen solution in memory
	+ include optimization criteria
		+ maximizing distance of separation between both classes