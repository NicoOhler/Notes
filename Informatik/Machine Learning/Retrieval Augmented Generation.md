
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