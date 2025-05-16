"""
Model responsible for generating a speech from the given text.
Repo of edge_tts library: https://github.com/rany2/edge-tts.

"""


import edge_tts


class TTS:
    audio_file = "speech.mp3"
    subtitles_file = "subtitles.srt"


    async def print_voices(self):
        """ Print all available voices. """

        # TODO: Print all available voices in the readable format, picking categories out.
        


    def generate_speech(self, text: str, voice: str) -> None:
        """ Generate the speech with subtitles. """

        # Generate speech
        communicate = edge_tts.Communicate(text, voice)

        # Subtitles buffer
        submaker = edge_tts.SubMaker()

        # Write data to files
        with open(self.audio_file, 'wb') as file:
            for chunk in communicate.stream_sync():
                # if data type equals to audio
                if chunk["type"] == "audio":
                    # Write chunk data to audio file
                    file.write(chunk["data"])
                # if data type equals to subtitles
                elif chunk["type"] == "WordBoundary":
                    # Write chunk to the submaker buffer
                    submaker.feed(chunk)

        # Write subtitles to the srt file
        with open(self.subtitles_file, 'w', encoding="utf-8") as file:
            file.write(submaker.get_srt())
