"""
Looking for photos and videos, that fits the generated text.
Using pexels api.

"""


from dotenv import load_dotenv
from typing import List

import os
import requests


# Load environmental variables from the .env file
load_dotenv()


class Pexels:
    standard_endpoint = "https://api.pexels.com/v1/"
    video_endpoint = "https://api.pexels.com/videos/"
    api_key = os.getenv("PEXELS_API_KEY")


    def search_for_photo(self, query: str, curated: bool = False) -> List[str]:
        """ Search the regular pexels photo library or the curated section """

        section: str
        section = "curated" if curated else "search"

        response = requests.get(self.standard_endpoint + f"{section}?query={query}", headers={"Authorization": self.api_key})
        if response.ok:
            photos_data: List[dict] = response.json()['photos']
            photo_urls: List[str] = [photo["url"] for photo in photos_data]

            return photo_urls
        else:
            return f"Error code: {response.status_code}"


    def search_for_video(self, query: str, popular: bool = False) -> List[str]:
        """ Search th regular pexels video library or the popular one """

        section: str
        section = "popular" if popular else "search"

        response = requests.get(self.standard_endpoint + f"{section}?query={query}", headers={"Authorization": self.api_key})
        if response.ok:
            photos_data: List[dict] = response.json()['photos']
            photo_urls: List[str] = [photo["url"] for photo in photos_data]

            return photo_urls
        else:
            return f"Error code: {response.status_code}"
