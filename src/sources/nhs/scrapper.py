from interfaces import LinkCollector, TextExtractor
from base_scraper import BaseScraper
from bs4 import BeautifulSoup


class NHSLinkCollector(BaseScraper, LinkCollector):
    def collect_links(self, url: str) -> list[str]:
        xml_content = self.fetch_page(url)
        return self.parse_xml(xml_content)

    def parse_xml(self, xml_content: str) -> list[str]:
        soup = BeautifulSoup(xml_content, "lxml-xml")
        return [loc.text for loc in soup.find_all("loc") if "/live-well/" in loc.text]


class NHSTextExtractor(TextExtractor):
    def extract_text(self, page_content: str) -> str:
        soup = BeautifulSoup(page_content, "html.parser")
        content = soup.find("article")
        if not content:
            content = soup.find("main", id="maincontent")
        if not content:
            raise ValueError("Unknown website")
        # Возвращаем текст, если элемент найден, иначе пустой словарь
        return content.get_text(strip=True)
