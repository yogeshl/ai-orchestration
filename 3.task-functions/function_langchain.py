from langchain_openai.chat_models import ChatOpenAI
from langchain.chains.structured_output import create_openai_fn_runnable
from langchain.prompts import ChatPromptTemplate
import json
import random

def get_weather_for_city(city: str):
    print(f"Calling local get_weather_for_city for {city}")
    return json.dumps({"city": city, "temperature": random.randint(1,50)})

llm = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo-1106"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "What's the weather like in {location}?")
    ]
)

chain = create_openai_fn_runnable([get_weather_for_city], llm, prompt)
response = chain.invoke({"location": "Georgia"})

print(response)