### Naive RAG

**Naive RAG**: A basic linear approach to RAG with sequential indexing, retrieval, augmentation and generation process.

**Retrieve-Read**: A retriever that retriever reads information and the LLM that is reads this information to generate the results

**RAG Failure Points**: A RAG system can misfire if the the retriever fails to retrieve the entire context or retrieves irrelevant context, the LLM despite being provided the context, does not consider it and, instead of answering the query picks irrelevant information from the context.

**Disjointed Context**: When information is retrieved from different source documents, the transition between two chunks becomes abrupt.

**Over-reliance on Context**: It is noticed, sometimes, that the LLM becomes over-reliant on the retrieved context and forgets to draw from its own parametric memory.