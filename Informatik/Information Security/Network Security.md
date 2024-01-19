###  Data Link Layer
+ MAC flooding attack
	+ switch runs out of space for port to MAC mappings
	+ drop legitimate entries => unicast frames flooded to all ports
+ About Wi-Fi
	+ every client can listen to all packets
	+ WPA2-PSK
		+ pre-shared key
			+ password or dedicated authentication server
		+ traffic inaccessible without password
		+ recording genuine user's handshake
			+ allow offline bruteforce
			+ ![[Pasted image 20240116211902.png]]
			+ easy to derive if SSID + password known
		+ connection control not authenticated/encrypted
			+ easy forging of control frames 
		+ no forward secrecy
		+ weak per-user key derivation
			+ if master password is known
			+ ![[Pasted image 20240116211708.png]]
			+ weak to rainbow tables => no common SSID/password
	+ WPA3
		+ not available on every device
		+ traffic inaccessible without password
		+ cannot attack passwords offline
		+ authenticated control frames
		+ forward secrecy
		+ strong per-user key derivation

### Internet Layer
+ ARP spoofing
	+ ARP maps IPs to MACs
	+ unauthenticated
	+ impersonate someone else 
		+ map own MAC to someone else's IP
+ governments "cooperate" with internet exchange points
+ BGP hijacks
	+ BGP lets network providers advertise routes
		+ big collaborative, distributed shortest-path algorithm
	+ assumes that ISPs are trustworthy
		+ might be hacked
	+ countermeasures
		+ DNSSEC
			+ digital signatures for DNS information
		+ BGP filtering
		+ HTTPS
			+ browser popup due to missing certificate

## Application Layer
+ Connecting to malicious websites
	+ can only attack current tab
	+ no interaction between cross-origin iframes
	+ make requests as victim
+ Token-based authentication
	+ storage
		+ URL rewriting => awful
		+ cookies
			+ SameSite
				+ do not send for requests from different origin
				+ strict/lax/none
					+ default lax allows top-level navigation
			+ Secure
			+ HttpOnly
	+ generation
		+ random session token
			+ server remembers user - token mapping
			+ require good randomness
			+ not infinitely scalable
		+ JSON Web Tokens JWT
			+ signed by server
			+ no need to remember tokens
			+ no expire/invalidation by default
			+ never trust alg field
+ navigate victim to arbitrary URLs
	+ execute POST requests with SameSite=None
	+ assumes GET has no side effects
+ Invisible iframes over buttons
	+ harder with SameSite=Lax default
	+ X-Frame-Options (HTTP header) prevents embedding
+ Cross-Origin Resource Sharing
	+ Access-Control-Allow-Origin
		+ allows specific origins
		+ \* for APIs
		+ otherwise URL/domain
		+ multiple origins => put source in Origin header and check server-side
+ Dealing with data
	+ evaluating JSON instead of parsing 
		+ ![[Pasted image 20240119134808.png]]
	+ SQL
		+ inserted strings 