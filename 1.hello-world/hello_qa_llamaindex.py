from llama_index.core import Document, VectorStoreIndex

# import logging, sys
# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

documents = [
    Document(text="Lal Bahadur Shastri was the 3rd prime minister of the India."),
    Document(text="Atal Bihari Vajpayee was the prime minister of the India during March 1998 to May 2004."),
    Document(text="Narendra Modi is the present prime minister of the Bharat."),
]

index = VectorStoreIndex(documents)
query_engine = index.as_query_engine()

resp1 = query_engine.query("Who is current prime minister of India")
print(resp1)

resp2 = query_engine.query("Is Atal Bihari Vajpayee was prime minister for 2 times?")
print(resp2)

resp3 = query_engine.query("Who was the prime minister during year 2000")
print(resp3)
