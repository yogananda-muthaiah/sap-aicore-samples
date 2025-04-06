

```
from gen_ai_hub.proxy.native.openai import completions

response = completions.create(
    model_name="meta--llama3.1-70b-instruct",
    prompt="The Answer to the Ultimate Question of Life, the Universe, and Everything is",
    max_tokens=20,
    temperature=0
)
print(response)
```


```
from gen_ai_hub.proxy.native.openai import chat

messages = [{"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
            {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
            {"role": "user", "content": "Do other Azure Cognitive Services support this too?"}]

kwargs = dict(model_name='gpt-4o-mini', messages=messages)
response = chat.completions.create(**kwargs)

print(response)
```

```
#example where deployment_id is passed instead of model_name parameter

from gen_ai_hub.proxy.native.openai import chat

messages = [{"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
            {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
            {"role": "user", "content": "Do other Azure Cognitive Services support this too?"}]

response = chat.completions.create(deployment_id="dcef02e219ae4916", messages=messages)
print(response)
```



```
from gen_ai_hub.proxy.native.google_vertexai.clients import GenerativeModel
from gen_ai_hub.proxy.core.proxy_clients import get_proxy_client

proxy_client = get_proxy_client('gen-ai-hub')
kwargs = dict({'model_name': 'gemini-1.0-pro'})
model = GenerativeModel(proxy_client=proxy_client, **kwargs)
content = [{
    "role": "user",
    "parts": [{
        "text": "Write a short story about a magic kingdom."
    }]
}]
model_response = model.generate_content(content)
print(model_response)
```

### Function Calling
```
from gen_ai_hub.proxy.native.google_vertexai.clients import GenerativeModel
# According to Gemini API it is recommended to use function_calling via chat interface, as this captures user-model back-and-forth interaction.

# example 1 of function calling using start_chat
def multiply(a:float, b:float):
    """returns a * b."""
    return a*b

kwargs = {'model_name': 'gemini-1.0-pro'}
model = GenerativeModel(**kwargs)
chat = model.start_chat(enable_automatic_function_calling=True)
prompt = 'I have 6 cats, each owns 2 mittens, how many mittens is that in total?'
response = chat.send_message(prompt, tools=[multiply])

print(response)
for content in chat.history:
    part = content.parts[0]
    print(content.role, "->", type(part).to_dict(part))
    print('-'*80)
```
