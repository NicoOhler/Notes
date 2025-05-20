###  RAG Concepts
**Parametric Memory**: The ability of an LLM to retain information that it has been trained on is solely reliant on its parameters. It can therefore be said that LLMs store factual information in their parameters. This memory that is internally present in the LLM can be referred to as the parametric memory. This parametric memory is limited. It depends upon the number of parameters and is a factor of the data on which the LLM has been trained on.

**Non-parametric Memory**: Information that LLMs do not have in their internal parameters but can access via external retrieval mechanisms, like a search engine or database. RAG provides the LLM with access to this non-parametric memory.

**Knowledge Base**: The non-parametric memory that has been created for the RAG application. This contains information from a variety of pre-determined sources which is processed and stored in persistent memory

**User Query:** The prompt that a user (or a system) wants to send to an LLM for a response

**Retrieval**: The process via which, information pertinent to the user query is searched for and fetched from the knowledge base.

**Augmentation**: The process of adding the retrieved information to the user query.

**Generation**: The process of generating results by the LLM when provided with an augmented prompt.

**Source Citation**: Ability of a RAG system to point out to the information from the knowledge base that was used to generate the response

**Unlimited Memory**: The notion that any number of documents can be added to the RAG knowledge base

![None](https://miro.medium.com/v2/resize:fit:700/1*gl9E75jITNtszyUxaEPQvA.png)
