### LLM Limitations

**Knowledge Cut-off Date**: Training an LLM is an expensive and time-consuming process. It takes massive volumes of data and several weeks, or even months, to train an LLM. The data that LLMs are trained on is therefore not current. For example, [GPT-4o has knowledge only up to October 2023.](https://otterly.ai/blog/knowledge-cutoff/) Any event that happened after this knowledge cut-off date is not available to the model.

**Training Data Limitation**: LLMs are trained on large volumes of data from a variety of public sources — like [Llama 3 has been trained on a whopping 15 trillion tokens (about 7 times more than Llama 2](https://kili-technology.com/large-language-models-llms/llama-3-guide-everything-you-need-to-know-about-meta-s-new-model-and-its-data#training-dataset--quality-and-quantity)) — but they do not have any knowledge of information that is not public. Publicly available LLMs have not been trained on information like internal company documents, customer information, product documents, etc. So, LLMs cannot be expected to respond to queries about such information.

**Hallucinations**: [LLMs are next-word predictors. They are not trained to verify the facts in their responses](https://amistrongeryet.substack.com/p/large-language-models-explained). Thus, it is observed that LLMs sometimes provide responses that are factually incorrect, and despite being incorrect, these responses sound extremely confident and legitimate. This characteristic of "lying with confidence," called hallucination, has proved to be one of the biggest criticisms of LLMs.

**Context Window**: Every LLM, by the nature of the architecture, can process upto a maximum number of tokens. This maximum number of tokens is referred to as the context window of the model. If the prompt is longer than the context window, then the portion of the prompt beyond the limit is discarded.

![None](https://miro.medium.com/v2/resize:fit:700/1*kw9RMVEV5EElOoFqQzeOFQ.png)

Popular LLMs with their cut-off date and context window (Source: Curated by Author)