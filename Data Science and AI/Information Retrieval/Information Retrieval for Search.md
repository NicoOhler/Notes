# Information Retrieval for Search
### Overview
 + search information retrieval
	+ represent documents as [[Vectors as KR]]
	+ assess its relevance (similarity)
	+ ranking

### Representing document as Vector
+ vector represents content
	+ disregards metadata (mostly)
+ vector elements correspond to content elements
	+ words
	+ word stems
	+ concepts
	+ phrases 
+ dictionary vector
	+ contains all selected content elements from documents and query
	+ each element has index
	+ decides which elements are relevant
		+ each vector element represents a different topic
		+ each document has value corresponding to each topic
			+ different ways to generate this value
			+ e.g. TFIDF
	+ weird example
		+ ![[Pasted image 20220425140706.png]]

### TFIDF
+ term frequency-inverse document-frequency
+ generates value for each topic of document
	+ term frequency
		+ based on how often term occurs in document $d_i$
		+ $tf_i=\frac{#term_occurences}{#terms}$
	+ inverse document frequency
		+ specifies how many documents contain term
		+ $idf_i=log_10(\frac{|D|}{#documents_containing_this_term})$
	+ TFIDF
		+ element-wise multiplication of $tf_i$ and $idf$



	[[Information Retrieval]]
