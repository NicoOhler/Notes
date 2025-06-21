+ $F(u)=-(u-E_L)+\Delta_T exp(\frac{u-\vartheta_{rh}}{\Delta_T})$
	+ linear term dominates for $u\ll \vartheta_{rh}$
	+ exponential dominates for $u\approx \vartheta_{rh}$
+ parameters
	+ rheobase current $I_{rh}$
		+ smallest constant current which causes spiking
	+ threshold at rheobase $\vartheta_{rh}$
		+ voltage at injection of $I_{rh}$
	+ steepness parameter $\Delta_T$
		+ converges to [Leaky Integrate-And-Fire Model](Leaky%20Integrate-And-Fire%20Model.md) for $\Delta_T \rightarrow 0$
+ advantages
	+ realistic compared to [Leaky Integrate-And-Fire Model](Leaky%20Integrate-And-Fire%20Model.md)
	+ way simpler than [Hodgkin-Huxley Model](Hodgkin-Huxley%20Model.md) allowing for easy parameter fitting
	+ decent reproduction of recorded spike trains
+ $I=0pA$
	+ semi-stable for at $\vartheta_{rh}$ for $I\gg0pA$
	+ ![](../../../z_images/Pasted%20image%2020250621075853.png)