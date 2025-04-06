

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
