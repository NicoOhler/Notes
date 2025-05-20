**Evaluation Metrics**: Quantitative measures used to evaluate the performance of retrieval & generation and overall RAG system.

**Accuracy**: The proportion of correct predictions (both true positives and true negatives) among the total number of cases examined. Even though accuracy is a simple, intuitive metric, it is not the primary metric for retrieval. In a large knowledge base, majority of documents are usually irrelevant to any given query, which can lead to misleadingly high accuracy scores. It does not consider ranking of the retrieved results.

**Precision**: It measures the proportion of retrieved documents that are relevant to the user query. It answers the question, "Of all the documents that were retrieved, how many were actually relevant?"

**Precision@k**: A variation of precision that measures the proportion of relevant documents amongst the top 'k' retrieved results. It is particularly important because it focusses on the top results rather than all the retrieved documents.

**Recall**: It measures the proportion of the relevant documents retrieved from all the relevant documents in the corpus. It answers the question, "Of all the relevant documents, how many were actually retrieved?". Like precision, recall also doesn't consider the ranking of the retrieved documents. It can also be misleading as retrieving all documents in the knowledge base will result in a perfect recall value.

**F1-score**: The harmonic mean of precision and recall. It provides a single metric that balances both the quality and coverage of the retriever.

![None](https://miro.medium.com/v2/resize:fit:700/1*TJYJVfHX5VoCVcHAEPeNwA.png)


**Mean Reciprocal Rank (MRR)**: Useful in evaluating the rank of the relevant document, it measures the reciprocal of the ranks of the first relevant document in the list of results. MRR is calculated over a set of queries.

**Mean Average Precision(MAP):** A metric that combines precision and recall at different cut-off levels of 'k' i.e. the cut-off number for the top results. It calculates a measure called Average Precision and then averages it across all queries.

**Normalised Discounted Cumulative Gain (nDCG)**: Evaluates the ranking quality by considering the position of relevant documents in the result list and assigning higher scores to relevant documents appearing earlier. It is particularly effective for scenarios where documents have varying degrees of relevance.

![None](https://miro.medium.com/v2/resize:fit:700/1*6Tk-D5EEYKA3jfcbGQ4TvQ.png)

Calculating nDCG(Source: Image by Author)

**Context relevance**: Evaluates how well the retrieved documents relate to the original query. The key aspects are topical alignment, information usefulness and redundancy. The retrieved context should contain information only relevant to the query or the prompt. For context relevance, a metric 'S' is estimated. 'S' is the number of sentences in the retrieved context that are relevant for responding to the query or the prompt.

**Answer Faithfulness**: A measure of the extent to which the response is factually grounded in the retrieved context. Faithfulness ensures that the facts in the response do not contradict the context and can be traced back to the source. It also ensures that the LLM is not hallucinating. Faithfulness first identifies the number of "claims" made in the response and calculates the proportion of those "claims" present in the context.

**Hallucination Rate**: Calculate the proportion of generated claims in the response that are not present in the retrieved context

**Coverage**: Measures the number of relevant claims in the context and calculates the proportion of relevant claims present in the generated response. This measures how much of the relevant information from the retrieved passages is included in the generated answer.

**Answer Relevance**: Measure of the extent to which the response is relevant to the query. This metric focusses on key aspects such as system's ability to comprehend the query, response being pertinent to the query and the completeness of the response.

**Ground truth**: Information that is known to be real or true. In RAG, and Generative AI domain in general, Ground Truth is a prepared set of Prompt-Context-Response or Question-Context-Response example, akin to labelled data in Supervised Machine Learning parlance. Ground truth data that is created for your knowledge base can be used for evaluation of your RAG system.

**Human Evaluation**: A subject matter expert looking at the documents and determines the relevance and accuracy of the outputs.

**Noise Robustness**: It is impractical to assume that the information stored in the knowledge base for RAG systems is perfectly curated to answer the questions that can be potentially asked of the system. It is very probable that a document is related to the user query but does not have any meaningful information to answer the query. The ability of the RAG system to separate these noisy documents from the relevant ones is Noise Robustness.

**Negative Rejection**: By nature, Large Language Models always generate text. It is possible that there is absolutely no information about the user query in the documents in the knowledge base. The ability of the RAG system to not give an answer when there is no relevant information is Negative Rejection.

**Information Integration**: It is also very likely that to answer a user query comprehensively the information must be retrieved from multiple documents. This ability of the system to assimilate information from multiple documents is Information Integration.

**Counterfactual Robustness**: Sometimes the information in the knowledge base might itself be inaccurate. A high-quality RAG system should be able to address this and reject known inaccuracies in the retrieved information. This ability is Counterfactual Robustness