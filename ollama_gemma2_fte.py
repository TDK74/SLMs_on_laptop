from ollama import Client


def main():
    """
    Sends user's request to the pre-chosen Ollama model.
    """
    input_prompt = input("Please, enter your prompt (in the terminal): \n")
    print("Waiting for SLM's response... \n")

    try:
        client = Client(host = 'http://localhost:11434')
        response = client.generate(model = 'gemma2:2b', prompt = input_prompt)
        print(f"Gemma's message: \n{response['response']} \n")

    except RuntimeError as e:
        print(f"Runtime Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
