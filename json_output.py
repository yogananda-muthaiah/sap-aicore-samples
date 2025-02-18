import openai 

system_prompt = """You are a helpful assistant designed to output this JSON format:
```
{
    "functions": [
        {
            "name": "<Function name>",
            "arguments": {
                "<argument name>": "<argument value>"
            }
        }
    ]
}
```
"""

functions = [
    {
        "type": "function",
        "function": {
            "name": "get_world_series_winner",
            "description": "Get the world series winner in a given year",
            "parameters": {
                "type": "object",
                "properties": {
                    "year": {"type": "integer"}
                },
                "required": ["year"],
            },
        },
    }
]

response = openai.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  response_format={"type": "json_object"},
  tool_choice="none",  # to force the response to be in free-form text
  tools=functions,   
  messages=[
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "Who won the world series in 2020?"}
  ]
)

print(response.choices[0].message.content)
# '{"functions": [{name="get_world_series_winner", "arguments": {"year": 2020}}]}'

print(response.choices[0].message.tool_calls)
# None
