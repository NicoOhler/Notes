### Klausur
Teilbarkeit, Euklid
	m|n <==> n=km
		m|0, m|m, 1|n, n|m und m|n <==> m=n
	division n/m ==> n=km+r
	ggT(m,n) = 1 ==> teilerfremd/rel prim
		algo
		ggt(m,0)=m
		ggt(m,1)=1
		ggt(m,m)=m
		ggt(lm,ln)=lggt(m,n)
		ggt(m,n)=d ==> ggt(m/d,n/d)=1
		n=km+r ==> ggt(n,m)=ggt(m,r)
	kgV(m,n)
		algo
	euklid
		tabelle a b  q r
			a(n+2)=a(n)-q(n+2)\*a(n+1)
			a\*m+b\*n=ggT
Logik
		
Primzahlen
	einzige Teiler von p sind 1,p
	jede n aus N >=2 teilbar durch mind 1 primzahl
	primfaktorzerlegung
		p|a\*b ==> p|a oder p|b
Äquivalenzrelationen

Gruppen
Relationen
	Partitionen

kongruenzen
	diophantische gl
	chin restsatz
	satz von euler fermat

kryptographie
	diffie hellman
	rsa