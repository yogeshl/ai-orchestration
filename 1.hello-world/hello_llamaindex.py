from llama_index.llms.openai_like import OpenAILike
from llama_index.core.llms import ChatMessage

application_prompt = """
Givne the short description of a particular topic, write 3 attention grabbing headlines for a presentation.
Reply with only the titles, one on each line with no additional text.
DESCRIPTION:    
"""

user_data = """
AI Orchestration with Langchain and llamaindex
keywords: Generative AI, applications, LLM, chatbot
"""

llm = OpenAILike(
    is_chat_model=True,
    temperature=0.8,
    max_tokens=500,
    model="gpt-4-1106-preview"
)

messages =[
    ChatMessage(role="system", content=application_prompt),
    ChatMessage(role="user", content=user_data),
]

# result = llm.chat(messages=messages)
# print(result)

# for streaming
resp = llm.stream_chat(messages=messages)
for chunk in resp:
    print(chunk.delta, end="")