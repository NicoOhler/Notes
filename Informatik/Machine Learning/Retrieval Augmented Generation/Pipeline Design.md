### Naive RAG

**Naive RAG**: A basic linear approach to RAG with sequential indexing, retrieval, augmentation and generation process.

**Retrieve-Read**: A retriever that retriever reads information and the LLM that is reads this information to generate the results

**RAG Failure Points**: A RAG system can misfire if the the retriever fails to retrieve the entire context or retrieves irrelevant context, the LLM despite being provided the context, does not consider it and, instead of answering the query picks irrelevant information from the context.

**Disjointed Context**: When information is retrieved from different source documents, the transition between two chunks becomes abrupt.

**Over-reliance on Context**: It is noticed, sometimes, that the LLM becomes over-reliant on the retrieved context and forgets to draw from its own parametric memory.

### Advanced RAG

**Advanced RAG**: Pipeline with interventions at pre-retrieval, retrieval and post-retrieval stages to overcome the limitations of Naive RAG.

**Rewrite**-**Retrieve-Rerank-Read**: Improvement upon Retrieve-Read framework by adding the rewriting and reranking component

![None](https://miro.medium.com/v2/resize:fit:700/1*d7gWnFBVfWESzbf-gCgeWg.png)

**Index Optimisation**: Employed in the indexing pipeline, the objective of index optimisation is to set up the knowledge base for better retrieval.

**Query Optimisation**: The objective of query optimisation is to align the input user query in a manner that makes it better suited for the retrieval tasks

**Query Expansion**: The original user query is enriched with the aim of retrieving more relevant information. This helps in increasing the recall of the system and overcomes the challenge of incomplete or very brief user queries.

**Multi-query expansion**: In this approach, multiple variations of the original query are generated using an LLM and each variant query is used to search and retrieve chunks from the knowledge base.

**Sub-query expansion**: In this approach instead of generating variations of the original query, a complex query is broken down into simpler sub-queries.

**Step back expansion**: The term comes from the step-back prompting approach where the original query is abstracted to a higher-level conceptual query.

**Query Transformation**: In query transformation, instead of the original user query retrieval happens on a transformed query which is more suitable for the retriever

**Query Rewriting**: Queries are rewritten from the input. The input in quite a few real-world applications may not be a direct query or a query suited for retrieval. Based on the input a language model can be trained to transform the input into a query which can be used for retrieval.

**Hypothetical document embedding**: HyDE is a technique where the language model first generates a hypothetical answer to the user's query without accessing the knowledge base. This generated answer is then used to perform a similarity search against the document embeddings in the knowledge base, effectively retrieving documents that are similar to the hypothetical answer rather than the query itself.

**Query Routing**: Optimising the user query by routing it to the appropriate workflow based on criteria like intent, domain, language, complexity, source of information etc

**Hybrid Retrieval**: Hybrid retrieval strategy is an essential component of production-grade RAG systems. It involves combining retrieval methods for improved retrieval accuracy. This can mean simply using a keyword-based search along with semantic similarity. It can also mean combining all sparse embedding, dense embedding vector and knowledge graph-based search.

![None](https://miro.medium.com/v2/resize:fit:700/1*sk21RT4Mr5euKGqoMvjI7Q.png)


**Iterative Retrieval**: In this approach the retrieval happens 'n' number of times and the generated response is used to further retrieve documents each time.

**Recursive Retrieval**: This approach improves upon the iterative approach by transforming the retrieval query after each generation.

**Adaptive Retrieval**: This is a more intelligent approach where an LLM determines the most appropriate moment and the most appropriate content for retrieval.

**Contextual Compression**: Reduce the length of the retrieved information by extracting only the parts that are relevant and important to the query. This also has a positive effect on the cost and efficiency of the system.

**Reranking**: Retrieved information from different sources and techniques can further be ranked to determine the most relevant documents. Reranking, like hybrid retrieval, is commonly becoming a necessity in production RAG systems. To this end, commonly available rerankers like multi-vector, Learning to Rank (LTR), BERT based and even hybrid rerankers that can be employed are gaining prominence.

### Modular RAG

**Modular RAG**: Modular RAG breaks down the traditional monolithic RAG structure into interchangeable components. This allows for tailoring of the system to specific use cases. Modular approach brings modularity to RAG components like retrievers, indexing, and generation, while also adding more modules like search, memory, and fusion.

**Search Module**: Aimed at performing search on different data sources, it is customised to different data sources.

**RAG-Fusion**: Improves traditional search systems by overcoming their limitations through a multi-query approach.

**Memory Module**: The Memory Module leverages the inherent 'memory' of the LLM, meaning the knowledge encoded within its parameters from pre-training.

**Routing**: Routing in the RAG system navigates through diverse data sources, selecting the optimal pathway for a query, whether it involves summarization, specific database searches, or merging different information streams.

**Task Adapter:** This module makes RAG adaptable to various downstream tasks allowing the development of task-specific end-to-end retrievers with minimal examples, demonstrating flexibility in handling different tasks. The Task Adapter Module allows the RAG system to be fine-tuned for specific tasks like summarisation, translation, or sentiment analysis.
