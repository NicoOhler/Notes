### Overview
 + search information retrieval
	+ represent documents as [[Vectors as KR]]
	+ assess its relevance (similarity)
	+ ranking

### Representing Documents as Vector
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
			+ e.g. [[TFIDF]]
	+ hides some words with [[Natural Language Processing]]
	+ weird example
		+ ![](../../z_images/Pasted%20image%2020220425140706.png)


	[[Information Retrieval]]
