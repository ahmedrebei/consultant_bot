from bs4 import BeautifulSoup, NavigableString, Comment
import requests
import re
from typing import Optional


class Html_parser:
    """
    A class to parse HTML webpages with functionalities.
    """
    def __init__(self, url: str) -> None:
        if not re.match(r"https?://(?:www\.)?quebec\.ca", url):
            raise ValueError("Invalid URL. The URL must be from quebec.ca.")
        self.url: str = url
        self.soup: Optional[BeautifulSoup] = None
        
    def fetch_html(self) -> None:
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            self.soup = soup
        else:
            print("status code is", response.status_code)
            raise ValueError("Failed to fetch the HTML content.")
            
    def get_page_title(self) -> str:
        if not self.soup:
            self.fetch_html()

        title = self.soup.find("h1")
        return title.get_text(strip=True)
    
    def get_main_div(self) -> str:
        """
        Finds the div with id "main" considering inconsistent header structures.
        """
        if not self.soup:
            self.fetch_html()

        main_div = self.soup.find("div", id="main")
        divs = main_div.find_all("div", class_="col-12")

        text_column = max(divs, key=lambda div: len(div.get_text(strip=True)))

        return text_column

    def _decompose_non_text_tags(self, element: BeautifulSoup) -> None:
        non_text_tags = {
            "script",
            "style",
            "link",
            "meta",
            "input",
            "img",
            "br",
            "hr",
            "iframe",
            "form",
            "button",
            "nav",
            "template",
        }
        for tag in non_text_tags:
            for match in element.findAll(tag):
                match.decompose()
        for child in element.children:
            if child.name:
                self._decompose_non_text_tags(child)
        for comment in element.find_all(text=lambda text: isinstance(text, Comment)):
            comment.extract()

    def _get_text_recursively(self, div: BeautifulSoup) -> str:
        """
        Recursively extracts text from the given div element and its children.

        Args:
            div (BeautifulSoup.Tag): The div element to extract text from.

        Returns:
            str: The extracted text.

        """

        text = ""
        for tag in div.recursiveChildGenerator():

            if isinstance(tag, NavigableString):
                tag_text = tag.strip()
                text += tag_text + "\n" if tag_text else ""
        return text

    def get_text_from_web_page(self, main_div: BeautifulSoup) -> str:
        text = ""
        self._decompose_non_text_tags(main_div)
        for child in main_div.find_all(recursive=False):
            text += self._get_text_recursively(child).strip() + "\n"
        return text
    
def main() -> None:
    link = "https://www.quebec.ca/immigration/permanente/travailleurs-qualifies/programme-regulier-travailleurs-qualifies/declaration-interet"
    parser = Html_parser(link)
    parser.fetch_html()
    main_div = parser.get_main_div()
    text = parser.get_text_from_web_page(main_div)
    print(text)

if __name__ == "__main__":
    main()