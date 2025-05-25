"""
Repo of g4f library: https://github.com/xtekky/gpt4free

"""


import g4f

from g4f.client import Client
from g4f.Provider import RetryProvider, Blackbox, Chatai, DuckDuckGo, Pizzagpt, PollinationsAI


g4f.debug.logging = True
g4f.debug.version_check = False

class GPT:
    client = Client(client=RetryProvider([Blackbox, DuckDuckGo, Chatai, Pizzagpt, PollinationsAI ], shuffle=False))


    def print_providers(self, chat_model: str) -> None:
        # TODO: List all available providers whith no auhtentication require and for specific chat model.
        ...


    def generate_text(self, prompt: str, web_search: bool = False) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            web_search=web_search
        )

        # content of gpt's response
        text: str = response.choices[0].message.content

        # get text after the first colon
        text = (' ').join(text.split(':')[1:])
        
        return text
    

    def generate_image(self, prompt: str) -> str:
        response = self.client.images.generate(
            model="flux",
            prompt=prompt,
            response_format="url"
        )

        return response.data[0].url
