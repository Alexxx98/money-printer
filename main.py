from src.gpt import GPT
from src.tts import TTS


def main() -> None:
    gpt = GPT()
    tts = TTS()
    tts.generate_speech("siema byku, jak tam zdrowko?", "en-GB-SoniaNeural")


# Execute the app
if __name__ == "__main__":
    main()
