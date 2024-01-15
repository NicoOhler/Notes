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
		+ complexity
			+ Exhaustive key search takes ~$2^k$ offline trials
			+ Guessing the tag takes ~$2^t$ online trials
	+ Signatures
		+ uses encryption instead of hashing
		+ uses asymmetric private key K to encrypt message M to a signature S
		+ send M and S
		+ receiver decrypts S with public key to M' and verifies M=M'
+ Confidentiality using encryption
	+ block ciphers
		+ bijective permutation $E_K$ based on k-bit key K to encrypt n-bit message blocks M into n-bit cipher text blocks C
		+ inverse permutation $D_K=E_K^{-1}$ for decryption
		+ complexity
			+ $2^k$ possible keys(mappings)
			+ $2^n$ possible outputs for input
		+ requirements
			+ pseudorandomness
				+ unable to learn M from C (or vice-versa)
			+ key recovery security
				+ unable to recover K given any arbitrary number of (M, C) pairs
	+ key-alternating using key schedule
		+ each round/iteration depends on different round key which has been derived from K
		+ e.g. AES
			+ ![[Pasted image 20240115093758.png]]
			+ SubBytes
				+ substitute using lookup table S-box with original byte as key
				+ $b_{ij} = S[a_{ij}]$
			+ ShiftRows
				+ shift row i by i bytes to the left
				+ $b_{ij} = a_{i(j+i\%4)}$
			+ MixColumns
				+ multiplication of each column with constant matrix M
				+ ![[Pasted image 20240115094429.png]]
			+ AddRoundKey
				+ XOR with $k^{(r)}$
				+ $b_{ij} = a_{ij}⊕k^{(r)}$
	+ regular encryption
		+ does not provide authentication
		+ ECB
			+ ![[Pasted image 20240115094730.png]]
			+ ![[Pasted image 20240115094743.png]]
		+ CBC
			+ ![[Pasted image 20240115094825.png]]
			+ C also depends on nonce and previous blocks
		+ CTR
			+ ![[Pasted image 20240115094928.png]]
			+ C also depends on nonce and block index
	+ Authenticated Encryption (with Associated Data)
		+ produces cipher text C and tag T for message M using symmetric key K, nonce N and associated data A (e.g. metadata or system parameters)
		+ some TLS 1.3 authenticated ciphers
			+ AES-CCM (CTR using AES encryption with CBC-MAC authentication)
				+ ![[Pasted image 20240115095527.png]]
			+ AES-GCM (default)
+ Asymmetric encryption schemes
	+ Preliminary maths
		+ Euler function for product n of 2 primes p, q
			+ $\upvarphi(n)=\upvarphi(pq)=(p-1)(q-1)$
		+ Euler theorem
			+ a,n are coprime $\Leftrightarrow a^{\upvarphi(n)}\equiv 1 \pmod{n}$
		+ ![[Pasted image 20240115100753.png]]
		+ ![[Pasted image 20240115100804.png]]
		+ ![[Pasted image 20240115101326.png]]
		+ ![[Pasted image 20240115101307.png]]
	+ Key exchange
		+ agree on shared symmetric key while communicating over insecure channel
		+ Diffie-Hellman
			+ public: large prime p and generator $\alpha$
			+ Alice chooses $a∈{2,...,p-2}$ and sends $\alpha^a$ to Bob
			+ Bob chooses $b∈{2,...,p-2}$ and sends $\alpha^b$ to Alice
			+ $K_{AB}\equiv(\alpha^b)^a \pmod{p}\equiv(\alpha^b)^a \pmod{p}
			+ a^{\upvarphi(n)}\equiv 1 \pmod{n}$
