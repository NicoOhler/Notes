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
		+ stable point
			+ at $u_{rest}$ for $I(t)=0$
		+ unstable point
			+ at $u_{c}$ for $I(t)=0$
	+ no intersection with x-axis causes
		+ potential to always increase followed by a reset
		+ repeated/tonic spiking
	+ ![](../../../../z_images/Pasted%20image%2020250616140856.png)

### Exponential Integrate-And-Fire Model
+ $F(u)=-(u-E_L)+\Delta_T exp(\frac{u-\vartheta_{rh}}{\Delta_T})$
	+ linear term dominates for $u\ll \vartheta_{rh}$
	+ exponential 