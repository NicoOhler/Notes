+ $\tau_m\frac{du}{dt}=F(u)+R_mI(t)$
	+ $F(u)$ is an arbitrary, nonlinear function
+ reset to $u_{reset}$ for $u\ge\vartheta_{reset}$
+ analytical solution often do not exist
+ simulation via 1D [Dynamical Systems](Dynamical%20Systems.md)
### Quadratic Integrate-And-Fire Model
+ $F(u)=a_0(u-u_{reset})(u-u_c)$
	+ $u_c\sim\vartheta$ for short current pulse injection
		+ meaning?
+ parabola with roots (intersection with x-axis)
	+ shifted up/downwards depending on $I(t)$
	+ two equilibrium points
		+ stable point ($u_{rest}$ for $I(t)=0$)
	+ no intersection with x-axis causes
		+ potential to always increase followed by a reset
		+ repeated/tonic spiking
	+ 

### Exponential Integrate-And-Fire Model