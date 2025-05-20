**Indexing Pipeline:** The set of processes that is employed to create the knowledge base for RAG applications. It is a non real-time pipeline that updates the knowledge base at periodic intervals.

**Source Systems**: The original locations where the data that is desired for the RAG application is stored. These can be data lakes, file systems, CMSs, SQL & NoSQL databases, 3rd party data stores etc.

**Data Loading**: The first step of the indexing pipeline that connects to source systems to extract and parse files for data to be used in the RAG knowledge base.

**Metadata**: A common way of defining metadata is "data about data". Metadata describes other data. It can provide information like a description of the data, time of creation, author, etc. While metadata is useful for managing and organising data, in the context of RAG, metadata enhances the search-ability of data.

**Data Masking:** Obfuscation of sensitive information like PII or confidential data

**Chunking**: The process of breaking down long pieces of text into smaller manageable sizes or "chunks". Chunking is crucial to the efficient creation of knowledge base for RAG systems. Chunking increases the ease of search and overcomes the context window limits of LLMs.

**Lost in the middle problem:** Even in those LLMs which have a long context window (Claude 3 by Anthropic has a context window of up to 200,00 tokens), an issue with accurately reading the information has been observed. It has been noticed that [accuracy declines dramatically if the relevant information is somewhere in the middle of the prompt](https://cs.stanford.edu/~nfliu/papers/lost-in-the-middle.arxiv2023.pdf). This problem can be addressed by passing only the relevant information to the LLM instead of the entire document.

**Fixed Size Chunking**: A very common approach is to p[re-determine the size of the chunk and the amount of overlap between the chunks](https://www.geeksforgeeks.org/how-to-chunk-text-data-a-comparative-analysis/). There are several chunking methods that follow a fixed size chunking approach. Chunks are created based on a fixed number of characters, tokens, sentences or paragraphs.

**Structure-Based Chunking**: The aim of chunking is to keep meaningful data together. If we are dealing with data in form of HTML, Markdown, JSON or even computer code, it makes more sense to split the data based on the structure rather than a fixed size.

**Context-Enriched Chunking:** [This method adds the summary of the larger document to each chunk to enrich the context of the smaller chunk](https://adasci.org/chunking-strategies-for-rag-in-generative-ai/). This makes more context available to the LLM without adding too much noise. It also improves the retrieval accuracy and maintains semantic coherence across chunks. This is particularly useful in scenarios where a more holistic view of the information is crucial. While this approach enhances the understanding of the broader context, it adds a level of complexity and comes at the cost of higher computational requirements, increased storage needs and possible latency in retrieval.

**Agentic Chunking**: In [agentic chunking](https://myscale.com/blog/benefits-agentic-chunking-love/), chunks from the text are created based on a goal or a task. Consider an e-commerce platform wanting to analyse customer reviews. The best way for the reviews to be chunked is if the reviews pertaining to a particular topic are put in the same chunk. Similarly, the critical reviews and positive reviews may be put in different chunks. To achieve this kind of chunking, we will need to do sentiment analysis, entity extraction and some kind of clustering. This can be achieved by a multi-agent system. Agentic chunking is still an active area of research and improvement.

**Semantic Chunking:** This method looks at [semantic similarity](https://python.langchain.com/v0.2/docs/how_to/semantic-chunker/) (or similarity in the meaning) between sentences is called semantic chunking. It first creates groups of three sentences and then merges groups that are similar in meaning. To find out the similarity in meaning, this method uses Embeddings. This is still an experimental chunking technique.

**[Small to big chunking](https://towardsdatascience.com/advanced-rag-01-small-to-big-retrieval-172181b396d4)**: A hierarchical chunking method where the text is first broken down into very small units (e.g., sentences, paragraphs), and the small chunks are merged into larger ones until the chunk size is achieved. Sliding window chunking uses overlap between chunks to maintain context across chunk boundaries**.**

![None](https://miro.medium.com/v2/resize:fit:700/1*G8njsa0-GRvbmFQQQ_VGoA.png)

Small to big chunking (Source: Image by Author)

**Chunk Size:** The [size of the chunks, which is measure in the number of tokens in the chunk, can have a significant impact on the quality of the RAG system](https://www.llamaindex.ai/blog/evaluating-the-ideal-chunk-size-for-a-rag-system-using-llamaindex-6207e5d3fec5). While large sized chunks provide better context, they also carry a lot of noise. Smaller chunks, on the other hand, have precise information but they might miss important information.

**Metadata Filtering:** Adding metadata like timestamp, author, category, etc. can enhance the chunks. While retrieving, chunks can first be filtered by relevant metadata information before doing a similarity search. This improves retrieval efficiency and reduces noise in the system. For example, using the timestamp filters can help avoid outdated information in the knowledge base.

**Metadata Enhancement**: Metadata like chunk summary, sentiment, category etc. that can be inferred beyond tags like source, timestamp, author etc. can be used to enhance retrieval.

**Parent Child Indexing:** A document structure where documents are organised hierarchically. The parent document contains overarching themes or summaries, while child documents delve into specific details. During retrieval, the system can first locate the most relevant child documents and then refer to the parent documents for additional context if needed. This approach enhances the precision of retrieval while maintaining the broader context. At the same time, this hierarchical structure can present challenges in terms of memory requirements and computational load.

**Embeddings**: Computers, at the very core, do mathematical calculations. Mathematical calculations are done on numbers. Therefore, for a computer to process any kind of non-numeric data like text or image, it must be first converted into a numerical form. Embeddings is a design pattern that is extremely useful for RAG. Embeddings are vector representations of data. As a general definition, embeddings are data that has been transformed into n-dimensional matrices. A word embedding is a vector representation of words.


![None](https://miro.medium.com/v2/resize:fit:700/1*t7v6yp6d3d702NHqj_8adw.png)

**Cosine Similarity**: The reason why embeddings are popular is because they help in establishing semantic relationship between words, phrases, and documents. Cosine similarity is calculated as the cosine value of the angle between the two vectors. Cosine of parallel lines i.e. angle=0 is 1 and cosine of a right angle i.e. 90 is 0. On the other end, the cosine of opposite lines i.e. angle =180 is -1. Therefore, the cosine similarity lies between -1 and 1 where unrelated terms have a value close to 0, and related terms have a value close to 1.

![None](https://miro.medium.com/v2/resize:fit:700/1*YiLBenEmsOVeMxdtT8TkmQ.png)

Cosine similarity calculation (Source: Image by Author)

**Word2Vec**: Word2Vec is a shallow neural network-based model for learning word embeddings developed by researchers at Google. It is one of the earliest embedding techniques

**GloVe**: Global Vectors for Word Representations is an unsupervised learning technique developed by researchers at Stanford University

**FastText**: FastText is an extension of Word2Vec developed by Facebook AI Research. It is particularly useful for handling misspellings and rare words.

**ELMo:** Embeddings from Language Models was developed by researchers at Allen Institute for AI. ELMo embeddings have been shown to improve performance on question answering and sentiment analysis tasks.

**BERT**: Bidirectional Encoder Representations from Transformers, developed by researchers at Google, is a Transformers architecture-based model. It provides contextualized word embeddings by considering bidirectional context, achieving state-of-the-art performance on various natural language processing tasks.

**Pre-trained Embeddings Models**: Embeddings models that have been trained on a large corpus of data can also generalise well across a number of tasks and domains. There are a variety of proprietary and open-source pre-trained embeddings models that are available to use. This is also one of the reasons why the usage of embeddings has exploded in popularity across machine learning applications.

**Vector Databases**: Vector Databases are built to handle high dimensional vectors like embeddings. These databases specialise in indexing and storing vector embeddings for fast semantic search and retrieval.

**Vector Indices**: These are libraries that focus on the core features of indexing and search. They do not support data management, query processing, interfaces etc. They can be considered a bare bones vector database. Examples of vector indices are Facebook AI Similarity Search (FAISS), Non-Metric Space Library (NMSLIB), Approximate Nearest Neighbors Oh Yeah (ANNOY), etc.