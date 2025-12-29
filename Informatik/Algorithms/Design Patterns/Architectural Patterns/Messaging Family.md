 >[!quote] Messages
> > [!tip] Core idea
> > + encapsulate information in a standardized way
> 
> > [!success] Solution
![](../../../../z_images/Pasted%20image%2020251229094726.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + combine data and metadata in explicitly defined format/protocol
> > > + enclosed packet instead of continuous data stream 
> >
> >> [!failure] Bad
> >> + computation overhead due to (de)serialization
> >> + communication overhead due to protocol
> >> + costlier changes and new versions
> >> + format must be well defined and respected

 >[!quote] Message Endpoint
> > [!tip] Core idea
> > + provide functionality to send and receive messages
> 
> > [!success] Solution
![](../../../../z_images/Pasted%20image%2020251229095259.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + endpoint handles message conversion
> > > + decouples external messaging from internal communication
> > > + separation of concerns
> >
> >> [!failure] Bad
> >> + additional performance overhead and abstraction
> >> + potentially a single point of failure or bottleneck

 >[!quote] Request-Response
> > [!tip] Core idea
> > + answer every request with a response
> 
> > [!success] Solution
![](../../../../z_images/Pasted%20image%2020251229095618.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + enables timeout detection, windowing and buffered responses
> > > + two decoupled communication events: question and answer
> >
> >> [!failure] Bad
> >> + no continuous data stream, broad or multicasting?
> >> + async is difficult to debug
> >> + requires error handling (e.g. error response or no response)

 >[!quote] Messages
> > [!tip] Core idea
> > + encapsulate information in a standardized way
> 
> > [!success] Solution
![](../../../../z_images/Pasted%20image%2020251229094726.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + 
> >
> >> [!failure] Bad
> >> + 

 >[!quote] Messages
> > [!tip] Core idea
> > + encapsulate information in a standardized way
> 
> > [!success] Solution
![](../../../../z_images/Pasted%20image%2020251229094726.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + 
> >
> >> [!failure] Bad
> >> + 

 >[!quote] Messages
> > [!tip] Core idea
> > + encapsulate information in a standardized way
> 
> > [!success] Solution
![](../../../../z_images/Pasted%20image%2020251229094726.png)
>
> >[!quote] Consequences
> > > [!success] Good
> > > + 
> >
> >> [!failure] Bad
> >> + 

