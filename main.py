from src.gpt import GPT


def main() -> None:
    gpt = GPT()
    print(gpt.generate_image("gorilla smoking zaza"))


# Execute the app
if __name__ == "__main__":
    main()
