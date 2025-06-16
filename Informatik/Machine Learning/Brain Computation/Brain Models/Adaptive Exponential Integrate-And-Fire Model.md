### Motivation
+ some [Neurons](Neurons/Neurons.md) adapt their behavior
+ neuron types
	+ type I neurons increase their firing rate proportional to current
	+ type II neurons fire only at one specific frequency
	+ type III neurons fire once if the current is constant
	+ more complex behaviors also exist
+ ![](../../../../z_images/Pasted%20image%2020250616151154.png)
### Modeling Approaches
+ requires 2D [Dynamical Systems](Dynamical%20Systems.md)
	+ $\tau_m\frac{du}{dt}=F(u,w)+R_mI(t)$
	+ $\frac{dw}{dt}=g(u,w)$
+ idea
	+ model adaptation as current
	+ $\tau_m\frac{du}{dt}=F(u,w)-R_m w +R_mI(t)$
	+ $\tau_w\frac{dw}{dt}=g(u,w,S(t))$ with adaptation time constant $\tau_w$
### Adaptive Exponential IAF Model (AdEx)
+ add adaptation current $-R_m w$ to [Exponential Integrate-And-Fire Model](Exponential%20Integrate-And-Fire%20Model.md)
+ $\tau_w\frac{dw}{dt}=-w+a(u-u_{rest})+b \tau_w \sum\limits_f\delta(t-t^{(f)})$
	+ steady change via subthreshold adaptation
	+ incremental spike triggered adaptation
		+ i.e. $w\rightarrow w+b$ whenever a spike occurs
	+ usually steady converge to $u_{rest}$ due to $a>0$
+ adaptation parameters $a$
+ adaptation parameters $b$
	
	+ b
	+ $b<0\Rightarrow$ increased excitability after spikes
	+ $b>0\Rightarrow$ reduced excitability after spikes
+ $a=b=0\Rightarrow$ [Exponential Integrate-And-Fire Model](Exponential%20Integrate-And-Fire%20Model.md)

