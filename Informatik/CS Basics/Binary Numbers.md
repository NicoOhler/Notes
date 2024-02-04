### Two's Complement
+ most significant bit is 1 if negative
+ over/underflow as side effect
+ ![[../../z_images/Pasted image 20221014124832.png]]
+ subtraction equal to addition due to overflow
	+ ![[../../z_images/Pasted image 20221014125043.png]]
+ negation
	+ flipping MSB
	+ add 1
	+ ![[../../z_images/Pasted image 20221014125408.png]]

### Sign Extension
+ required to add different sized numbers
	+ ![[../../z_images/Pasted image 20221014125702.png]]
+ fill up bits left of MSB with MSB
	+ ![[../../z_images/Pasted image 20221014125807.png]]

### Rational Numbers
+ LSB represent fractions of 2
	+ ![[../../z_images/Pasted image 20221014125943.png]]
	+ ![[../../z_images/Pasted image 20221014125957.png]]

### Multiplication and Division by the base
+ multiplication by left shift
+ division
	+ Arithmetic Shift Right
		+ shift right
		+ prior MSB as new MSB
	+ Logic Shift Right
		+ shift right
		+ 0 as new MSB 
