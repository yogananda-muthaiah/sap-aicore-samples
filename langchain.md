

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

### Chat Model

```
from langchain.prompts.chat import (
    AIMessagePromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

from gen_ai_hub.proxy.langchain.openai import ChatOpenAI
from gen_ai_hub.proxy.core.proxy_clients import get_proxy_client

proxy_client = get_proxy_client('gen-ai-hub')

chat_llm = ChatOpenAI(proxy_model_name='gpt-4o-mini', proxy_client=proxy_client)
template = 'You are a helpful assistant that translates english to pirate.'

system_message_prompt = SystemMessagePromptTemplate.from_template(template)

example_human = HumanMessagePromptTemplate.from_template('Hi')
example_ai = AIMessagePromptTemplate.from_template('Ahoy!')
human_template = '{text}'

human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, example_human, example_ai, human_message_prompt])

chain = chat_prompt | chat_llm

response = chain.invoke({'text': 'I love planking.'})
print(response.content)
```

Embedding

```
from gen_ai_hub.proxy.langchain.openai import OpenAIEmbeddings
from gen_ai_hub.proxy.core.proxy_clients import get_proxy_client

proxy_client = get_proxy_client('gen-ai-hub')

embedding_model = OpenAIEmbeddings(proxy_model_name='text-embedding-ada-002', proxy_client=proxy_client)

response = embedding_model.embed_query('Every decoding is another encoding.')

#call without passing proxy_client

embedding_model = OpenAIEmbeddings(proxy_model_name='text-embedding-ada-002')

response = embedding_model.embed_query('Every decoding is another encoding.')
print(response)
```
