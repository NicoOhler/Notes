# Information Retrieval
### Overview
+ assign a relevance score to documents based on a query
+ ranks documents by relevance
	+ further filtering possible
	+ each document is [[Vectors as KR]]
		+ relevant if simillar to query
+ different from [[Data Retrieval]]
	+ hybrid approach possible
+ heavily reliant on user feedback
	+ query refining
		+ user unhappy with results ==>  user changes query
	+ offline evaluation and adaptation of algorithms
	+ online machine learning
+ usage:
	+ [[Recommender Systems]]]
	+ search engines
	+ basically all over the web

###  Formula
+ r=f(q,D)
	+ r...ranking score
	+ D...set of documents
	+ q...query returns data from document
	+ f....function returns ranking based on query and document

### Query formulation
+ content-related queries
+ query by example
	+ upload similar image
	+ recommend books based on previously read books
+ context extended queries

[[Data Science and AI]]