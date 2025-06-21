+ $\tau_m\frac{du}{dt}=F(u)+R_mI(t)$
	+ $F(u)$ is an arbitrary, nonlinear function
+ reset to $u_{reset}$ for $u\ge\vartheta_{reset}$
+ analytical solution often do not exist
+ simulation via 1D [dynamical systems](Dynamical%20Systems.md)
+ examples
	+ [[Quadratic Integrate-And-Fire Model]]
	+ [[Exponential Integrate-And-Fire Model]]
### Fitting IAF Models
+ possible goals
	+ reproduce spike train $S(t)$ to fit recorded relationship $I(t) \rightarrow S(t)$
	+ reproduce subthreshold behavior $V(t)$ to fit recorded relationship $I(t) \rightarrow V(t)$
+ record $V(t)$ for known (injected) $I(t)$
	+ easy to construct $S(t)$ from $V(t)$
	+ in vitro unrealistic
	+ in vivo difficult
	+ add a little noise to mimic in vivo conditions
+ fit model with respect to metric using black-box optimization
	+ swarm optimization
	+ evolution
	+ ...