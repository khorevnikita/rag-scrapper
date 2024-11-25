from interfaces import LinkCollector, TextExtractor
from base_scraper import BaseScraper
from bs4 import BeautifulSoup
import json


class WhoLinkCollector(BaseScraper, LinkCollector):
    def collect_links(self, base_url: str) -> list[str]:
        take = 100
        skip = 0
        links = []
        while True:
            url = f"{base_url}&$skip={skip}&$top={take}"
            json_content = self.fetch_page(url)
            data = json.loads(json_content)
            page_links = [i["DownloadUrl"] for i in data["value"] if len(i["DownloadUrl"]) > 0]
            if len(page_links) == 0:
                break

            skip += take
            links += page_links

        return links


class WhoTextExtractor(TextExtractor):
    def extract_text(self, page_content: str) -> str:
        soup = BeautifulSoup(page_content, "html.parser")
        content = soup.find("article")
        if not content:
            content = soup.find("main", id="maincontent")
        if not content:
            raise ValueError("Unknown website")
        # Возвращаем текст, если элемент найден, иначе пустой словарь
        return content.get_text(strip=True)
