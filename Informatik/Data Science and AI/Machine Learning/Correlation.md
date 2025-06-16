### Correlation
+ describes to what extent two variables are related
+ does not immediately mean causality
	+ e.g. correlation between shark attacks and ice cream sales
		+ shark attacks do not cause ice cream sales
		+ ice cream sales do not cause ice cream sales
		+ both are caused by third variable summer/heat

### Pearson Correlation
+ correlation between two quantitive variables
+ ![](Pasted%20image%2020220523100513.png)
+ correlation coefficient r 
	+ describes strength of relation ship between X and Y
	+ r=-1: 
		+ perfect descending linear relationship
		+ high X <==> low Y
	+  0: 
		+ variables not systematically related
		+ high X <==> high or low Y
	+  1: 
		+ perfect ascending linear relationship
		+ high X <==> high Y
+  correlation threshold
	+ threshold depends on domain
	+ different for each use case
+  large population but small sample size
	+ likelihood of correlation within subset
	+ even though no correlation within whole population
	+ null hypothesis
	+ ![](Pasted%20image%2020220523101844.png)

### Linear Regression
+ approximates linear function between linearly correlated data
	+ $y=a+bx$
+ underlying assumption
	+ never know all data
	+ we just have training data
	+ keep part of data for testing afterwards
+ optimisation criterion
	+ method of least squares
	+ see [[NRLA]] script
	+ ![](Pasted%20image%2020220523102714.png)
	+ ![](Pasted%20image%2020220523102749.png)
	+ ![](Pasted%20image%2020220523102804.png)

### Other Types of Regression
+ non-linear regression - curve fitting
	+ fitting non-linear function to data
	+ ![](Pasted%20image%2020220523103022.png)
+ logistic regression
	+ fitting log function to continous independent data
	+ and dichotomous (zweigeteilt) out come data
	+ classification method

### Prediction with Correlation and Regression
+ estimate value $y_i$, given $x_i$ using regression line
	+ $y_i$ dependent outcome variable
	+ $x_i$ independent input variable

[[../../Machine Learning/Machine Learning]]
