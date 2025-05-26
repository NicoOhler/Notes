tasks:
	explore different LLMS?
	explore chunking methods
		small to big chunking?
	explore databases/index methods
	use different LLMS for chunk search and answer generation
	explore prompts
		task description
		number of attached chunks + formatting
		output format

rewrite chunks using LLM before storing them in knowledge base
evaluate using LLM-as-a-Judge
hybrid retrieval using a combination of vector and lexical search 
accuracy declines dramatically if the relevant information is somewhere in the middle of the prompt. This problem can be addressed by passing only the relevant information to the LLM instead of the entire document.
Corrective RAG: In this approach, real-time information is retrieved to check for the factual accuracy of the LLM generated answer. Particularly useful in fact-checking, medical & legal domains.
generate answer without context. Then ask llm to revise its previous answer given the context.
rerank using lightweight llm?
rewrite query using lightweight llm - not needed in our case right? unless we want to rewrite articles
use lightweight llm to rewrite the retrieved documents to make it more relevant to the query?
DEFAULT_TRANSFORM_QUERY_TEMPLATE = PromptTemplate(
    template="""Your task is to refine a query to ensure it is highly effective for retrieving relevant search results. \n
    Analyze the given input to grasp the core semantic intent or meaning. \n
    Original Query:
    \n ------- \n
    {query_str}
    \n ------- \n
    Your goal is to rephrase or enhance this query to improve its search performance. Ensure the revised query is concise and directly aligned with the intended search objective. \n
    Respond with the optimized query only:"""
)

include (not) credible sources in the knowledge base.
confidence
step by step reasoning
	either free form or dictate structure like this
	First, assess the **source reliability**.  
	Next, compare the article's claims against the retrieved **scientific context**.  
	Then, determine whether the article supports or contradicts **scientific consensus**.  
	Finally, produce your JSON output.

prompt hyperparameter:
	neg example
	pos example
	json format
	context
	if context irrelevant => still come to conclusion
	If the context contradicts the article, prioritize the context.
	1. Watch for biased language, scientific distortion, or claims that contradict established climate science.
	Do not trust claims solely because they are presented in technical language.  
	Do not classify an article as trustworthy if the source is known to spread disinformation.  
	Avoid relying on tone or writing style; evaluate factual claims only.
	examples after actual task
