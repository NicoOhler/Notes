**Corrective RAG**: In this approach, [real-time information is retrieved to check for the factual accuracy of the LLM generated answer](https://arxiv.org/abs/2401.15884). Particularly useful in fact-checking, medical & legal domains.

**Contrastive RAG**: Integrates contrastive learning techniques to enhance the retrieval process by distinguishing between relevant and irrelevant documents. [https://arxiv.org/abs/2406.06577](https://arxiv.org/abs/2406.06577)

**Selective RAG**: Optimises the retrieval phase by determining [when it is beneficial to retrieve external information](https://arxiv.org/abs/2403.10059). This method aims to improve the overall performance of language models, particularly in contexts where retrieval may not add value.

**RAG with Active Learning**: User feedback on generated content is used to [fine-tune or adapt the retrieval process over time](https://arxiv.org/abs/2402.13547). Useful in continuous improvement systems, like recommendation engines or educational tutoring systems, where the goal is to enhance performance with each interaction.

**Personalised RAG**: User preferences, behaviour, and historical interactions are used to [personalise the retrieval process](https://arxiv.org/abs/2401.13256). It's used in personalisation-heavy domains like recommendation engines or customer service, where the system tailors responses to individual users.

**Self-RAG**: An adaptive retrieval mechanism that [selectively decides when to retrieve knowledge based](https://arxiv.org/abs/2310.11511) on the query's context.

**RAFT**: [Retrieval-Augmented Fine-Tuning](https://techcommunity.microsoft.com/t5/ai-ai-platform-blog/raft-a-new-way-to-teach-llms-to-be-better-at-rag/ba-p/4084674) combine retrieval mechanisms with traditional fine-tuning techniques to help models access and utilise external knowledge dynamically during their fine-tuning process.

**RAPTOR**: [Recursive Abstractive Processing for Tree-Organised Retrieval](https://arxiv.org/abs/2401.18059) focusses on creating a recursive, tree-like structure from documents to improve context-aware information retrieval. It is beneficial for question-answering tasks, especially when dealing with extensive documents or information that requires multi-step reasoning.