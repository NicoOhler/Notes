#### 2.B — Generation


### 3. Evaluation

#### 3.A — Metrics



#### 3.B — Frameworks

**Frameworks:** Tools designed to facilitate evaluation offering automation of the evaluation process and data generation. They are used to streamline the evaluation process by providing a structured environment for testing different aspects of a RAG systems. They are flexible and can be adapted to different datasets and metrics.

**RAGAS**: Retrieval Augmented Generation Assessment or RAGAs is a framework developed by Exploding Gradients that assesses the retrieval and generation components of RAG systems without relying on extensive human annotations. RAGAs also helps in synthetically generating a test dataset that can be used to evaluate a RAG pipeline

**Synthetic Test Dataset Generation**: Using models like LLMs to automatically generate ground truth data from the knowledge base.

![None](https://miro.medium.com/v2/resize:fit:700/1*tk8RewN90-r0ufrkYamqVw.png)

Synthetic Data Generation in RAGAS (Source: Image by Author)

**LLM as a judge**: Using an LLM to evaluate a task.

**ARES**: Automated RAG evaluation system, or ARES, is a framework developed by researchers at Stanford University and Databricks. Like RAGAs, ARES uses an LLM as a judge approach for evaluations.

#### 3.C — Benchmarks

**Benchmarks**: Standardised datasets and their evaluation metrics used to measure the performance of RAG systems. Benchmarks provide a common ground for comparing different RAG approaches. Benchmarks ensure consistency across the evaluations by considering fixed tasks and evaluation criteria.

**BEIR or Benchmarking Information Retrieval:** A comprehensive, heterogeneous benchmark that is based on 9 IR tasks and 19 Question-Answer datasets.

![None](https://miro.medium.com/v2/resize:fit:700/1*uCq1pt6F13xZZgusXcImgQ.png)

BEIR — 9 tasks and 18 (of 19) datasets (Source: [BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models](https://arxiv.org/pdf/2104.08663v4))

**Retrieval Augmented Generation Benchmark (RGB)**: Introduced in a Dec 2023, it comprises 600 base questions and 400 additional questions, evenly split between English and Chinese. It is a benchmark that focusses on four key abilities of a RAG system — Noise Robustness, Negative Rejection, Information Integration and Counterfactual Robustness

![None](https://miro.medium.com/v2/resize:fit:700/1*HJO2KIS5WMmBibmIxgpu6A.png)

Four abilities required of RAG systems (Source: [Benchmarking Large Language Models in Retrieval-Augmented Generation, Chen et al](https://arxiv.org/pdf/2309.0143) )

**Multihop RAG**: Curated by researchers at HKUST, Multihop RAG contains 2556 queries, with evidence for each query distributed across 2 to 4 documents. The queries also involve document metadata, reflecting complex scenarios commonly found in real-world RAG applications.

**Comprehensive RAG:** Curated by Meta and HKUST, CRAG, is a factual question answering benchmark of 4,409 question-answer pairs and mock APIs to simulate web and Knowledge Graph (KG) search. It contains 8 types of queries across 5 domains

### 4. Pipeline Design

#### 4.A — Naive RAG



#### 4.B — Advanced RAG

**Advanced RAG**: Pipeline with interventions at pre-retrieval, retrieval and post-retrieval stages to overcome the limitations of Naive RAG.

**Rewrite**-**Retrieve-Rerank-Read**: Improvement upon Retrieve-Read framework by adding the rewriting and reranking component

![None](https://miro.medium.com/v2/resize:fit:700/1*d7gWnFBVfWESzbf-gCgeWg.png)

Advanced RAG as Rewrite-Retrieve-Rerank-Read pattern (Source: Image by Author)

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

Hybrid of sparse, dense and graph retrieval (Source: Image by Author)

**Iterative Retrieval**: In this approach the retrieval happens 'n' number of times and the generated response is used to further retrieve documents each time.

**Recursive Retrieval**: This approach improves upon the iterative approach by transforming the retrieval query after each generation.

**Adaptive Retrieval**: This is a more intelligent approach where an LLM determines the most appropriate moment and the most appropriate content for retrieval.

**Contextual Compression**: Reduce the length of the retrieved information by extracting only the parts that are relevant and important to the query. This also has a positive effect on the cost and efficiency of the system.

**Reranking**: Retrieved information from different sources and techniques can further be ranked to determine the most relevant documents. Reranking, like hybrid retrieval, is commonly becoming a necessity in production RAG systems. To this end, commonly available rerankers like multi-vector, Learning to Rank (LTR), BERT based and even hybrid rerankers that can be employed are gaining prominence.

#### 4.D — Modular RAG

**Modular RAG**: Modular RAG breaks down the traditional monolithic RAG structure into interchangeable components. This allows for tailoring of the system to specific use cases. Modular approach brings modularity to RAG components like retrievers, indexing, and generation, while also adding more modules like search, memory, and fusion.

**Search Module**: Aimed at performing search on different data sources, it is customised to different data sources.

**RAG-Fusion**: Improves traditional search systems by overcoming their limitations through a multi-query approach.

**Memory Module**: The Memory Module leverages the inherent 'memory' of the LLM, meaning the knowledge encoded within its parameters from pre-training.

**Routing**: Routing in the RAG system navigates through diverse data sources, selecting the optimal pathway for a query, whether it involves summarization, specific database searches, or merging different information streams.

**Task Adapter:** This module makes RAG adaptable to various downstream tasks allowing the development of task-specific end-to-end retrievers with minimal examples, demonstrating flexibility in handling different tasks. The Task Adapter Module allows the RAG system to be fine-tuned for specific tasks like summarisation, translation, or sentiment analysis.

### 5. Operations Stack

#### 5.A — Critical Layers

**Critical Layers**: Fundamental components for the operation of a RAG system. A RAG system is likely to fail if any of these layers are missing or incomplete

**Data Layer**: The data layer serves the critical role of creating and storing the knowledge base for RAG. It is responsible for collecting data from source systems, transforming it into a usable format and storing it for efficient retrieval.

**Model Layer**: Predictive models enable generative AI applications. Some models are provided by third parties and some need to be custom trained or fine-tuned. Generating quick and cost-effective model responses is also an important aspect of leveraging predictive models. This layer holds the model library, training & fine-tuning and the inference optimisation components.

![None](https://miro.medium.com/v2/resize:fit:700/1*WmVdKrPuL_FXaDCowfqU-g.png)

Model Layer of the RAGOps stack (Source: Image by Author)

**Fully managed deployment**: Deployment provided by service providers where all infrastructure for model deployment, serving, and scaling is managed and optimised by these providers

**Self-hosted deployment**: In this scenario, models are deployed in private clouds or on-premises, and the infrastructure is managed by the application developer. Tools like Kubernetes and Docker are widely used for containerisation and orchestration of models, while Nvidia Triton Inference Server can optimise inference on Nvidia hardware.

**Local/edge deployment:** Running optimised versions of models on local hardware or edge devices, ensuring data privacy, reduced latency, and offline functionality.

**Application Orchestration Layer** : Layer responsible for managing the interactions amongst the other layers in the system. It is a central coordinator that enables communication between data, retrieval systems, generation models and other services.

#### 5.B — Essential Layers

**Essential Layers**: Layers focussing on performance, reliability and safety of the system. These essential components bring the system to a standard that provides value to the user.

**Prompt Layer**: Manages the augmentation and other LLM prompts.

**Evaluation Layer**: Manages regular evaluation of retrieval accuracy, context relevance, faithfulness and answer relevance of the system is necessary to ensure the quality of responses.

**Monitoring Layer**: Continuous monitoring ensures the long-term health of the RAG system. Understanding system behaviour and identifying points of failure, assessing the relevance & adequacy of information, and tracking regular system metrics tracking like resource utilisation, latency and error rates form the part of the monitoring layer.

**LLM Security & Privacy Layer**: RAG systems rely on large knowledge bases stored in vector databases, which can contain sensitive information. They need to follow all data privacy regulations, data protection strategies like anonymisation, encryption, differential privacy, query validation & sanitisation, and output filtering to assist in protection against attacks. Implementing guardrails, access controls, monitoring and auditing are also components of the security and privacy layer.

**Caching Layer**: Caching is becoming a very important component of any LLM based application. This is because the high costs and inherent latency of generative AI models. With the addition of retrieval layer, the costs and latency increase further in RAG systems.

![None](https://miro.medium.com/v2/resize:fit:700/1*2mcaxzTkYXDvHFUgXydpJA.png)


#### 5.C — Enhancement Layers

**Enhancement Layer**: Layers improving the efficiency, scalability and usability of the system. These components are used to make the RAG system better and are decided based on the end requirements.

**Human-in-the-loop Layer**: Provides critical oversight where human judgment is necessary, especially for use-cases requiring higher accuracy or ethical considerations.

**Cost Optimisation Layer**: Helps manage resources efficiently, which is particularly important for large-scale systems.

**Explainability and Interpretability Layer**: Provides transparency for system decisions, especially important for domains requiring accountability

**Collaboration and Experimentation Layer**: Useful for teams working on development and experimentation but non-critical for system operation.

### 6. Emerging Patterns

#### **6.A — Knowledge Graphs**

**Knowledge Graph powered RAG**: Using knowledge graph structures not only increases the contextual understanding but also equips the system with enhanced reasoning capabilities and improved explainability.

**Knowledge Graphs**: Knowledge graphs organise data in a structured manner as entities and relationships.

**GraphRAG**: An open-source framework developed by Microsoft that facilitates automatic creation of knowledge graphs from source documents and then uses the knowledge graph for retrieval.

**Graph Communities**: Partitioning entities & relationships into groups.

**Community Summaries**: LLM generated summaries for communities, providing insights into topical structure and semantics

**Local Search**: Identifying a set of entities from the knowledge graph that are semantically-related to the user input

**Global Search**: Similarity based search on community summaries.

**Ontology**: A formal representation of knowledge as a set of concepts within a domain, and the relationships between those concepts.

#### 6.B — Multimodal

**Multimodal RAG**: Using other modalities like images, audio, video etc. in addition to text in both retrieval and generation.

**Modality**: A specific type of input data, such as text, image, video, or audio. Multimodal systems can handle multiple modalities simultaneously.

**Multimodal Embeddings**: A unified vector representation that encodes multiple data types (e.g., text and image embeddings combined) to enable retrieval across different modalities.

**CLIP (Contrastive Language-Image Pre-training)**: A model developed by OpenAI that learns visual concepts from natural language supervision, often used for cross-modal retrieval and generation

![None](https://miro.medium.com/v2/resize:fit:700/1*Qd4KNvG5JuODabqkYf8YqA.png)

Mapping data of different modalities into a shared embedding space (Source: Image by Author)

**Contrastive Learning**: A learning method used to align data across different modalities by bringing semantically similar data points closer in the shared embedding space.

#### 6.C — Agentic

**Agentic RAG**: Leverages LLM based agents for adapting RAG workflow to query types and the type of documents in the knowledge base.

**Adaptive Frameworks**: Dynamic systems that adjust retrieval and generation strategies based on the evolving context and data, ensuring relevant responses.

**Routing Agents**: Agents responsible for directing user queries to the most appropriate sources or sub-systems for efficient processing.

**Query Planning Agents**: Agents that break down complex queries into sub-queries and manage their execution across different retrieval pipelines.

**Multiple Vectors per Document**: A technique where multiple vector representations are generated for each document to capture different aspects of its content.
### 8. Applied RAG

#### 8.A — Other RAG Patterns

**Corrective RAG**: In this approach, [real-time information is retrieved to check for the factual accuracy of the LLM generated answer](https://arxiv.org/abs/2401.15884). Particularly useful in fact-checking, medical & legal domains.

**Contrastive RAG**: Integrates contrastive learning techniques to enhance the retrieval process by distinguishing between relevant and irrelevant documents. [https://arxiv.org/abs/2406.06577](https://arxiv.org/abs/2406.06577)

**Selective RAG**: Optimises the retrieval phase by determining [when it is beneficial to retrieve external information](https://arxiv.org/abs/2403.10059). This method aims to improve the overall performance of language models, particularly in contexts where retrieval may not add value.

**RAG with Active Learning**: User feedback on generated content is used to [fine-tune or adapt the retrieval process over time](https://arxiv.org/abs/2402.13547). Useful in continuous improvement systems, like recommendation engines or educational tutoring systems, where the goal is to enhance performance with each interaction.

**Personalised RAG**: User preferences, behaviour, and historical interactions are used to [personalise the retrieval process](https://arxiv.org/abs/2401.13256). It's used in personalisation-heavy domains like recommendation engines or customer service, where the system tailors responses to individual users.

**Self-RAG**: An adaptive retrieval mechanism that [selectively decides when to retrieve knowledge based](https://arxiv.org/abs/2310.11511) on the query's context.

**RAFT**: [Retrieval-Augmented Fine-Tuning](https://techcommunity.microsoft.com/t5/ai-ai-platform-blog/raft-a-new-way-to-teach-llms-to-be-better-at-rag/ba-p/4084674) combine retrieval mechanisms with traditional fine-tuning techniques to help models access and utilise external knowledge dynamically during their fine-tuning process.

**RAPTOR**: [Recursive Abstractive Processing for Tree-Organised Retrieval](https://arxiv.org/abs/2401.18059) focusses on creating a recursive, tree-like structure from documents to improve context-aware information retrieval. It is beneficial for question-answering tasks, especially when dealing with extensive documents or information that requires multi-step reasoning.

#### **8.B — Application Areas**

**Search Engine**: Conventional search results are shown as a list of page links ordered by relevance. More recently, Google Search, Perplexity, You have used RAG to present a coherent piece of text, in natural language, with source citation. As a matter of fact, search engine companies are now building LLM first search engines where RAG is the cornerstone of the algorithm.

![None](https://miro.medium.com/v2/resize:fit:700/1*zTTjvhOv9K2Cz6JuZyLZvA.png)

Prominent Search Engines using RAG (Source: Google.com, Bing.com, Perplexity.ai, OpenAI.com)

**Personalised Marketing Content Generation**: The widest use of LLMs has probably been in content generation. Using RAG, the content can be personalised to readers, incorporate real-time trends and be contextually appropriate. Yarnit, Jasper, Simplified are some of the platforms that assist in marketing content generation like blogs, emails, social media content, digital advertisements etc.

**Personalised Learning Plans**: In the field or education, and learning & development, RAG is used extensively to create personalised learning paths based on past trends and for automated evaluation and feedback.

**Real-time Event Commentary**: Imagine an event like a sport or a news event. A retriever can connect to real-time updates/data via APIs and pass this information to the LLM to create a virtual commentator. These can further be augmented with Text-To-Speech models. IBM leveraged technology for commentary during the 2023 US Open Tennis tournament.

**Conversational agents**: LLMs can be customised to product/service manuals, domain knowledge, guidelines, etc. using RAG and serve as support agents resolving user complaints and issues. These agents can also route users to more specialised agents depending on the nature of the query. Almost all LLM based chatbots on websites or as internal tools use RAG. These are being used in industries like Travel & Hospitality, Fintech and e-commerce.

**Document Question Answering Systems**: With access to proprietary documents, a RAG enabled system becomes an intelligent AI system that can answer all questions about the organisation.

**Virtual Assistants**: Virtual personal assistants like Siri, Alexa and others are in plans to use LLMs to enhance the user's experience. Coupled with more context on user behaviour using RAG, these assistants are set to become more personalised.

#### **8.C — Applied RAG Challenges**

**Relevance Mismatch**: Difficulty retrieving the most relevant documents or passages from a large dataset due to suboptimal ranking or search mechanisms.

**Over-Retrieval**: Retrieving too many documents, leading to unnecessary noise and irrelevant content in the final generation.

**Sparse vs Dense Retrieval Trade-off**: Balancing between sparse retrieval (TF-IDF, BM25) and dense retrieval (using embeddings) to maximise relevance without losing performance.

**Document Question Answering Systems**: With access to proprietary documents, a RAG enabled system becomes an intelligent AI system that can answer all questions about the organisation.

**Latency**: Retrieval from large or distributed knowledge bases can introduce significant delays, affecting real-time applications.

**Cost of Storage**: Maintaining and managing massive vector databases for dense retrieval can be expensive and resource-intensive.

**Narrow Retrieval Focus**: The challenge of retrieving diverse perspectives or sources to ensure that multiple viewpoints or alternative pieces of evidence are surfaced.

**Bias in Retrieval**: Biases in retrieval results based on the structure of the indexed data or retrieval algorithms.

**Context Loss in Long Queries**: Loss of context when handling long, multi-turn queries, leading to disjointed or incomplete answers.

**Incoherent Summarisation**: Generating inconsistent or disjointed summaries from multiple retrieved documents, leading to poor user experience.

**Over-Generation**: Generating overly verbose or redundant responses based on retrieved data that fails to condense the key points effectively.

**Inconsistent Modal Alignment**: Challenges integrating multimodal data where retrieved content across different modalities may not be aligned properly, affecting the quality of the generated response.

**Data Silos**: When knowledge is fragmented across multiple sources or platforms, retrieval becomes challenging due to inconsistent indexing or lack of interoperability between knowledge bases.

**Processing Large-Scale Data**: Difficulty in maintaining high throughput and low latency as the amount of indexed data grows.

**Multi-Agent Coordination**: When multiple agents are used for task orchestration (as in agentic RAG), coordination among agents can become complex and resource-heavy, impacting system efficiency.

**Inefficient Query Routing**: Routing queries to the wrong sources or retrieval pipelines can reduce efficiency.

**Data Poisoning Attacks**: External retrieval sources could be manipulated to feed biased or poisoned data into the generation pipeline, leading to compromised outputs.

**Adversarial Attacks**: Security vulnerabilities where attackers may influence retrieval or generation results by exploiting weaknesses in retrieval pipelines.

**Knowledge Base Updating**: Maintaining an up-to-date knowledge base while keeping the retrieval process fast and accurate can be difficult, especially in dynamic fields like news or finance.

**Memory Retention**: Ensuring that the system can store and retrieve long-term memory across interactions, allowing for a more personalised and context-aware response.

RAG is a fast evolving technique, like much of the generative AI space and it is quite easy to get overwhelmed with all the jargon. I hope this taxonomy will help in breaking down the components of RAG systems, assess the various approaches within RAG systems, making it easier to design, develop, and optimise RAG systems.