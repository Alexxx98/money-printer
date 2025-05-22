"""
Usage: python3 main.py "<prompt>"

"""

import sys


def main() -> None:
    """ Function where the code is executed """

    if len(sys.argv) < 2:
        print('Error bad usage')
        print('Proper usage: python3 main.py "<prompt>"\n')
        return
    
    # Import modules
    from src import gpt, tts, pexels

    # Input as a string
    prompt = sys.argv[1]

    # Generate text from the prompt
    text: str = gpt.generate_text(prompt)

    # generate speech with subtitles from the generated text
    # with the method's default voice
    tts.generate_speech(text)


# Execute the app
if __name__ == "__main__":
    main()
