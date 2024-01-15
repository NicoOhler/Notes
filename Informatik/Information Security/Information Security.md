### Overview
+ Cryptography
	+ [[C0_Introduction.pdf]]
	+ [[C1_Authentication.pdf]]
	+ [[C2_Encryption.pdf]]
	+ [[C3_Asymmetric.pdf]]
	+ [[C4_Protocols.pdf]]
+ System Security
	+ [[S1_Memory_Safety.pdf]]
	+ [[S2_Side_Channels.pdf]]
	+ [[S3_Physical_Side_Channels.pdf]]
	+ [[S4_Sandboxing_and_Isolation.pdf]]
+ Networking
	+ [[N1_Networks.pdf]]
	+ [[N2_Servers.pdf]]
	+ [[N3]]

### Cryptography - Exam Summary
+ Authenticity using hash functions
	+ Compression function
		+ hash function for fixed-size input
	+ MD-Hash
		+ hash function for input of arbitrary size
		+ padding always applied so the input is a multiple of the block size
		+ hash=tag
	+ MAC
		+ hash function which uses symmetric key K (k-bits) to compute tag t (t-bits) for authentication of message M
		+ application
			+ compute T for M
			+ send M and T
			+ receiver recomputes new tag T' on M
			+ receiver verifies T=T'
		+ unforgeability
			+ infeasible for attacker to forge any new valid pair (M,T) even if they can query tags for any other messages 
			+ Exhaustive key search takes ~$2^k$ offline trials
			+ Guessing the tag takes ~$2^t$ online trials
+ Confidentiality using encryption
	+ block ciphers
		+ bijective permutation $E_K$ based on k-bit key K to encrypt n-bit message blocks M into n-bit cipher text blocks C
		+ inverse permutation $D_K=E_K^{-1}$ for decryption
		+ $2^k$ possible mappings
		+ $2^n$ possible 
	+ regular encryption
		+ 