### Two's Complement
+ most significant bit is 1 if negative
+ over/underflow as side effect
+ ![](Pasted%20image%2020221014124832.png)
+ subtraction equal to addition due to overflow
	+ ![](Pasted%20image%2020221014125043.png)
+ negation
	+ flipping MSB
	+ add 1
	+ ![](Pasted%20image%2020221014125408.png)

### Sign Extension
+ required to add different sized numbers
	+ ![](Pasted%20image%2020221014125702.png)
+ fill up bits left of MSB with MSB
	+ ![](Pasted%20image%2020221014125807.png)

### Rational Numbers
+ LSB represent fractions of 2
	+ ![](Pasted%20image%2020221014125943.png)
	+ ![](Pasted%20image%2020221014125957.png)

### Multiplication and Division by the base
+ multiplication by left shift
+ division
	+ Arithmetic Shift Right
		+ shift right
		+ prior MSB as new MSB
	+ Logic Shift Right
		+ shift right
		+ 0 as new MSB 
