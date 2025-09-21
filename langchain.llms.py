from langchain.llms import OpenAI

# Accessing the OPENAI KEY
# Simple LLM call Using LangChain
llm = OpenAI(model_name="text-davinci-003", openai_api_key='API_KEY')
question = "Which language is used to create chatgpt ?"
print(question, llm(question))
