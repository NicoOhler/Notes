### Term Frequency-Inverse Document Frequency
+ generates value for each topic of document
	+ documents are [[Vectors as KR]]
		+ each topic as vector element
	+ term frequency
		+ based on how often term occurs in document $d_i$
		+ normaliced with document length
		+ $tf_i=$$\frac{\#term\_occurences}{\#terms}$
	+ inverse document frequency
		+ based on how many documents contain term
		+ $idf_i=log_10(\frac{|D|}{\#documents\_containing\_this\_term})$
	+ TFIDF
		+ combination of 
			+ term frequency
			+ inverse document frequency
		+ element-wise multiplication of $tf_i$ and $idf$
+ example
	+ ![](../../z_images/Pasted%20image%2020220425144131.png)
	+ ![](../../z_images/Pasted%20image%2020220425144153.png)
