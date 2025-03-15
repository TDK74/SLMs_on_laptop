from ollama import Client


input_prompt = input("Please, enter your prompt (in the terminal): \n")
print("Waiting for SLM's response... \n")

# if Ollama is on the local host
client = Client(host = 'http://localhost:11434')
response = client.generate(model = 'llama3.1:8b', prompt = input_prompt)

print(f"Llama's message: \n{response['response']} \n")
