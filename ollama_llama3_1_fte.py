from ollama import Client


def main():
    """
    Send user request to the pre-chosen Ollama model.
    """
    input_prompt = input("Please, enter your prompt (in the terminal): \n")
    print("Waiting for SLM's response... \n")

    try:
        client = Client(host = 'http://localhost:11434')
        response = client.generate(model = 'llama3.1:8b', prompt = input_prompt)
        print(f"Llama's message: \n{response['response']} \n")

    except RuntimeError as e:
        print(f"Runtime Error: {e}")

    except Exception as e:
        print(f"An unexpected error occured: {e}")


if __name__ == "__main__":
    main()
