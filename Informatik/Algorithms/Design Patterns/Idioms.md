### Difference to other [[Types of Design Patterns]]
+ limited to a small scope instead of being widely applicable
+ rather specific, no general solution template

 >[!quote] Counted Pointer
> > [!tip] Core idea
> > + 
> 
> > [!success] Solution
UML

 >[!quote] Scoped Locking
> > [!tip] Core idea
> > + utilize language scope for locking
> > + automatically release acquired locks upon leaving scope
> 
> > [!success] Solution
![](../../../z_images/Pasted%20image%2020251229110349.png)

 >[!quote] Double Checked Locking
> > [!tip] Core idea
> > + check twice to ensure condition
> > 	+ once before locking, once after 
> > + avoid having to wait for lock if condition is anyway not met 
> 
> > [!success] Solution
![](../../../z_images/Pasted%20image%2020251229110502.png)
