import requests
from bs4 import BeautifulSoup
from abc import ABC


class BaseScraper(ABC):
    def fetch_page(self, url: str) -> str:
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    def parse_xml(self, xml_content: str) -> list[str]:
        soup = BeautifulSoup(xml_content, "lxml-xml")
        return [loc.text for loc in soup.find_all("loc")]
