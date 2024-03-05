import os;
from openai import OpenAI;

llm = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
    #base_url="http://localhost:1234/v1" - Will use this for LM Studio local inference server
)

system_prompt = """
Givne the short description of a particular topic, write 3 attention grabbing headlines for a presentation.
Reply with only the titles, one on each line with no additional text.
DESCRIPTION:    
"""

user_input = """
AI Orchestration with Langchain and llamaindex
keywords: Generative AI, applications, LLM, chatbot
"""

response = llm.chat.completions.create(
    model="gpt-4-1106-preview",
    max_tokens=500,
    temperature=0.8,
    messages=[
        {"role" : "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]
)

print(response.choices[0].message.content)