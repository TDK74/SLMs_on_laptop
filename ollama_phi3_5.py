from ollama import Client


input_prompt = input("Please, enter your prompt (in the terminal): \n")
print("Waiting for SLM's response... \n")

# If Ollama is on the local host.
client = Client(host = 'http://localhost:11434')
response = client.generate(model =  'phi3.5:3.8b', prompt =  input_prompt)

print(f"Phi's message: \n{response['response']} \n")
