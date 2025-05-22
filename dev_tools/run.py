"""
Test methods of app's objects in the terminal
Usage: python3 dev_tools/run.py <module> <function> args...

"""

import os
import sys
import asyncio

# Add the parent directory of "tools/" to the module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import gpt, tts, pexels
from typing import List


def main() -> None:
    if len(sys.argv) < 3:
        return "Error code 1\n"\
        "Proper usage: python3 dev_tools/run.py <module> <function> [args...]\n"\
        "For more info: python3 dev_tools/run.py --help"

    module: str = sys.argv[1]
    func: str = sys.argv[2]

    # Prevent from raising an error if no args provided
    try:
        args: List[str] = sys.argv[3:]
    except:
        pass

    # GPT module methods
    if module == "gpt":
        prompt: str = args[0] if args else None
        if func == "generate_text":
            web_search: bool = args[1] if len(args) > 1 else False
            return gpt.generate_text(prompt, web_search)
        
        elif func == "generate_image":
            return gpt.generate_image(prompt)

    # TTS module methods 
    elif module == "tts":
        if func == "print_voices":
            language: str = args[0] if args else "English"
            return asyncio.run(tts.print_voices(language))
        
        elif func == "generate_speech":
            text: str = args[0] if args else None
            voice: str = args[1] if len(args) > 1 else "en-US-ChristopherNeural"
            return tts.generate_speech(text, voice)
      
    # Pexels module methods 
    elif module == "pexels":
        query: str = args[0] if args else None
        if func == "search_for_pohoto":
            curated: bool = args[1] if len(args) > 1 else False
            pexels.search_for_photo(query, curated)

        elif func == "search_for_video":
            popular: bool = args[1] if len(args) > 1 else False
            pexels.search_for_video(query, popular)


if __name__ == "__main__":
    main()
