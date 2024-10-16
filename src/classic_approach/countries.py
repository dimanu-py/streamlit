import random

import streamlit as st
import requests



class Text:

    content: str

    def __init__(self) -> None:
        self.content = ""

    def render(self, content: str) -> None:
        self.content = content
        st.write(self.content)


class Image:

    width: int | None
    url: str

    def __init__(self) -> None:
        self.url = ""
        self.width = None

    def render(self, url: str, width: int | None =None) -> None:
        self.url = url
        self.width = width
        st.image(self.url, width=self.width)


class CountriesApp:

    def __init__(self) -> None:
        self._req = requests

    def main(self, limit: int = 10) -> None:
        st.header("Countries")

        if st.button("Load Countries", type="primary"):
            response = self._req.get("https://restcountries.com/v2/all?fields=name,capital,flag")
            content = response.json()
            random.shuffle(content)

            for item in content[0:limit]:
                name = item["name"]
                flag = item["flag"]
                capital = item.get("capital", "N/A")

                text = Text()
                text.render(f"Country: {name}, Capital: {capital}")

                image = Image()
                image.render(url=flag, width=100)


if __name__ == '__main__':
    app = CountriesApp()
    app.main()