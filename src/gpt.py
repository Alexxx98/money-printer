from g4f.client import Client


class GPT:
    client = Client()


    def generate_text(self, prompt: str, web_search: bool) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            web_search=web_search
        )

        return response.choices[0].message.content
    

    def generate_image(self, prompt: str) -> str:
        response = self.client.images.generate(
            model="flux",
            prompt=prompt,
            response_format="url"
        )

        return response.data[0].url
