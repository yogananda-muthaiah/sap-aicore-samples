

```
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from gen_ai_hub.proxy.langchain.init_models import init_llm

template = """Question: {question}
    Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=['question'])
question = 'What is a supernova?'

llm = init_llm('meta--llama3.1-70b-instruct', max_tokens=300)
chain = prompt | llm | StrOutputParser()
response = chain.invoke({'question': question})
print(response)
```

```
from gen_ai_hub.proxy.langchain.init_models import init_embedding_model

text = 'Every decoding is another encoding.'

embeddings = init_embedding_model('text-embedding-ada-002')
response = embeddings.embed_query(text)
print(response)
```

### LLM

```
from langchain import PromptTemplate

from gen_ai_hub.proxy.langchain.openai import OpenAI  # langchain class representing the AICore OpenAI models
from gen_ai_hub.proxy.core.proxy_clients import get_proxy_client

proxy_client = get_proxy_client('gen-ai-hub')
# non-chat model
model_name = "meta--llama3.1-70b-instruct"

llm = OpenAI(proxy_model_name=model_name, proxy_client=proxy_client)  # can be used as usual with langchain

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = prompt | llm

question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"

print(llm_chain.invoke({'question': question}))
```
