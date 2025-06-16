+ biologically plausible
+ models currents received via voltage-gated [Ion Channels](../Neurons/Ion%20Channels.md)
	+ $I_{ion} = -g_{ion} (V-E_{ion}) p_{ion}(V)$
	+  depends on the fraction of open channels $p_{ion}(V)$
		+ $p_{ion}(V)=a_{ion}^A(V)b_{ion}^B(V)$
			+ a...activation
			+ b...inactivation
			+ A...number of gating events needed for activation
			+ B...number of gating events needed for inactivation
		+ parameters representing the channel dynamics fit to data
+ $C_m \frac{du}{dt}=-g_L(V-E_L)+\sum_\limits\text{ion types} -g_{ion}(V-E_{ion})p_{ion}(V) + I_{ext}$
+ simulation via numerical integration
	+ Euler's Method
	+ Zero-Order Hold
+ complex and computationally expensive
	+ need for simplification
### Simplification Approaches
+ neglecting ion types with minor contributions
	+ i.e. model only sodium and potassium
+ combine into single ionic current $I_{fast}$
	+ $C_m \frac{du}{dt}=-g_L(V-E_L)-g_{fast}(V-E_{fast})p_{fast}(V) + I_{ext}$
	+ express $p_{fast}(V)$ as constant 
		+ reduce differential equation to constant
