import datetime
import random
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# task functions
def getTime():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%dT%H:%M")

def getWeather(city: str):
    print(f"Calling local getweather for {city}")
    return f"The weather in {city} is {random.randint(1,50)}C."

# task offloading prompt.
system_prompt =  """
You are a helpful assistant. If asked something you don't know for sure,
of if you are requested to perform an action you are not otherwise capable of,
YOU may choose to respond with one of the following commands, which will get fulfilled
in a subsequent conversational turn:

"#TASK:TIME" to request the current time and date in a format like 2024-01-01T12:34
"#TASK:WEATHER city" to request the current weather in a given city

Do not include any additional explanation when replying with one of these commands.
Upon receiving a response from a command, rephrase it in friendly language,
without adding any additional explanation.

Current conversation:
{history}

Human: {input}
AI:
"""

def main():
    llm = ChatOpenAI(
        #base_url="http://localhost:1234/v1",
        verbose=True,
        temperature=0.6
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt)
        ]
    )

    conversation = ConversationChain(
        llm=llm,
        prompt=prompt,
        verbose=True
    )

    # REPL loop
    observation = None
    cli_prompt = "Ask a question. Type 'exit' to quit.\n>"
    while True:
        user_input = observation if observation else  input(cli_prompt)
        observation = None
        
        if user_input=='exit':
            break

        result = conversation.invoke({"input": user_input})
        print(f"Result: {result}");

        response = result["response"].strip()
        print("AI: ", response)

        if response.startswith("#TASK:"):
            cmd = response[6:]
            print(f"got a task offloading request.. {cmd}.")
            
            if cmd=="TIME":
                observation = getTime()
                print(f"observation: {observation}")
            elif cmd.startswith("WEATHER "):
                city = cmd[8:]
                observation = getWeather(city)
                print(f"observation: {observation}")
            else:
                print("Unknown task")
                observation = None


if __name__ == "__main__":
    main()