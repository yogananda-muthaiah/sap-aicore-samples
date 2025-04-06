
### OpenAI
```
from gen_ai_hub.proxy.native.openai import chat

def stream_openai(prompt, model_name='gpt-4o-mini'):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    
    kwargs = dict(model_name=model_name, messages=messages, max_tokens=500, stream=True)
    stream = chat.completions.create(**kwargs)
    
    for chunk in stream:
        if chunk.choices:
            content = chunk.choices[0].delta.content
            if content:
                print(content, end='')

stream_openai("Why is the sky blue?")
```
### Google Gemini

```
from gen_ai_hub.proxy.native.google_vertexai.clients import GenerativeModel
from vertexai.generative_models import GenerationConfig


def stream_gemini(prompt, model_name='gemini-1.5-flash'):
    generation_config = GenerationConfig(max_output_tokens=500)
    model = GenerativeModel(model_name=model_name, generation_config=generation_config)
    stream = model.generate_content(prompt, stream=True)
    
    for chunk in stream:
        print(chunk.text, end='')    
stream_gemini("Why is the sky blue?")
```
