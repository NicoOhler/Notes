### Leaky Integrate-And-Fire Model
+ extreme simple neuron model
+ ![](../../../../z_images/Pasted%20image%2020250616112630.png)
+ $\tau_m \frac{du}{dt} = -(u(t)-u_{rest}) + R_m I(t)$ with $\tau_m = R_m C_m$
+ if $u(t) \ge \vartheta$
	+ spike
	+ reset to $u_{rest}$
### Derivation
+ Kirchhoff's law with $\sum \limits_j i_j = 0$
	+ $I(t) = i_C + i_R \implies i_C = -i_R + I(t)$
+ membrane acts as resistor with $u_R=R i_R$
	+ $i_R = \frac{u_r}{R} \implies i_C = -\frac{u_r}{R_m} + I(t)$
+ inside fluid acts as capacitance with $i_c=C \frac{du_c}{dt}$
	+ $i_C = C_m \frac{du_c}{dt} = -\frac{u_r}{R_m} + I(t)$
+ multiply with $R_m$ and insert the difference to the default resting potential
	+ $\tau_m = R_m C_m$ and $u_R=u(t)-u_{rest}$
	+ $\tau_m \frac{du}{dt} = -(u(t)-u_{rest}) + R_m I(t)$ with 


[40-Phys-ETTE-Elektrizitaet-Magnetismus-2022](../../../../Mathematik/Physik/40-Phys-ETTE-Elektrizitaet-Magnetismus-2022.pdf)